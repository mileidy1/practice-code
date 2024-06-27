weight_converter = {
    'lbs': 2.20462,
    'kg': 0.453592
}

user_restart = 'yes'

while user_restart == 'yes' or user_restart == 'y':
    user_weight = input("\n Please enter your weight: ")

    user_measurement = input("\n(L)bs or (K)g: ")

    user_measurement = user_measurement.lower()

    if user_restart == 'yes' or user_restart == 'y':

        if user_measurement == 'kg' or user_measurement == 'k':
            conversion_of_weight = weight_converter['lbs'] * float(user_weight)
            print(f"\nYour weight conversion is: {conversion_of_weight} lbs ")
            user_restart = input("\nWould you like to restart? (yes/no):  ").lower()

        elif user_measurement == 'lbs' or user_measurement == 'l':
            conversion_of_weight = weight_converter['kg'] * float(user_weight)
            print(f"\nYour weight conversion is: {conversion_of_weight} kg ")
            user_restart = input("\nWould you like to restart? (yes/no):  ").lower()
        
        else:
            user_restart = input("Invalid input. Would you like to try again? (yes/no): ").lower()


if user_restart == 'no' or user_restart == 'n':
    print("\nThank you for using our app. Goodbye!")
else:
    print('couldnt run')
