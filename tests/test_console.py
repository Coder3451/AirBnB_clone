#!/usr/bin/python3
"""Unittests for the console module."""
import unittest
import sys
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test case for the AirBnB command interpreter."""

    def test_quit_command(self):
        """Test quit command."""
        console = HBNBCommand()
        self.assertTrue(console.onecmd("quit"))

    def test_EOF_command(self):
        """Test EOF command."""
        console = HBNBCommand()
        # Capture output to avoid printing an extra newline
        captured_output = StringIO()
        sys.stdout = captured_output
        self.assertTrue(console.onecmd("EOF"))
        sys.stdout = sys.__stdout__

    def test_emptyline(self):
        """Test that an empty line does nothing."""
        console = HBNBCommand()
        # When empty, nothing should happen; check that it returns None
        self.assertIsNone(console.onecmd(""))


if __name__ == '__main__':
    unittest.main()
