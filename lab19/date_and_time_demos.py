import datetime
# --------------------------------- Example 1 -------------------------------- #
# now = datetime.datetime.now()
# print(type(now))
# print(f'Current Date and Time: {now}')

# print(f'current hour: {now.hour}')
# print(f'{now.day}.{now.month}.{now.year}')

# --------------------------------- Example 2 -------------------------------- #
# date = datetime.date(year=2000, month=12, day=31)
# print(date)

# ---------------------------- Example: strftime() --------------------------- #
# now = datetime.datetime.now()

# # format now as 'DD.MM.YYYY, HH:MM'
# now_formated = now.strftime('%d.%m.%Y, %H:%M:%S')

# print(f'Default formated: {now}')
# print(f'Custom format: {now_formated}')

# ----------------- TASK: print the current locale month name ---------------- #
# Hint: use '%B' format string

# now = datetime.datetime.now()
# month_name = now.strftime('%B')
# # print(month_name)

# print( now.strftime('%x %X'))

# ---------------------------------- TASK 2: --------------------------------- #
# Ask the user to enter a birthdate ('DD.MM.YYYY'):
# Print the user birth year

# user_bd_str = input('Enter your birthdate ["DD.MM.YYYY"]:')
# user_bd = datetime.datetime.strptime(user_bd_str, '%d.%m.%Y')
# print(user_bd)

# ---------------------------- Example 1: timedelta ---------------------------- #
# now = datetime.datetime.now()
# date_1_week_after = now + datetime.timedelta(weeks=1)
# print(date_1_week_after)

# --------------------------- Example 2: timedelta --------------------------- #
# now = datetime.datetime.now()
# new_year_dt = datetime.datetime(year=2023, month=12, day=31)

# print(new_year_dt - now)

# ----------------------------------- TASK: ---------------------------------- #
# Print the weekday name of the 50th day of current year (2023):
# 01.01.2023 + 50 days = 20.02.2023

# now = datetime.datetime.now()
# start_date = datetime.datetime(year=2023, month=1,day=1)
# print(start_date)
# date_after_50_days = start_date + datetime.timedelta(days=50)
# print(date_after_50_days)


# ----------------------------- Example: dateutil ---------------------------- #
# from datetime import datetime
# from dateutil.relativedelta import relativedelta

# # User's birthdate
# user_birthdate = datetime(year=2000, month=1, day=31)

# # Current date
# current_date = datetime.now()

# # Calculate the age difference in years, days, and minutes
# age_difference = relativedelta(current_date, user_birthdate)
# print(age_difference)

# --------------------------- Example: pytz module --------------------------- #
# import pytz

# now = datetime.datetime.now()
# # Get the timezone object for New York and London
# now_NY = datetime.datetime.now(pytz.timezone('America/New_York'))
# now_London = datetime.datetime.now(pytz.timezone('Europe/London'))


# print(now_NY.strftime('%Y-%m-%d')) 		# 2023-10-17
# print(now_London.strftime('%Y/%m/%d'))	# 2023/10/17
# print(now.strftime('%d.%m.%Y'))			# 17.10.2023

# ------------------------ Get weekday name for today ------------------------ #
# now = datetime.datetime.now()
# print(now.strftime('%A'))

# print(datetime.datetime.now().weekday())

# import datetime

# def get_weekday_name(date, lang):
#   named_wd = {
#     'bg':["понеделник", "вторник", "сряда", "четвъртък", "петък", "събота", "неделя"],
#     'en':["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#   }

#   wd_name = named_wd[lang][date.weekday()]
#   return wd_name

# now = datetime.datetime.now()

# print('Днес е ', get_weekday_name(now, "bg"))
# print('Today is', get_weekday_name(now, "en"))



# -------------- When will new year be on given weekday name? ------------- #
# def get_dates_for_given_weekday(weekday, start_year, end_year):
# 	dates_for_given_weekday = []

# 	for year in range(start_year,end_year+1):
# 		# create datetime object from new_year date for each year
# 		new_year = datetime.datetime(year=year,month=12,day=31)
# 		# TODO: new_year_weekday =
# 		if new_year_weekday == weekday:
# 			dates_for_given_weekday.append(new_year)

# 		# print(new_year.strftime('%A'))



# 	return dates_for_given_weekday


# named_wd = {
#     'bg':["понеделник", "вторник", "сряда", "четвъртък", "петък", "събота", "неделя"],
#     'en':["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# }

# dates_for_given_weekday = get_dates_for_given_weekday('събота', start_year=2022, end_year=2025)

# --------------------------- Example: time module --------------------------- #
# import time

# print(time.time())
# print(time.time())
# print(time.time())
# print(time.time())





