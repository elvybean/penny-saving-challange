import datetime

today = datetime.date.today()
someday = datetime.date(2028, 12, 25)
diff = someday - today
print(diff.days)