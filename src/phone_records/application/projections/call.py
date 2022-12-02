"""
Call DTO.

Basic representation of a call.
"""
from datetime import datetime

from src.phone_records.application.projections.record import RecordDto


class CallDto(RecordDto):
    """Call Dto.

    Basic representation of a call record.
    """

    def __init__(
        self, emitter: str, receiver: str, emition_date: datetime, duration: int
    ) -> None:
        """Construct a representation of a call record.

        :param emitter: Emitter Phone number
        :type emitter: str
        :param receiver: Receiver Phone number
        :type receiver: str
        :param emition_date: Emition date
        :type emition_date: datetime
        :param duration: Call duration in milliseconds
        :type duration: int
        """
        """ TODO: add defensive programming """
        super().__init__(emitter, receiver, emition_date)
        self._duration: int = duration

    def get_duration(self) -> int:
        """Get call duration.

        :return: call duration in milliseconds
        :rtype: int
        """
        return self._duration
