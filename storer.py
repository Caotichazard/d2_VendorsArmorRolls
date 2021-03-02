
from datetime import date
from datetime import timedelta
import json
MON, TUE, WED, THU, FRI, SAT, SUN = range(7)

def lastTday(adate, w):
    """Mon:w=0, Sun:w=6"""
    if adate.weekday() == w:
        return adate
    else:
        delta = (adate.weekday() + 6 - w) % 7 + 1
        return adate - timedelta(days=delta)

def nextTday(adate, w):
    """Mon:w=0, Sun:w=6"""
    delta = (adate.weekday() + 6 - w) % 7 + 1
    return adate + timedelta(days=delta)


def get_file_name():
    week_beg = lastTday(date.today(),TUE).strftime("%Y-%m-%d")
    week_end = nextTday(date.today(),TUE).strftime("%Y-%m-%d")

    return week_beg + " - " + week_end
print(get_file_name())

def store_info(info):
    file_name = get_file_name()
    with open("weeks/"+file_name+".json", "w") as file:
        file.write(json.dumps(info, indent=2))