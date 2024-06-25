import random

distance = input('What is the distance? ')
#distance asked 
units = input('what are the units in abbreviated form? ')
#units will be used to get int out of dictionary
distance = int(distance)
#converting the string input into int to be able to do calculation
num_converter ={
    'ft' : 0.3048,
    'mi' : 1609.34,
    'm'  :  1,
    'km' : 1000,
    'yd' : 0.9144,
    'inch' : 0.0254
}

print(f"The conversion for {distance}{units} into meters is {distance * num_converter[units]}m.")
#distance *num_converter[units] = plain text(12 * 0.3048 =  3.65760000000004(example))

