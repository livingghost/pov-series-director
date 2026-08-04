#Requires -Version 7
# Resumes polling for the two jobs already submitted by submit-and-poll.ps1,
# using the saved submit responses. Submits nothing, so it can never incur a
# new charge. Downloads completed videos and saves final poll responses.
$ErrorActionPreference = "Stop"

$studyName = "2026-08-04-seedance20-openrouter-prose-identity"
$repoRoot  = (Resolve-Path (Join-Path $PSScriptRoot "..\..\..")).Path
$mediaDir  = Join-Path (Split-Path $repoRoot -Parent) "field-study-media\$studyName"

$key = $env:OPENROUTER_API_KEY
if (-not $key) { $key = [Microsoft.Win32.Registry]::GetValue("HKEY_CURRENT_USER\Environment", "OPENROUTER_API_KEY", $null) }
if (-not $key) { throw "OPENROUTER_API_KEY is not set." }
$key = "$key".Trim().Trim('"').Trim("'")
if ($key -notmatch "^sk-or-v1-") { throw "Stored key is malformed (length $($key.Length))." }
$auth = @{ Authorization = "Bearer $key" }

$jobs = [ordered]@{}
foreach ($run in "A", "B") {
    $resp = Get-Content -Raw (Join-Path $mediaDir "run$run-submit-response.json") | ConvertFrom-Json
    $jobs[$run] = $resp
    "run{0}: resuming poll for id={1}" -f $run, $resp.id
}

$pending  = [System.Collections.Generic.List[string]]@("A", "B")
$deadline = (Get-Date).AddMinutes(60)
$final    = [ordered]@{}

while ($pending.Count -gt 0 -and (Get-Date) -lt $deadline) {
    Start-Sleep -Seconds 30
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
if ($pending.Count -gt 0) { "TIMEOUT: still pending after 60 more minutes: $($pending -join ', ')" }

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
