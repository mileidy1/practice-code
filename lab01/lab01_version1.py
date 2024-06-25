# ask the user what is distance in ft

import random

num_converter = {
    'ft': 3.6576,
}

#need to get info from user

user_input = input('Enter number of feet: ')

#recieves user input as a string

user_input = int(user_input)

#converts user input into a integer

print(f"The conversion for {user_input}ft into meters is {user_input * num_converter['ft']}m.")

#print conversion / do calculations inside of the print statement