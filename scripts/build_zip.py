"""Build the ZIP uploaded to the OpenAI plugin submission portal.

Checks the listing limits the portal enforces, then zips the plugin files
(no .git, no scripts, no dist) into dist/ondimi-weddings-<version>.zip.
Usage: python scripts/build_zip.py
"""
import json
import struct
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INCLUDE = ["plugin.json", "mcp.json", "README.md", "LICENSE", "skills", "assets"]


def check(manifest: dict, mcp: dict) -> list[str]:
    errors = []
    ui = manifest["extensions"]["com.openai"]["interface"]
    for key, limit in (("displayName", 30), ("shortDescription", 30), ("longDescription", 4000)):
        if len(ui.get(key, "")) > limit:
            errors.append(f"{key} is {len(ui[key])} chars (max {limit})")
    for key in ("websiteURL", "supportURL", "privacyPolicyURL", "termsOfServiceURL"):
        if not ui.get(key, "").startswith("https://"):
            errors.append(f"{key} must be an https URL")
    for key in ("logo", "composerIcon"):
        path = ROOT / ui[key]
        if not path.is_file():
            errors.append(f"{key} {ui[key]} is missing")
            continue
        head = path.read_bytes()[:24]
        w, h = struct.unpack(">II", head[16:24])
        if w != h or w < 48:
            errors.append(f"{key} must be square and at least 48px (is {w}x{h})")
    servers = mcp["mcpServers"]
    if len(servers) != 1:
        errors.append("exactly one MCP server per plugin")
    for name, server in servers.items():
        if server.get("headers"):
            errors.append(f"server {name}: public submission rejects headers")
    tests = manifest["extensions"]["com.openai"]["review"]["test_cases"]
    if len(tests["positive"]) < 5 or len(tests["negative"]) < 3:
        errors.append("need 5 positive and 3 negative test cases")
    for skill in sorted((ROOT / "skills").glob("*/SKILL.md")):
        if not skill.read_text(encoding="utf-8").startswith("---\nname: "):
            errors.append(f"{skill.relative_to(ROOT)} has no name frontmatter")
    return errors


def main() -> int:
    manifest = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
    mcp = json.loads((ROOT / "mcp.json").read_text(encoding="utf-8"))
    errors = check(manifest, mcp)
    if errors:
        print("\n".join("ERROR: " + e for e in errors))
        return 1
    out = ROOT / "dist" / f"{manifest['name']}-{manifest['version']}.zip"
    out.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for entry in INCLUDE:
            path = ROOT / entry
            files = [path] if path.is_file() else sorted(p for p in path.rglob("*") if p.is_file())
            for f in files:
                z.write(f, f.relative_to(ROOT).as_posix())
    print(f"wrote {out.relative_to(ROOT)}")
    with zipfile.ZipFile(out) as z:
        print("\n".join("  " + n for n in z.namelist()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
