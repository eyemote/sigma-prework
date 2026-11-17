import datetime

date_now = datetime.datetime.now()
day = int(input("Enter your day of birth: "))
month = int(input("Enter your month of birth (numerical): "))
year = int(input("Enter your year of birth: "))
dob = datetime.datetime(year, month, day)
age = date_now - dob
age_seconds = age.total_seconds()
age_years = int(divmod(age_seconds, 31536000)[0])
print(f"You are {age_years} years old.")
