from datetime import datetime

date_format = "%d/%m/%Y"
a = datetime.strptime('18/8/2008', date_format)
b = datetime.strptime('26/9/2008', date_format)
delta = b - a
print(delta) 