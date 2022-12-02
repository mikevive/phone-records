"""
Record service abstract class.

Abstract class used as base for implementing services that manage records.
"""
from abc import ABC, abstractmethod

from src.phone_records.application.projections.record import RecordDto


class RecordService(ABC):
    """Service in charge of manage records."""

    @abstractmethod
    def get_first(self) -> RecordDto:
        """Get the first emited record and return its result as a RecordDto."""
        pass

    @abstractmethod
    def get_last(self) -> RecordDto:
        """Get the last emited record and return its result as a RecordDto."""
        pass
