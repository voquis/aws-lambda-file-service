"""
File service unit tests
"""

from file_service import __version__
from file_service import example


def test_version():
    """
    Test package version
    """
    assert __version__ == '0.1.0'


def test_example_function():
    """
    Test example function
    """
    assert example.example_function('a') == 'a'
