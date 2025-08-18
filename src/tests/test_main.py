from unittest.mock import patch

import pytest
from click.testing import CliRunner

from src.main import gamebrain


@pytest.fixture(name="fake_response")
def _mock_api_response():
    with patch("requests.get") as mock_get:
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
def test_dummy(fake_response):
    runner = CliRunner()
    dummy = runner.invoke(gamebrain, ["game-detail", "1273796"], standalone_mode=False)
    expected = "Kingdom Come: Deliverance II"
    assert dummy.exit_code == 0
    assert dummy.return_value == expected
