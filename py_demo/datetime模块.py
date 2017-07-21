# -*- coding:utf-8 -*-

from datetime import datetime, timezone, timedelta
import re

def to_timestamp(dt_str, tz_str):
	dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
	tz_info = re.split(r'[UTC\:]+',tz_str)
	# print(tz_info)
	tz_hours = int(tz_info[1])
	tz_minutes = int(tz_info[2])
	dt = dt.replace(tzinfo = timezone(timedelta(hours=tz_hours, minutes=tz_minutes)))
	return dt.timestamp()

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
print(t1)