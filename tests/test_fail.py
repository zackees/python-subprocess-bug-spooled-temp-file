# flake8: noqa: E501

import unittest
import os
from pathlib import Path
from tempfile import SpooledTemporaryFile
import subprocess


HERE = Path(os.path.dirname(__file__))

def to_stream(input: str) -> SpooledTemporaryFile:
    stream = SpooledTemporaryFile()
    stream.write(input.encode("utf-8"))
    return stream


class Tester(unittest.TestCase):

    def test_fail(self):
        """This test passes on windows and linux but fails on macos"""
        p = subprocess.Popen(
            "python accept_input.py",
            cwd=HERE,
            shell=True,
            stdin=to_stream("y\n"),
            stdout=subprocess.PIPE,
            universal_newlines=True
        )
        p.wait()
        stdout = p.stdout.read()
        self.assertIn("OK", stdout)


if __name__ == "__main__":
    unittest.main()
