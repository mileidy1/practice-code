#Allow the user to also enter the units. Then depending on the units, convert the distance into meters. The units we'll allow are feet, miles, meters, and kilometers.
import random

distance = input('What is the distance? ')
#distance asked 
units = input('what are the units? ')
#units will be used to get int out of dictionary
distance = int(distance)
#converting the string input into int to be able to do calculation
num_converter ={
    'ft' : 0.3048,
    'mi' : 1609.34,
    'm'  :  1,
    'km' : 1000
}

print(f"The conversion for {distance}{units} into meters is {distance * num_converter[units]}m.")
#distance *num_converter[units] = plain text(12 * 0.3048 =  3.65760000000004(example))

#left off with trying to create a number converter.
# code needs to have the ability to convert for larger numbers (can not be a string#
#need to figure out how to get 2 thing out  dictionary
#concatinate the input, and add int values then return to a string for a print?