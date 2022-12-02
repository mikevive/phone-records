"""
Call repository abstract class.

Abstract class used as base for implementing repositories that handles call
records persistance.
"""

from abc import ABC, abstractmethod

from src.phone_records.application.projections.call import CallDto


class CallRepository(ABC):
    """Repository that handles call records persistance."""

    @abstractmethod
    def get_first(self) -> CallDto:
        """Get the first call record and return its result as a CallDto."""
        pass

    @abstractmethod
    def get_last(self) -> CallDto:
        """Get the last call record and return its result as a CallDto."""
        pass
