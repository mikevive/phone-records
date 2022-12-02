from datetime import datetime
from src.phone_records.application.projections.call import Call
from src.phone_records.application.services.impl.task0 import DefaultTask0Service


record1 = Call(
    "1234567890",
    "0987654321",
    datetime.strptime("01-01-2020 10:10:10", "%d-%m-%Y %H:%M:%S"),
    1000,
)
record2 = Call(
    "1234567891",
    "0987654322",
    datetime.strptime("01-01-2020 10:10:20", "%d-%m-%Y %H:%M:%S"),
    2000,
)
record3 = Call(
    "1234567892",
    "0987654323",
    datetime.strptime("01-01-2020 10:10:30", "%d-%m-%Y %H:%M:%S"),
    3000,
)

records = [record1, record2, record3]


def test_get_first_record():

    expected = record1

    actual = DefaultTask0Service.get_first_record(records)

    assert expected == actual, "Assert Error: testget_first_record"


def test_get_last_recordtestget_last_record():

    expected = record3

    actual = DefaultTask0Service.get_last_record(records)

    assert expected == actual, "Assert Error: testget_last_record"
