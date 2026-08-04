"""Read duration, track dimensions, and track handlers from an MP4 container.

Pure standard library, no decoding. This reproduces the sibling record's
machine-side verification: duration, dimensions, and the presence of video
and audio tracks, read from the container itself.

Usage: python read_mp4_metadata.py file.mp4 [file2.mp4 ...]
"""

import struct
import sys

CONTAINERS = {b"moov", b"trak", b"mdia", b"minf", b"stbl"}


def walk(data, start, end, found):
    off = start
    while off + 8 <= end:
        size, btype = struct.unpack_from(">I4s", data, off)
        hdr = 8
        if size == 1:
            size = struct.unpack_from(">Q", data, off + 8)[0]
            hdr = 16
        elif size == 0:
            size = end - off
        if size < hdr or off + size > end:
            break
        body_s = off + hdr
        if btype in CONTAINERS:
            walk(data, body_s, off + size, found)
        elif btype == b"mvhd":
            ver = data[body_s]
            if ver == 1:
                timescale, duration = struct.unpack_from(">IQ", data, body_s + 20)
            else:
                timescale, duration = struct.unpack_from(">II", data, body_s + 12)
            found["duration_s"] = round(duration / timescale, 3) if timescale else None
        elif btype == b"tkhd":
            ver = data[body_s]
            w_off = body_s + (88 if ver == 1 else 76)
            w, h = struct.unpack_from(">II", data, w_off)
            if w and h:
                found.setdefault("track_dimensions", []).append(f"{w >> 16}x{h >> 16}")
        elif btype == b"hdlr":
            handler = data[body_s + 8:body_s + 12].decode("latin-1")
            found.setdefault("handlers", []).append(handler)
        off += size


def main(paths):
    for path in paths:
        with open(path, "rb") as f:
            data = f.read()
        found = {}
        walk(data, 0, len(data), found)
        handlers = found.get("handlers", [])
        print(path)
        print(f"  duration: {found.get('duration_s')} s")
        print(f"  track dimensions: {', '.join(found.get('track_dimensions', [])) or 'none found'}")
        print(f"  video track: {'yes' if 'vide' in handlers else 'no'}; audio track: {'yes' if 'soun' in handlers else 'no'}")
        print(f"  bytes: {len(data):,}")


if __name__ == "__main__":
    main(sys.argv[1:])
