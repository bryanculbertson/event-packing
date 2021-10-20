from click.testing import CliRunner

from event_packing.cli import book, version


def test_version() -> None:
    runner = CliRunner()
    result = runner.invoke(version)
    assert result.exit_code == 0
    assert result.output == "0.1.0\n"


def test_book() -> None:
    runner = CliRunner()
    result = runner.invoke(book, "[[0,1,2]]")
    assert result.exit_code == 0
    assert result.output == "`[[0,1,2]]` which has `3` attendees\n"
