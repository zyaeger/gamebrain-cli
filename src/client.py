# pylint: disable=logging-not-lazy,consider-using-f-string
import logging
import os
import urllib.parse

from dotenv import load_dotenv
from requests import Session
from requests.adapters import HTTPAdapter
from requests.exceptions import HTTPError
from urllib3.util import Retry

logger = logging.getLogger(__name__)


load_dotenv()
API_KEY = os.environ.get("GAMEBRAIN_API_KEY")

retry_strategy = Retry(
    total=3,
    backoff_factor=0.1,
    status_forcelist=[502, 503, 504],
    allowed_methods={"GET"},
)


def init_session() -> Session:
    session = Session()
    session.headers["x-api-key"] = API_KEY

    session.mount("https://", HTTPAdapter(max_retries=retry_strategy))
    session.mount("http://", HTTPAdapter(max_retries=retry_strategy))

    return session


class GamebrainClient:
    def __init__(self, base_url: str, session: Session) -> None:
        self.base_url = base_url
        self.session = session

    def build_url(self, endpoint: str) -> str:
        return urllib.parse.urljoin(self.base_url, endpoint)

    def call_api(self, url: str, params: dict = None) -> dict | list:
        try:
            resp = self.session.request("GET", url=url, params=params)
        except HTTPError as exc:
            logger.exception(exc)
            raise exc

        headers = resp.headers
        logger.info("Request Token Usage: %s" % headers["X-API-Quota-Request"])
        logger.info("Today's Total Token Usage: %s" % headers["X-API-Quota-Request"])
        logger.info("Today's Remaining Tokens: %s" % headers["X-API-Quota-Request"])

        return resp.json()
