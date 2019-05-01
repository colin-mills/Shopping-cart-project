from app.functions import to_USD, human_friendly_timestamp
import datetime

def test_to_USD():
    result = to_USD(4)
    assert result == "($4.00)"

def test_human_friendly_timestamp():
    t = datetime.datetime.now()
    stdTime = t.strftime("%Y-%m-%d  %H:%M:%S")
    time = human_friendly_timestamp()
    assert time == stdTime

