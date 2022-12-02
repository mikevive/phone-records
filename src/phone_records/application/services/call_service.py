"""
Call service abstract class.

Abstract class used as base for implementing services that manage call records.
"""
from abc import ABC, abstractmethod

from src.phone_records.application.projections.call import CallDto


class CallService(ABC):
    """Service in charge of manage call records."""

    @abstractmethod
    def get_first(self) -> CallDto:
        """Get the first emited call record and return its result as a CallDto."""
        pass

    @abstractmethod
    def get_last(self) -> CallDto:
        """Get the last emited call record and return its result as a CallDto."""
        pass
