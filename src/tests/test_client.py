from unittest.mock import MagicMock

import requests
import pytest

from src.client import GamebrainClient


@pytest.fixture(name="fake_session")
def _fake_session(fake_api_key):
    mock_session = MagicMock(spec=requests.Session)
    mock_session.headers = {"x-api-key": fake_api_key}
    return mock_session


def test_client(fake_session):
    client = GamebrainClient("https://foo.com", fake_session)
    assert client.base_url == "https://foo.com"
    assert client.session.headers == {"x-api-key": "fake_key"}
