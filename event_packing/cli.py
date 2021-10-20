#!/usr/bin/env python3

"""
Event Packing

Example usage:
    poetry run event-packing version

"""
import json

import click
import dotenv

from event_packing.booking import book_meetings


@click.group()
def cli() -> None:
    """Run cli commands"""
    dotenv.load_dotenv()


@cli.command()
def version() -> None:
    """Get the cli version."""
    click.echo(click.style("0.1.0", bold=True))


@cli.command()
@click.argument("meetings_spec", type=str, required=True)
def book(meetings_spec: str) -> None:
    """Book non-conflicting meetings with maximimum total attendees"""
    meetings_list = json.loads(meetings_spec)

    if not isinstance(meetings_list, list):
        raise Exception("Meetings spec must be a list of lists")

    if not isinstance(meetings_list[0], list):
        raise Exception("Meetings spec must be a list of lists")

    meetings, attendees = book_meetings(meetings_list)
    meetings_result = json.dumps(meetings, separators=(",", ":"))
    print(f"`{meetings_result}` which has `{len(attendees)}` attendees")


if __name__ == "__main__":
    cli()
