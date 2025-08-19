import os
import urllib.parse

from dotenv import load_dotenv
from requests import Session
from requests.adapters import HTTPAdapter
from requests.exceptions import HTTPError
from urllib3.util import Retry


load_dotenv()
API_KEY = os.environ.get("GAMEBRAIN_API_KEY")

retry_strategy = Retry(
    total=3,
    backoff_factor=0.1,
    status_forcelist=[502, 503, 504],
    allowed_methods={"GET"},
)


class GamebrainClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = Session()
        self._bootstrap_session()

    def _bootstrap_session(self):
        self.session.headers["x-api-key"] = API_KEY

        self.session.mount("https://", HTTPAdapter(max_retries=retry_strategy))
        self.session.mount("http://", HTTPAdapter(max_retries=retry_strategy))

    def build_url(self, endpoint: str):
        return urllib.parse.urljoin(self.base_url, endpoint)

    def call_api(self, params: dict):
        
        try:
            resp = self.session.request("GET", "", params=params)
        except HTTPError as exc:
            print(exc)
            raise exc
        
        return resp
