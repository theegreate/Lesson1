#ONKUNDI EUNICE NYABOKE
#SCT211-0544/2022
#take user input for year
year = int(input('Enter any year'))
modulus = year % 4
if modulus == 0:
    print('This is a leap year')
 
else:
    print ('This is a lean year')