from selene import by, be, have
from selene.support.shared import browser
from selene_intro import __version__


def test_version():
    assert __version__ == '0.1.0'
