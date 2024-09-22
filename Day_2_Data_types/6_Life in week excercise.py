# To find out how many weeks i have left in my life

age = input("What is your age ? ")
age_as_int = int(age)

years_remaining = 100-age_as_int
days_reamaning = years_remaining*365
weeks_reamaning = years_remaining*52
months_reamaning = years_remaining*12

message = f"You have {days_reamaning} days,{weeks_reamaning} weeks,{months_reamaning} months in your life"
print(message)


# ________________________________________________________

# Highlights of this session

# Project
# F-string
# mixup
# Operators
