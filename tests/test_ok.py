# flake8: noqa: E501

import unittest
import os
from pathlib import Path
from tempfile import SpooledTemporaryFile
import subprocess


HERE = Path(os.path.dirname(__file__))

class Tester(unittest.TestCase):
    def test_ok(self):
        """This test passes on windows, linux and macos"""
        from tempfile import TemporaryFile
        with TemporaryFile(HERE / "in4.txt") as stream:
            p = subprocess.Popen(
                "python accept_input.py",
                cwd=HERE,
                shell=True,
                stdin=stream,
                stdout=subprocess.PIPE,
                universal_newlines=True
            )
            p.wait()
            stdout = p.stdout.read()
            self.assertIn("OK", stdout)

if __name__ == "__main__":
    unittest.main()
