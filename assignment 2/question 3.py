#ONKUNDI EUNICE NYABOKE
#SCT211-0544/2022
# take user weight and height
weight = float (input ('Enter your weight in kilogrammes '))
height = float(input ('Enter your height in metres '))
#BMI formula
BMI=weight/(height **2)

#print height, weight, BMI
print('Your weight is: ', weight,'kilogrammes')
print('Your height is: ', height,'metres')
print('Your BMI is: ',BMI)

if BMI<=18.5:

    print('underweight')

elif 18.5<=BMI<=24.9:

    print('normal')


else:

    print('overweight')

