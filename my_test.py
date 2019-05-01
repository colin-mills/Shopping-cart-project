from app.functions import to_USD, human_friendly_timestamp, find_product
import datetime

def test_to_USD():
    assert to_USD(4) == "($4.00)" #should have two decimal points
    assert to_USD(57.9999) == "($58.00)" #test rounding 
    assert to_USD(99999.99) == "($99,999.99)" #test commas 
    assert to_USD(100000) == "($100,000.00)" #test commas and decimals 
    assert to_USD(8.00000000001) == "($8.00)" #Should round down

def test_human_friendly_timestamp():
    t = datetime.datetime.now()
    stdTime = t.strftime("%Y-%m-%d  %H:%M:%S")
    time = human_friendly_timestamp(t)

    assert time == stdTime #should work the same as the function

    t = datetime.datetime.today()
    stdTime = t.strftime("%Y-%m-%d  %H:%M:%S")
    time = human_friendly_timestamp(t)

    assert time == stdTime #should work the same as now

def test_find_product():
    product = find_product(1) #testing ints
    assert product[0]["id"] == 1
    assert product[0]["price"] == 3.5

    product = find_product("10") #testing strings
    assert product[0]["id"] == 10
    assert len(product) == 1
    assert product[0]["department"] == "beverages"

    product = find_product(0) #non existent should be empty
    assert len(product) == 0

    product = find_product(1.5) #Should return empty for doubles
    assert len(product) == 0

    product = find_product("1.5") #Should return empty for strings that are not ints but are within range of product IDs
    assert len(product) == 0