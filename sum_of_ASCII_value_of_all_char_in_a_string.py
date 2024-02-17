import re

str_input = input("Enter the String : ")
print("Length of input string:", len(str_input))

'''
re: regular expressions.
sub(): Function of re module. Short from "substitute". Used for replacing a pattern in a string with another string.
r: This is a raw string. 
\s: A regular expression pattern that matches any whitespace character.
"": This is the replacement string.
str: This is the input string.
'''

#str_space_removed = re.sub(r'\s', "", str_input)
#print("String with spaces removed:", str_space_removed)

str_ASCII_sum = 0
for i in range(len(str_input)):
    str_ASCII_sum += ord(str_input[i])

print("Sum of ASCII value of all characters in the string:", str(str_ASCII_sum))
