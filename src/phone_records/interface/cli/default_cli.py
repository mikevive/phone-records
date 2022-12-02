"""
Default CLI.

Default CLI used to manage records.
"""
from typing import Callable, Dict
from injector import inject
import logging

from src.phone_records.application.projections.call import CallDto
from src.phone_records.application.services.call_service import CallService
from src.phone_records.interface.cli.exceptions import InvalidCommand


class DefaultCli:
    """Default CLI used to manage records."""

    @inject
    def __init__(self, call_service: CallService) -> None:
        """Construct a Default CLI.

        :param call_service: Services that manage call records.
        :type call_service: CallService
        """
        self._call_service: CallService = call_service
        self._is_cli_active: bool = True

    def start(self) -> None:
        """Start the CLI."""
        command_executor: Callable[[str], None] = self._get_command_executor()

        while self._is_cli_active:
            self._print_prompt()
            selected_command: str = input()
            try:
                command_executor(selected_command)
            except InvalidCommand:
                self._print_invalid_command_warning(selected_command)
            except Exception as error:
                logging.exception(error)

    def _get_command_executor(self) -> Callable[[str], None]:
        """Return a function that executes the selected command."""
        commands: Dict[str, Callable[[], None]] = {
            "1": self._get_first_call,
            "h": self._print_instructions,
            "exit": self._deactivate_cli,
        }

        def command_executor(selected_command: str) -> None:
            """Search for the selected command and execute it."""
            try:
                command: Callable[[], None] = commands[selected_command]
            except:
                raise InvalidCommand()

            command()

        return command_executor

    def _print_prompt(self) -> None:
        """Print prompt to capture the command selected by the user."""
        print("records>", end=" ")

    def _get_first_call(self) -> None:
        """Return the first call recorded."""
        first_call_dto: CallDto = self._call_service.get_first()

        print(f"Emitter: {first_call_dto.get_emitter()},", end=" ")
        print(f"Receiver: {first_call_dto.get_receiver()},", end=" ")
        print(f"Emition Date: {first_call_dto.get_emition_date()},", end=" ")
        print(f"Duration {first_call_dto.get_duration()}")

    def _print_instructions(self) -> None:
        """Print CLI instructions on console."""
        print("Phone Records CLI:")
        print("An Application to manage phone records.", end="\n\n")
        print("Commands:")
        print("1                Get first call record")
        print("help             Help")
        print("exit             Quit")

    def _deactivate_cli(self) -> None:
        """Deactivate the CLI in order to execute a safety exit."""
        self._is_cli_active = False

    def _print_invalid_command_warning(self, selected_command: str) -> None:
        """Print invalid command warning."""
        print(f"'{selected_command}' is not a valid command.")
        print("See 'h' for help.")
