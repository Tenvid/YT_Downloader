import cmd2_ext_test
import pytest
from downloader_for_yt.__main__ import DownloaderApp


class DownloaderAppTester(cmd2_ext_test.ExternalTestMixin, DownloaderApp):
    def __init__(self, *args, **kwargs):
        # gotta have this or neither the plugin or cmd2 will initialize
        super().__init__(*args, **kwargs)


@pytest.fixture
def base_app():
    app = DownloaderAppTester()
    app.fixture_setup()
    yield app
    app.fixture_teardown()


def test_url_validation(base_app):
    url = "https://youtu.be/example"
    assert base_app.validate_url(url)
