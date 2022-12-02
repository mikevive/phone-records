"""
Call repository.

Repository that handles call records persistace with a csv file on the database
folder.
"""
import csv
from datetime import datetime
from typing import List

from src.phone_records.application.projections.call import CallDto
from src.phone_records.infrastructure.call_repository import CallRepository


class DefaultCallRepository(CallRepository):
    """Repository that handles call records persistance."""

    def get_all(self) -> List[CallDto]:
        """Get all the call records and return its result as a CallDto List."""
        calls: List[CallDto] = []
        with open("src/database/calls.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                emitter: str = row[0]
                receiver: str = row[1]
                emition_date: datetime = datetime.strptime(row[2], "%d-%m-%Y %H:%M:%S")
                duration: int = int(row[3])
                call = CallDto(emitter, receiver, emition_date, duration)
                calls.append(call)
        return calls

    def get_first(self) -> CallDto:
        """Get the first call record and return its result as a CallDto."""
        calls = self.get_all()
        calls.reverse()
        firstCall = calls.pop()
        return firstCall

    def get_last(self) -> CallDto:
        """Get the last call record and return its result as a CallDto."""
        calls = self.get_all()
        lastCall = calls.pop()
        return lastCall
