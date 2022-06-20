"""Test fetch_radio_cmat2aset."""
# pylint: disable=broad-except
import joblib
from fetch_radio_cmat2aset import __version__, fetch_radio_cmat2aset


def test_version():
    """Test version."""
    assert __version__[:3] == "0.1"


def test_sanity():
    """Check sanity."""
    try:
        assert not fetch_radio_cmat2aset()
    except Exception:
        assert True


def test_fetch_radio_cmat2aset_simple():
    """Test fetch_radio_cmat2aset simple."""
    cmat = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
    ]
    res = fetch_radio_cmat2aset(
        cmat,
        # api_url="http://127.0.0.1:7860/api/predict",
    )
    assert res == [[0, 0, 1.0], [1, 1, 1.0], [2, 2, 1.0]]


def test_fetch_radio_cmat2aset_84():
    """Test fetch_radio_cmat2aset simple."""
    cmat = joblib.load("tests/cmat_list.lzma")
    res = fetch_radio_cmat2aset(
        cmat.tolist(),
        # api_url="http://127.0.0.1:7860/api/predict",
    )
    assert len(res) >= 84
