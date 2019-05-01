from app.functions import to_USD

def test_to_USD():
    result = to_USD(4)
    assert result == "($4.00)"