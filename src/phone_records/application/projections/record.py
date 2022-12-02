"""
Record DTO.

Basic representation of a record.
"""
from datetime import datetime


class RecordDto:
    """Record Dto.

    Basic representation of a record.
    """

    def __init__(self, emitter: str, receiver: str, emition_date: datetime) -> None:
        """Construct a representation of a record.

        :param emitter: Emitter Phone number
        :type emitter: str
        :param receiver: Receiver Phone number
        :type receiver: str
        :param emition_date: Emition date
        :type emition_date: datetime
        """
        """ TODO: add defensive programming """
        self._emitter: str = emitter
        self._receiver: str = receiver
        self._emition_date: datetime = emition_date

    def get_emitter(self) -> str:
        """Get emitter phone number.

        :return: emitter phone number
        :rtype: str
        """
        return self._emitter

    def get_receiver(self) -> str:
        """Get receiver phone number.

        :return: receiver phone number
        :rtype: str
        """
        return self._receiver

    def get_emition_date(self) -> datetime:
        """Get emition date.

        :return: emition date
        :rtype: datetime
        """
        return self._emition_date
