#ask the user for the distance, the starting units, and the units to convert to.
import random
converter = {
'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000
}
user_distance = input('What is the distance? ')
#input for integer
user_starting_units = input('Enter the starting units? ')
# starting units
user_ending_units = input('Enter the units you would like to convert to? ')
#units that the wants it to be converted to
user_distance = int(user_distance)
#converted from string to int for calculation


final_distance = user_distance * converter[user_starting_units] / converter[user_ending_units] # 0.3048 / 1
#100 * meters / ft(plain text)
print(f"{user_distance} {user_starting_units} is {final_distance} {user_ending_units}.")

#how i did it in the coding academy
