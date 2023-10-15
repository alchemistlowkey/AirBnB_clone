#!/usr/bin/python3
"""
Test for console
"""

import inspect
import io
import pep8
import sys
import unittest
from console import HBNBCommand
from contextlib import redirect_stdout


class TestHBNBCommand(unittest.TestCase):
    """
    Test cases for testing HBNBCommand class
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class for the doc tests
        """
        cls.setup = inspect.getmembers(HBNBCommand, inspect.isfunction)

    def test_pep8_conformance_HBNBCommand(self):
        """
        Test that console.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["console.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_HBNBCommand(self):
        """
        Test that test_console.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Test if module docstring documentation exist
        """
        self.assertTrue(len(HBNBCommand.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(HBNBCommand.__doc__) >= 1)


if __name__ == "__main__":
    unittest.main()
