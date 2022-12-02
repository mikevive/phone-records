"""Phone registers.

Study of data structures and good programming practices conducted over a mock
collection of phone records.
"""
import logging
from injector import Injector

from src.dependencies import configure
from src.phone_records.interface.cli.default_cli import DefaultCli


def main():
    """Set up the app and start it."""
    logging.basicConfig(
        filename="phone-records.log", encoding="utf-8", level=logging.DEBUG
    )
    injector = Injector(configure)
    defaultCli = injector.get(DefaultCli)
    defaultCli.start()


if __name__ == "__main__":
    """Execute only if run as the entry point into the program."""
    main()
