import pytest
from datetime import datetime
from src.phone_records.application.projections.call import Call

call: Call = Call(
    "1234567890",
    "0987654321",
    datetime.strptime("01-01-2020 10:10:10", "%d-%m-%Y %H:%M:%S"),
    1000,
)


def test_create_call():
    call: Call = Call(
        "1234567890",
        "0987654321",
        datetime.strptime("01-01-2020 10:10:10", "%d-%m-%Y %H:%M:%S"),
        1000,
    )

    assert isinstance(call, Call)


def test_create_call_with_wrong_incoming_number():
    with pytest.raises(ValueError):
        Call(
            1234567890,
            "0987654321",
            datetime.strptime("01-01-2020 10:10:10", "%d-%m-%Y %H:%M:%S"),
            1000,
        )


def test_create_call_with_wrong_answering_number():
    with pytest.raises(ValueError):
        Call(
            "1234567890",
            1234567890,
            datetime.strptime("01-01-2020 10:10:10", "%d-%m-%Y %H:%M:%S"),
            1000,
        )


def test_create_call_with_wrong_date():
    with pytest.raises(ValueError):
        Call("1234567890", "0987654321", "01-01-2020 10:10:10", 1000)


def test_create_call_with_wrong_duration():
    with pytest.raises(ValueError):
        Call(
            "1234567890",
            "0987654321",
            datetime.strptime("01-01-2020 10:10:10", "%d-%m-%Y %H:%M:%S"),
            "1000",
        )


def test_get_incoming_number():
    expected = "1234567890"
    actual = call.get_incoming_number()
    assert expected == actual


def test_get_answering_number():
    expected = "0987654321"
    actual = call.get_answering_number()
    assert expected == actual


def test_get_date():
    expected = "2020-01-01 10:10:10"
    actual = call.get_date()
    assert expected == str(actual)


def test_get_duration():
    expected = 1000
    actual = call.get_duration()
    assert expected == actual


def test_get_str():
    expected = (
        "1234567890 calls 0987654321 at time 2020-01-01 10:10:10, lasting 1000 seconds"
    )
    actual = call.__str__()
    print(actual)
    assert expected == actual
