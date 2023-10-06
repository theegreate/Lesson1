#ONKUNDI EUNICE NYABOKE
#SCT211-0544/2022
#user input year,month,date of birth
year = int(input('Enter year of birth'))
month = int(input ('Enter month of birth'))
day = int(input ('Enter day of birth'))

#age in years
current_year= 2023
age=current_year-year
print('Your age is in years is:',age)

#age in months
age_in_months = age * 12
print('Your age in months is: ',age_in_months)

#age in days
age_in_days = (age_in_months*30)
print('Your age in days is approximately: ',age_in_days)