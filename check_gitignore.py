"""Fail closed if .env is tracked."""
import subprocess
import sys


def main() -> int:
    r = subprocess.run(
        ['git', 'check-ignore', '-v', '.env'],
        capture_output=True,
        text=True,
    )
    if r.returncode != 0 or not r.stdout.strip():
        print('FAIL: .env is not gitignored. Add it, then re-run.')
        return 1
    print('OK: .env ignored')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
