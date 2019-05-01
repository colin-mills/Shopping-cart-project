from app.functions import to_USD, human_friendly_timestamp
import datetime

def test_to_USD():
    first = to_USD(4)
    second = to_USD(57.9999)
    third = to_USD(99999.99)
    fourth = to_USD(100000)
    fifth = to_USD(8.00000000001)
   
    assert first == "($4.00)"
    assert second == "($58.00)"
    assert third == "($99,999.99)"
    assert fourth == "($100,000.00)"
    assert fifth == "($8.00)"

def test_human_friendly_timestamp():
    t = datetime.datetime.now()
    stdTime = t.strftime("%Y-%m-%d  %H:%M:%S")
    time = human_friendly_timestamp(t)

    assert time == stdTime

    t = datetime.datetime.today()
    stdTime = t.strftime("%Y-%m-%d  %H:%M:%S")
    time = human_friendly_timestamp(t)

    assert time == stdTime

