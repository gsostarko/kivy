import datetime


	
def TimeSpentInApp(start_time):
	#Function that takes starting time and returns seconds spent in app.
	#End time returned in seconds is rounded 
	#To use you must imorpot "datetime" module.

	endtime = None
	temp = datetime.datetime.now() - start_time
	endtime = temp.total_seconds()
	return round(endtime)


