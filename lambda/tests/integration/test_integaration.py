"""
File service integration tests
"""

from file_service import __version__

def test_version():
    """
    Test package version
    """
    assert __version__ == '0.1.0'
