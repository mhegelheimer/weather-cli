import click
from .helpers import print_lines
from .weather import get_weather, parse_response


@click.command()
@click.argument("city")
def main(city):
    response = get_weather(city)
    if response.status_code == 401:
        raise Exception("Invalid API Key")
    print_lines(parse_response(response.json()))
