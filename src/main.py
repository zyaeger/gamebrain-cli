# pylint: disable=fixme
import os
from pprint import pprint

import click
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get("GAMEBRAIN_API_KEY")
BASE_URL = "https://api.gamebrain.co/v1"


@click.group()
def gamebrain():
    pass


@gamebrain.command("game-detail")
@click.argument("game-id")
def game_detail(game_id: str) -> dict | str:
    """
    Takes a Gamebrain game ID and runs a request to GET information on the Game
    """
    game_id = int(str(game_id))
    url = os.path.join(BASE_URL, f"games/{game_id}")
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


@gamebrain.command("search")
@click.argument("query")
# Add options fo filter and sort
def search(query: str) -> list:
    """
    Takes a search query and gets the first 10 games returned with their metadata
    """
    url = os.path.join(BASE_URL, "games")
    # Add pagination and filters
    click.echo(f"Querying {url} for {query}")
    return list[query]


@gamebrain.command("suggest")
@click.argument("query")
def suggest(query: str) -> list:
    """
    Takes and incomplete query and returns a list of similar titles
    """
    url = os.path.join(BASE_URL, "games/suggestions")
    click.echo(f"Querying {url} for {query}")
    return [query]


@gamebrain.command("similar")
@click.argument("game-id")
def similar(game_id: str) -> list:
    """
    Takes a game_id and returns 10 games considered similar to the provided ID
    """
    url = os.path.join(BASE_URL, f"games/{game_id}/similar")
    click.echo(f"Querying {url} for similar games")
    return [game_id]


if __name__ == "__main__":
    print("Querying Gamebrain API...")
