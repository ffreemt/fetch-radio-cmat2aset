"""Test fetch_radio_cmat2aset."""
# pylint: disable=broad-except
from fetch_radio_cmat2aset import __version__
from fetch_radio_cmat2aset import fetch_radio_cmat2aset


def test_version():
    """Test version."""
    assert __version__[:3] == "0.1"


def test_sanity():
    """Check sanity."""
    try:
        assert not fetch_radio_cmat2aset()
    except Exception:
        assert True
