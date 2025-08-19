from unittest.mock import patch

import pytest
from click.testing import CliRunner

from src.main import gamebrain


@pytest.fixture(name="fake_session_get")
def _fake_session():
    with patch("requests.Session.request") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "id": 1,
            "name": "Kingdom Come: Deliverance II",
        }
        mock_get.return_value.headers.return_value = {
            "X-API-Quota-Request": 1.0,
            "X-API-Quota-Used": 1.0,
            "X-API-Quota-Left": 49.0,
        }
        yield mock_get


# pylint: disable=unused-argument
def test_game_detail(fake_session_get):
    runner = CliRunner()
    actual = runner.invoke(gamebrain, ["game-detail", "1"], standalone_mode=False)
    expected = "Kingdom Come: Deliverance II"
    assert actual.exit_code == 0
    assert actual.return_value == expected
