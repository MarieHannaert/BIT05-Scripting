#!/usr/bin/python3
import datetime

import locale
date_EN=datetime.datetime.now()
print(date_EN.strftime("%B"))
print(date_EN.strftime("%U"))
print(date_EN.strftime("%j"))
print(date_EN.strftime("%d"))
print(date_EN.strftime("%A"))

delta=datetime.timedelta(weeks=1)
delta2=datetime.timedelta(days=-5)
print((date_EN+delta).strftime("%Y/%M/%d"))
print((date_EN+delta2).strftime("%Y/%M/%d"))


locale.setlocale(locale.LC_TIME, "nl_NL")
print(date_EN.strftime("%a, %d %b %Y %H:%M:%S"))





