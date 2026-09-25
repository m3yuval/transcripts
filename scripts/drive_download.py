#!/usr/bin/env python3
"""Decode a saved Google Drive download_file_content result to the original bytes.

usage: drive_download.py RAW_JSON OUT_FILE [EXPECTED_SIZE]
  RAW_JSON       the file the harness saved the tool result to: {"content": <base64>, ...}
  EXPECTED_SIZE  the fileSize from the Drive listing; exits 3 on mismatch
For a PDF, also writes OUT_FILE.txt with the extracted text (pages joined by form feed),
ready for turn splitting.
"""
import base64, json, sys

raw, out = sys.argv[1], sys.argv[2]
expected = int(sys.argv[3]) if len(sys.argv) > 3 else None
p = json.load(open(raw, encoding="utf-8"))
if isinstance(p, list) and p and isinstance(p[0], dict) and "text" in p[0]:
    p = json.loads(p[0]["text"])
data = base64.b64decode(p["content"])
open(out, "wb").write(data)
print(f"{out}: {len(data)} bytes ({p.get('mimeType')}, {p.get('title')})")
if expected is not None and len(data) != expected:
    print(f"SIZE MISMATCH: expected {expected}", file=sys.stderr)
    sys.exit(3)
if data[:5] == b"%PDF-":
    import io, pypdf
    reader = pypdf.PdfReader(io.BytesIO(data))
    text = "\f".join(page.extract_text() or "" for page in reader.pages)
    open(out + ".txt", "w", encoding="utf-8").write(text)
    print(f"{out}.txt: {len(reader.pages)} pages extracted")
