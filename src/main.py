import logging
from pprint import pprint

import click

from src.client import init_session, GamebrainClient

logger = logging.getLogger(__name__)

BASE_URL = "https://api.gamebrain.co/v1/"


@click.group()
def gamebrain():
    click.echo("Querying Gamebrain API...")


@gamebrain.command("game-detail")
@click.argument("game-id")
def game_detail(game_id: str | int) -> dict | str:
    """
    Takes a Gamebrain game ID and runs a request to GET information on the Game
    """
    game_id = int(str(game_id))
    session = init_session()
    client = GamebrainClient(BASE_URL, session)
    url = client.build_url(f"games/{game_id}")
    resp_json = client.call_api(url)
    pprint(resp_json)
    return resp_json.get("name")


@gamebrain.command("search")
@click.argument("query")
@click.option("--platform", "-p", multiple=True)
@click.option("--review-rating", "-r")
@click.option("--release", "-d")
@click.option("--play-mode", "-m", multiple=True)
@click.option("--age-rating", "-a")
@click.option("--price", "-c")
@click.option(
    "--sorting",
    "-s",
    nargs=2,
    type=(
        click.Choice(["computed_rating", "release_date", "price"]),
        click.Choice(["asc", "desc"], case_sensitive=False),
    ),
)
def search(query: str, sorting: tuple, **filters) -> dict:
    """
    Takes a search query and gets the first 10 games returned with their metadata
    """
    session = init_session()
    client = GamebrainClient(BASE_URL, session)
    url = client.build_url("games/")
    params = {
        "query": query,
        "filters": [
            {"key": f_type, "values": [{"value": val} for val in f_value]}
            for f_type, f_value in filters.items()
            if f_value is not None
        ],
    }
    if sorting:
        sort_dict = {"sort": sorting[0], "sort-order": sorting[1]}
        params.update(sort_dict)
    resp_json = client.call_api(url, params=params)
    pprint(resp_json)
    return resp_json


@gamebrain.command("suggest")
@click.argument("query")
def suggest(query: str) -> list:
    """
    Takes and incomplete query and returns a list of similar titles
    """
    session = init_session()
    client = GamebrainClient(BASE_URL, session)
    url = client.build_url("games/suggestions")
    params = {"query": query}
    resp_json = client.call_api(url, params=params)
    results = resp_json["results"]
    pprint(results)
    return results


@gamebrain.command("similar")
@click.argument("game-id")
def similar(game_id: str) -> list:
    """
    Takes a game_id and returns 10 games considered similar to the provided ID
    """
    session = init_session()
    client = GamebrainClient(BASE_URL, session)
    url = client.build_url(f"games/{game_id}/similar")
    resp_json = client.call_api(url)
    results = resp_json["results"]
    pprint(results)
    return results


if __name__ == "__main__":
    gamebrain()
