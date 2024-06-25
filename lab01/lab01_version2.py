#Allow the user to also enter the units. Then depending on the units, convert the distance into meters. The units we'll allow are feet, miles, meters, and kilometers.


distance = input('What is the distance? ')

units = input('what are the units? ')

#print answer after user response not during

num_converter ={
    '1 ft' : '0.3048 m',
    '1 mi' : '1609.34 m',
    '1 m'  :  '1 m',
    '1 km' : '1000 m'
}

print(f"12 ft is {num_converter.get(distance)(units)}")

#left off with trying to create a number converter.
# code needs to have the ability to convert for larger numbers (can not be a string#
#need to figure out how to get 2 thing out  dictionary
#concatinate the input, and add int values then return to a string for a print?