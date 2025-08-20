from unittest.mock import patch

import pytest
from click.testing import CliRunner

from src.main import gamebrain


@pytest.fixture(name="fake_session_get")
def _fake_session():
    with patch("requests.Session.request") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.headers.return_value = {
            "X-API-Quota-Request": 1.0,
            "X-API-Quota-Used": 1.0,
            "X-API-Quota-Left": 49.0,
        }
        yield mock_get


# pylint: disable=unused-argument
def test_game_detail(fake_session_get):
    runner = CliRunner()
    fake_session_get.return_value.json.return_value = {
        "id": 2,
        "name": "Kingdom Come: Deliverance II",
    }
    actual = runner.invoke(gamebrain, ["game-detail", "2"], standalone_mode=False)
    expected = "Kingdom Come: Deliverance II"
    assert actual.exit_code == 0
    assert actual.return_value == expected


def test_search(fake_session_get):
    runner = CliRunner()
    fake_session_get.return_value.json.return_value = {
        "query": "bloodborne",
        "results": [
            {
                "id": 1,
                "name": "BloodBorne",
                "year": 2015,
                "platforms": [{"value": "playstation_4", "name": "Playstation 4"}],
                "short_description": "Grant us eyes...",
            }
        ],
    }
    actual = runner.invoke(gamebrain, ["search", "bloodborne"], standalone_mode=False)
    assert actual.return_value["query"] == "bloodborne"
    assert actual.return_value["results"][0]["year"] == 2015


def test_suggest(fake_session_get):
    runner = CliRunner()
    fake_session_get.return_value.json.return_value = {
        "results": [
            {
                "id": 1,
                "name": "BloodBorne",
                "year": 2015,
                "rating": {
                    "mean": 1.0,
                    "count": 999999,
                },
                "adult_only": True,
            }
        ],
    }
    actual = runner.invoke(gamebrain, ["suggest", "bloodbo"], standalone_mode=False)
    assert actual.return_value[0]["adult_only"] is True
    assert actual.return_value[0]["name"] == "BloodBorne"


def test_similar(fake_session_get):
    runner = CliRunner()
    fake_session_get.return_value.json.return_value = {
        "results": [
            {
                "id": 1,
                "name": "BloodBorne",
                "year": 2015,
                "genre": "Souls-like",
                "rating": {
                    "mean": 1.0,
                    "count": 999999,
                },
                "adult_only": True,
                "short_description": "Grant us eyes...",
            }
        ],
    }
    actual = runner.invoke(gamebrain, ["similar", "1"], standalone_mode=False)
    assert actual.return_value[0]["adult_only"] is True
    assert actual.return_value[0]["name"] == "BloodBorne"
    assert actual.return_value[0]["genre"] == "Souls-like"
