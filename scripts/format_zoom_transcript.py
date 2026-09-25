#!/usr/bin/env python3
"""Turn a saved Zoom get_recording_resource result into a transcript file.

usage: format_zoom_transcript.py RAW_JSON OUT_TXT DATE TOPIC MEETING_UUID SOURCE
  RAW_JSON  the file the harness saved the tool result to (or any file holding that JSON)
  SOURCE    "transcript" or "summary"
exit 2 = the response held no timeline entries (fall back to summary, or record no_transcript)
"""
import json, sys

raw, out, date, topic, uuid, source = sys.argv[1:7]
p = json.load(open(raw, encoding="utf-8"))
# Some harness versions wrap MCP output as [{"type": "text", "text": "<json>"}]
if isinstance(p, list) and p and isinstance(p[0], dict) and "text" in p[0]:
    p = json.loads(p[0]["text"])

entries = []
for key in ("transcripts", "summaries", "recordings"):
    for rec in p.get(key) or []:
        entries += rec.get("timeline") or []
if not entries:
    sys.exit(2)

lines = [f"Date: {date}", f"Topic: {topic}", f"Meeting UUID: {uuid}",
         f"Source: {source}", ""]
for e in entries:
    body = (e.get("text") or "").strip()
    if body:                                   # Zoom emits blank entries for pauses
        ts = str(e.get("ts") or "00:00:00").split(".")[0]   # whole seconds
        lines.append(f"[{ts}] {e.get('display_name') or 'Unknown'}: {body}")
open(out, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print(f"{out}: {len(lines) - 5} entries")
