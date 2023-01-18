import unittest
import os
import subprocess


HERE = os.path.dirname(__file__)

class Tester(unittest.TestCase):
    def test_ok(self):
        """This test passes on windows, linux and macos"""
        with open(os.path.join(HERE, "in.txt"), encoding="utf-8") as stream:
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
