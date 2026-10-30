#!/usr/bin/env python3
"""Validate the existing repository shape; preserve upstream diagnostics verbatim.

Usage: python3 fidelity-ledger/validate_repository.py [--book-tools /path/to/Books-to-Skill-Refs]
The upstream path enables the full book/reference/budget and injection scans.
This checker does not run model acceptance or verify source audio.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys


def check(root, book_tools=None):
    errors = []
    for rel in ('SKILL.md', 'AGENTS.md', 'README.md', 'LICENSE', '.gitignore',
                'liu-zhongjing-confusion-patterns.md', 'fidelity-ledger/source-manifest.json'):
        if not (root / rel).is_file():
            errors.append('Missing ' + rel)
    core = (root / 'SKILL.md').read_text()
    if not re.match(r'\A---\nname: transcript-proofreader\ndescription: .+\n---\n', core):
        errors.append('Invalid skill name/frontmatter')
    alias = root / '.agents/skills/transcript-proofreader'
    if not alias.is_symlink() or alias.readlink().as_posix() != '../..' or alias.resolve() != root:
        errors.append('Discovery alias must be a relative symlink to canonical root')
    refs = sorted((root / 'references').glob('reference-*.md'))
    if len(refs) != 3:
        errors.append('Expected the existing three canonical book references')
    for ref in refs:
        if ref.relative_to(root).as_posix() not in core:
            errors.append('Unrouted reference: ' + ref.name)
    companion = (root / 'liu-zhongjing-confusion-patterns.md').read_text()
    rows = [int(n) for n in re.findall(r'^\|\s*(\d+)\s*\|', companion, re.M)]
    if rows != list(range(1, 46)):
        errors.append('Experience rows must retain stable ordered IDs 1–45')
    if "Compiled from experience by: Ariel Lee" not in companion:
        errors.append('Missing experience authorship')
    checked = []
    for path in root.rglob('*.md'):
        if '.git' in path.parts or '.agents' in path.parts:
            continue
        # Check explicit local Markdown targets, not code paths or external URLs.
        text = re.sub(r'```.*?```', '', path.read_text(), flags=re.S)
        for target in re.findall(r'\]\(([^)]+)\)', text):
            if target.startswith(('http:', 'https:', 'mailto:', '#')):
                continue
            target = target.split('#', 1)[0]
            if target and not (path.parent / target).exists():
                errors.append(f'{path.relative_to(root)}: broken link {target}')
        checked.append(path.relative_to(root).as_posix())
    runtime = [root/'SKILL.md', *refs, root/'liu-zhongjing-confusion-patterns.md']
    report = {'errors': errors, 'checked_markdown_files': sorted(checked),
              'experience_rows': len(rows), 'discovery': str(alias.relative_to(root)),
              'runtime_sha256': {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest() for p in runtime},
              'upstream_status': 'not_run', 'scans': {}, 'behavioral_acceptance': 'unrun'}
    if book_tools:
        cmd = [sys.executable, str(book_tools/'tools/validate_library.py'), str(root), '--layout', 'published-repo', '--json']
        proc = subprocess.run(cmd, text=True, capture_output=True)
        try:
            raw = json.loads(proc.stdout)
        except (ValueError, TypeError):
            errors.append('Upstream validator did not produce valid JSON: ' + proc.stderr)
            return report
        report['validator_sha256'] = hashlib.sha256((book_tools/'tools/validate_library.py').read_bytes()).hexdigest()
        report['upstream_raw'] = raw
        report['upstream_exit_code'] = proc.returncode
        allowed_error = '.github/ — the only subdirectory the generated skill may have is references/ (no chapters/, no per-book folders)'
        allowed_warnings = {name + ' — unexpected file at the skill root; the contract is SKILL.md plus a references/ directory'
                            for name in ('CHANGELOG.md', 'NOTICE.md', 'liu-zhongjing-confusion-patterns.md')}
        deviations = []
        for issue in raw.get('errors', []):
            if issue == allowed_error:
                deviations.append(issue)
            else:
                errors.append('Upstream: ' + issue)
        for issue in raw.get('warnings', []):
            if issue in allowed_warnings:
                deviations.append(issue)
            else:
                errors.append('Unresolved upstream warning: ' + issue)
        report['accepted_existing_architecture_deviations'] = deviations
        report['upstream_status'] = 'existing_architecture_exceptions' if deviations else 'pass'
        if proc.returncode and not raw.get('errors'):
            errors.append('Unexplained upstream nonzero exit')
        for key, path in [('core', root/'SKILL.md'), ('references', root/'references'), ('experience', root/'liu-zhongjing-confusion-patterns.md')]:
            scan = subprocess.run([sys.executable, str(book_tools/'tools/scan_generated_skill.py'), str(path), '--json', '--strict'], text=True, capture_output=True)
            try:
                report['scans'][key] = json.loads(scan.stdout)
            except ValueError:
                errors.append('Invalid scan output for ' + key)
            if scan.returncode:
                errors.append('Instruction scan failed for ' + key)
    return report


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--book-tools', type=Path)
    args = ap.parse_args()
    result = check(Path(__file__).resolve().parents[1], args.book_tools)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(bool(result['errors']))
