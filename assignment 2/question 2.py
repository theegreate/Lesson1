#ONKUNDI EUNICE NYABOKE
#SCT211-0544/2022
bill = float(input('Enter total Bill amount: '))
tip_choice = int(input('Enter tip choice (1 for 10%, 2 for 12%, 3 for 13%): '))

# Check the tip choice and calculate tip percentage
if tip_choice == 1:
    tip_percent = 0.10
    print('10% tip selected')
elif tip_choice == 2:
    tip_percent = 0.12
    print('12% tip selected')
elif tip_choice == 3:
    tip_percent = 0.13
    print('13% tip selected')
else:
    print('Invalid tip choice')
    exit()

people = int(input('Enter the number of people splitting the bill: '))

# Calculate the total bill including tip
total = (1 + tip_percent) * bill

# Calculate the amount per person
per_person_total = total / people

print('Your total bill is:', total)
print('Each person should pay:', per_person_total)
