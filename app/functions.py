#Funcitons for code simplification
import datetime

def to_USD(Number):
    Number = "(${0:,.2f})".format(Number)
    return Number

def human_friendly_timestamp(datetime):
    stdTime = datetime.strftime("%Y-%m-%d  %H:%M:%S")
    return stdTime