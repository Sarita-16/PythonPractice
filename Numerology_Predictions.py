# Your code here
def fortunes(name):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    sum = 0

    for i in name.lower():
        if i in alphabet:
            # Get the value of the character
            value = alphabet.index(i) + 1
            # Add the value to the total value
            sum = sum + value

    if sum % 3 == 0:
        print("Bad")
    elif sum % 3 == 1:
        print("Good")
    else:
        print("Excellent")

name = input("Enter your name : ")
result = fortunes(name)
