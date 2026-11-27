from __future__ import annotations
import argparse
import json
import re
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path

PATTERN = re.compile(r"(?i)(?<![0-9a-f])[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}(?![0-9a-f])")
GREGORIAN_OFFSET = 12219292800
MASK_48 = (1 << 48) - 1
MASK_12 = (1 << 12) - 1

def timestamp_for(value: uuid.UUID):
    version = value.version
    if version == 1:
        seconds = value.time / 10_000_000 - GREGORIAN_OFFSET
    elif version == 6:
        time_high = (value.int >> 80) & MASK_48
        time_low = (value.int >> 64) & MASK_12
        seconds = ((time_high << 12) | time_low) / 10_000_000 - GREGORIAN_OFFSET
    elif version == 7:
        milliseconds = (value.int >> 80) & MASK_48
        seconds = milliseconds / 1000
    else:
        return None
    try:
        return datetime.fromtimestamp(seconds, tz=timezone.utc).isoformat()
    except (OverflowError, OSError, ValueError):
        return None

def inspect(text: str):
    found = []
    for match in PATTERN.finditer(text):
        try:
            value = uuid.UUID(match.group(0))
        except ValueError:
            continue
        found.append({
            "uuid": str(value),
            "version": value.version,
            "variant": value.variant,
            "timestamp_utc": timestamp_for(value),
        })
    counts = {}
    for item in found:
        counts[item["uuid"]] = counts.get(item["uuid"], 0) + 1
    for item in found:
        item["duplicate_count"] = counts[item["uuid"]]
    return found

def main(argv=None):
    parser = argparse.ArgumentParser(description="Inspect UUID versions, variants, timestamps, and duplicates.")
    parser.add_argument("values", nargs="*", help="UUID strings or text containing UUIDs")
    parser.add_argument("--file", type=Path, help="Read UUIDs from a local text file")
    parser.add_argument("--json", action="store_true", help="Print JSON output")
    args = parser.parse_args(argv)
    if args.file:
        try:
            text = args.file.read_text(encoding="utf-8")
        except OSError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 2
    elif args.values:
        text = "\n".join(args.values)
    else:
        text = sys.stdin.read()
    items = inspect(text)
    if args.json:
        print(json.dumps(items, indent=2))
    else:
        if not items:
            print("No UUIDs found.")
        for item in items:
            print(f"{item['uuid']}  version={item['version']}  variant={item['variant']}  "
                  f"timestamp={item['timestamp_utc'] or '-'}  occurrences={item['duplicate_count']}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
