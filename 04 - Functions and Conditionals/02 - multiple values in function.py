def convert_to_hours(minutes, seconds):
	hours = minutes / 60 + seconds /3600
	return hours
print(convert_to_hours(180,4200))