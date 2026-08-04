#Requires -Version 7
# Submits run A and run B of this study to OpenRouter, polls both to a terminal
# status, downloads completed videos, and saves every response OUTSIDE the repo.
# The API key is read from the process environment or HKCU\Environment and is
# never printed.
$ErrorActionPreference = "Stop"

$studyName = "2026-08-04-seedance20-openrouter-prose-identity"
$repoRoot  = (Resolve-Path (Join-Path $PSScriptRoot "..\..\..")).Path
$mediaDir  = Join-Path (Split-Path $repoRoot -Parent) "field-study-media\$studyName"
New-Item -ItemType Directory -Force $mediaDir | Out-Null

$key = $env:OPENROUTER_API_KEY
if (-not $key) { $key = [Microsoft.Win32.Registry]::GetValue("HKEY_CURRENT_USER\Environment", "OPENROUTER_API_KEY", $null) }
if (-not $key) { throw "OPENROUTER_API_KEY is not set in the process environment or HKCU\Environment." }
$key = "$key".Trim().Trim('"').Trim("'")
if ($key -notmatch "^sk-or-v1-") { throw "Stored key is malformed (length $($key.Length), no sk-or-v1- prefix). Re-run setx with the complete key." }

$auth = @{ Authorization = "Bearer $key" }

# Free authenticated endpoint; throws on 401 so a bad key can never reach a paid submission.
$preflight = Invoke-RestMethod -Method Get -Uri "https://openrouter.ai/api/v1/key" -Headers $auth
"{0}  auth preflight ok (key label: {1})" -f (Get-Date -Format o), $preflight.data.label
$jobs = [ordered]@{}

foreach ($run in "A", "B") {
    $body = Get-Content -Raw (Join-Path $PSScriptRoot "requests\run$run-request.json")
    $resp = Invoke-RestMethod -Method Post -Uri "https://openrouter.ai/api/v1/videos" -Headers ($auth + @{ "Content-Type" = "application/json" }) -Body $body
    $resp | ConvertTo-Json -Depth 10 | Set-Content (Join-Path $mediaDir "run$run-submit-response.json")
    $jobs[$run] = $resp
    "{0}  run{1} submitted: id={2} status={3}" -f (Get-Date -Format o), $run, $resp.id, $resp.status
}

$pending  = [System.Collections.Generic.List[string]]@("A", "B")
$deadline = (Get-Date).AddMinutes(20)
$final    = [ordered]@{}

while ($pending.Count -gt 0 -and (Get-Date) -lt $deadline) {
    Start-Sleep -Seconds 15
    foreach ($run in @($pending)) {
        $url = $jobs[$run].polling_url
        if (-not $url) { $url = "https://openrouter.ai/api/v1/videos/$($jobs[$run].id)" }
        $p = Invoke-RestMethod -Method Get -Uri $url -Headers $auth
        "{0}  run{1}: {2}" -f (Get-Date -Format o), $run, $p.status
        if ($p.status -in "completed", "failed", "cancelled", "expired") {
            $p | ConvertTo-Json -Depth 10 | Set-Content (Join-Path $mediaDir "run$run-poll-final.json")
            $final[$run] = $p
            [void]$pending.Remove($run)
        }
    }
}
if ($pending.Count -gt 0) { "TIMEOUT: still pending after 20 minutes: $($pending -join ', ')" }

foreach ($run in $final.Keys) {
    $p = $final[$run]
    if ($p.status -eq "completed") {
        $out = Join-Path $mediaDir "run$run.mp4"
        Invoke-WebRequest -Uri "https://openrouter.ai/api/v1/videos/$($jobs[$run].id)/content?index=0" -Headers $auth -OutFile $out
        "{0}  run{1} downloaded: {2:N0} bytes -> {3}" -f (Get-Date -Format o), $run, (Get-Item $out).Length, $out
    } else {
        "run{0} terminal status: {1}; error: {2}" -f $run, $p.status, ($p.error | ConvertTo-Json -Compress -Depth 5)
    }
    "run{0} usage: {1}" -f $run, ($p.usage | ConvertTo-Json -Compress -Depth 5)
}
"DONE"
