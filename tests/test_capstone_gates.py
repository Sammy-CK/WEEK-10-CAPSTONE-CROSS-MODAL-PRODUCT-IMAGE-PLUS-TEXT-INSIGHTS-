import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(script: str) -> None:
    r = subprocess.run(
        [sys.executable, script],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert r.returncode == 0, (script, r.stdout, r.stderr)


def test_gold_checks():
    run('check_mismatch.py')
    run('check_encoder_pin.py')
    run('check_insights.py')
    run('check_ethics.py')
    run('check_gen_pin_starter.py')
    run('check_outputs.py')
    run('check_gitignore.py')
    run('search.py')
