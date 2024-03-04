import subprocess
import sys

from testing04_mar import __version__


def test_cli_version():
    cmd = [sys.executable, "-m", "testing04_mar", "--version"]
    assert subprocess.check_output(cmd).decode().strip() == __version__
