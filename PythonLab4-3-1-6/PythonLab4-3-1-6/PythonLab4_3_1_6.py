#4.3.1.6 LAB: A leap year: writing your own functions

# Defines the 'is_year_leap' function
def is_year_leap(year):
	# if the year number isn't divisible by four, it's a common year;
	if year % 4:
		return False
	# if the year number isn't divisible by 100, it's a leap year;
	elif year % 100:
		return True
	# if the year number isn't divisible by 400, it's a common year;
	elif year % 400:
		return False
	# Otherwise, it's a leap year.
	else:
		return True

# "Short testing code"
test_data = [1900, 2000, 2016, 1987, 1985]		# The 5th element added, 1985 should be False, but has 
test_results = [False, True, True, False, True]	# been incorrectly entered to examine the testing code.
for i in range(len(test_data)):
	year = test_data[i]
	print(year,"-> ",end="")
	result = is_year_leap(year)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
