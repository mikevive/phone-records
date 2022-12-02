"""
Call service.

Service in charge of manage call records.
"""
from injector import inject

from src.phone_records.application.services.call_service import CallService
from src.phone_records.application.projections.call import CallDto
from src.phone_records.infrastructure.call_repository import CallRepository


class DefaultCallService(CallService):
    """Service in charge of manage call records."""

    @inject
    def __init__(self, call_repository: CallRepository) -> None:
        """Contruct a Default Call Service.

        :param call_repository: Repository that handle calls persistance.
        :type call_repository: CallRepository
        """
        self._call_repository: CallRepository = call_repository

    def get_first(self) -> CallDto:
        """Get the first emited call records and return its result as a CallDto."""
        first_call_dto = self._call_repository.get_first()
        return first_call_dto

    def get_last(self) -> CallDto:
        """Get the last emited call records and return its result as a CallDto."""
        raise Exception("Not implemented yet")
