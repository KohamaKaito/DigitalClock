import datetime
import math

def get_time():
	dt_now = datetime.datetime.now()
	hour = int(dt_now.hour)
	minute = int(dt_now.minute)
	
	if hour > 9:
		one = math.floor(hour/10)
		two = hour % 10
	else:
		one = 0
		two = hour

	if minute > 9:
		three = math.floor(minute/10)
		four = minute % 10
	else:
		three = 0
		four = minute
    	
	return one,two,three,four
