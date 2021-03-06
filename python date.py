import datetime #The date contains year, month, day, hour, minute, second, and microsecond.
x = datetime.datetime.now()
print(x)
print()

import datetime
date=datetime.datetime(2020,2,2)
print('today is',date)
print()

date=datetime.datetime.now()
print(date.strftime('%x'))
print()

date=datetime.datetime(2020,2,2)
print(date)
print(date.strftime('%y/%m/%d'))
print()

import datetime
x = datetime.datetime.now()
print(x.year)
print(x.day)
print(x.month)
print(x.strftime("%A"))
print()

import datetime
x = datetime.datetime(2020, 5, 17)
print(x)
print()

import datetime
x = datetime.datetime(2018, 6, 1)

x = datetime.datetime.now()
print(x)
print(x.strftime("%B"))
print(x.strftime("%b"))
print(x.strftime("%a"))
print(x.strftime("%A"))
print(x.strftime("%w")) #weekday: 0-sunday to 6-saturday
print(x.strftime("%y"))
print(x.strftime("%Y"))
print(x.strftime("%H")) #hour: 0-23
print(x.strftime("%I")) #hour: 0-12
print(x.strftime("%p"))
print(x.strftime("%M"))
print(x.strftime("%S"))
print(x.strftime("%f")) #microsecond
print(x.strftime("%z"))
print(x.strftime("%Z"))
print(x.strftime("%j"))
print(x.strftime("%U"))
print(x.strftime("%W"))
print(x.strftime("%c"))
print(x.strftime("%x"))
print(x.strftime("%X"))
print(x.strftime("%%"))
print(x.strftime("%G"))
print(x.strftime("%u"))
print(x.strftime("%W"))