import os
from unittest.mock import patch

import pytest
from dotenv import load_dotenv


@pytest.fixture(name="fake_api_key", scope="session")
def _fake_key():
    load_dotenv()
    with patch.dict(
        os.environ, {"GAMEBRAIN_API_KEY": "fake_key"}, clear=True
    ) as mock_key:
        yield mock_key.get("GAMEBRAIN_API_KEY")
