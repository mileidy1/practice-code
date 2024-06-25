# ask the user what is distance in ft

# find a way to store users answers
distance = input('What is the distance in feet: ')
#print answer after user response not during
num_converter ={
    '12': '3.6576 m'
}
print(f"12 ft is {num_converter.get(distance)}")