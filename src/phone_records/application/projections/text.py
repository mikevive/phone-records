"""
Text DTO.

Basic representation of a text.
"""
from datetime import datetime

from src.phone_records.application.projections.record import RecordDto


class TextDto(RecordDto):
    """Text Dto.

    Basic representation of a text record.
    """

    def __init__(self, emitter: str, receiver: str, emition_date: datetime) -> None:
        """Construct a representation of a text record.

        :param emitter: Emitter Phone number
        :type emitter: str
        :param receiver: Receiver Phone number
        :type receiver: str
        :param emition_date: Emition date
        :type emition_date: datetime
        """
        """ TODO: add defensive programming """
        super().__init__(emitter, receiver, emition_date)
