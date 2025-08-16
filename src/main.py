# pylint: disable=fixme
import os
from pprint import pprint

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get("GAMEBRAIN_API_KEY")


# TODO: Add click for cli args (search terms, IDs, Platforms)
def main():
    url = "https://api.gamebrain.co/v1/games/1273796"

    headers = {"x-api-key": API_KEY}

    try:
        response = requests.get(url, headers=headers, timeout=None)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(e)

    resp_json = response.json()
    headers = response.headers
    pprint(resp_json)
    print(f"Request Token Usage: {headers['X-API-Quota-Request']}")
    print(f"Today's Total Token Usage: {headers['X-API-Quota-Used']}")
    print(f"Today's Remaining Tokens: {headers['X-API-Quota-Left']}")
    return resp_json.get("name")


if __name__ == "__main__":
    main()
