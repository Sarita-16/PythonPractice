'''def createStack():
    stack = []
    return stack


def isEmpty(stack):
    return len(stack) == 0


def push(stack, item):
    stack.append(item)
    print(item + " is pushed :) ")


def pop(stack):
    if isEmpty(stack):
        return "Stack is Underflow :( nothing "
    return stack.pop()


def peek(stack):
    if isEmpty(stack):
        return "Stack is Underflow :( So, nothing "
    return stack[len(stack)-1]


stack = createStack()

push(stack, str(10))
push(stack, str(20))

print(str(pop(stack)) + " is Popped :] ")
print(str(pop(stack)) + " is Popped :] ")
print(str(pop(stack)) + " is Popped :] ")
#print(str(pop(stack)) + " is Popped :] ")

print(str(peek(stack)) + " is the Top most item :}")        '''

'''
a, b = list(map(int, input(). split(" ")))

if a >= 1 and b >= 1 and a <= 100 and b <= 100:
    if a <= 10 and b >= 10:
        print("true", end=" ")
    else:
        print("false", end=" ")
    if a % 2 == 0 or b % 2 == 0:
        print("true", end=" ")
    else:
        print("false", end=" ")
    if a != b:
        print("true", end=" ")
    else:
        print("false", end=" ")     '''

'''
a = 2
b = 3
c = 4
d = 5
result = (a + b + c + d)/4
print(result)

# f to c
f  = int(input())
c = (f - 32) * (5/9)
print(c)        '''

''' a, b = list(map(int, input().split(" ")))
a = a + b
b = a - b
a = a - b
print(a, b) '''

'''
def character_value(char):
    char = char.lower()  # Convert the character to lowercase
    alphabet = 'abcdefghijklmnopqrstuvwxyz'  # Define the alphabet
    value = alphabet.index(char) + 1  # Get the index of the character in the alphabet and add 1
    return value

# Test the function
print(character_value('as'))  # Output: 1
'''

'''
def getDiscount(SP, A, W):
    discount = 0

    if W == 'A' or W == 'B':
        discount += 5
        if A >= 50:
            discount += 5

    final_price = SP - discount

    return final_price


SP = int(input())
A = int(input())
W = input()
r = getDiscount(SP, A, W)
print(r)            '''

'''def calculateFine(X, D, staff):
    c = 0
    if D <= 7:
        c = X
    else:
        if staff == False:
            c = (2 * (D - 7))
            c = X + c
        else:
            c = X
    print(c)
X = int(input())
D = int(input())
staff = input().strip().lower() == "true"
calculateFine(X, D, staff)
    '''

'''
def trianglePattern(n):
    for i in range(n, 0, -1):

        if i >= n:
            print(i)

        else:
            for j in range(i, n+1):
                print(j, end='')

            print('')

n = int(input())
trianglePattern(n)      '''

'''
def palindromic(N):
    for i in range(0, N+1):
        for j in range(i, N):
            print(' ', end=' ')

        for j in range(1, i + 1):
            print(j, end=' ')

        for j in range(i - 1, 0, -1):
            print(j, end=' ')

        print()


N = int(input())
palindromic(N)          '''

################################################################################

''' h = eval(input("Enter diamond's height: "))

for x in range(h):
    print(" " * (h - x), "*" * (2*x + 1))
for x in range(h - 2, -1, -1):
    print(" " * (h - x), "*" * (2*x + 1))           '''

'''
N = int(input())
str_N = str(N)
count = len(str_N)
sumOdd = 0
sumEven = 0
for i in range(count):
    if int(str_N[i]) % 2 == 0:
        sumEven = sumEven + int(str_N[i])  # Convert character to integer
    else:
        sumOdd = sumOdd + int(str_N[i])    # Convert character to integer


print("Even : ", sumEven)
print("Odd : ", sumOdd)
product = sumEven * sumOdd

print(product)      '''

'''
def armstrong(N):
    for i in range(1, N + 1):
        armstrong_sum = 0
        n = i
        count = len(str(n))
        while n != 0:
            r = n % 10
            armstrong_sum += r ** count
            n //= 10
        if i == armstrong_sum:
            print(i)            '''

'''     def armstrong(N):
    print(1, end=' ')
    for i in range(10, N + 1):

        armstrong_sum = 0
        n = i
        count = len(str(n))

        armstrong_sum = sum(int(digit) ** count for digit in str(n))

        if i == armstrong_sum:
            print(i, end=' ')


N = int(input())
armstrong(N)            '''

'''
def pattern(N):
    for i in range(2 * N):
        if i % 2 != 0:
            for i in range(2 * i):
                print('#', end='')

        else:
            for i in range(i + 1):
                print('*', end='')

        print()

N = int(input())
pattern(N)      '''

'''
def Pattern(N):
    j = 0
    k = 0
    for i in range(N):
        k = j
        for a in range(N):
            print(k, end=' ')
            k = k + 4
        print()
        j = j + 6


N = int(input())
Pattern(N)      '''

'''
def arrayChallenge(arr):
    # Write your code here
    counter = 0
    print(counter)
    for i in range(1, len(arr)):
        counter = 0
        for j in range(i-1, -1, -1):
            if arr[i] > arr[j]:
                counter = counter + abs(arr[i] - arr[j])
            elif arr[i] < arr[j]:
                counter = counter - abs(arr[i] - arr[j])

        print(counter)

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arrayChallenge(arr)     '''

'''
def Duplicate(nums):
    flag = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            print("i : ", i, "& j : ", j)
            if nums[i] == nums[j]:
                flag = 1
                break

    if flag == 1:
        return True
    else:
        return False

n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))
ans = Duplicate(nums)
print(ans)      '''

'''

from collections import Counter
anagram_map = defaultdict(list)

for word in strs:
    sorted_word = ''.join(sorted(word))
    anagram_map[sorted_word].append(word)

return list(anagram_map.values())   '''

'''
eat
tea
tan
ate
nat
bat
'''

'''
def isAnagram(s, t):
    return Counter(s) == Counter(t)

# Example usage
s = input("Enter first string: ")
t = input("Enter second string: ")
result = isAnagram(s, t)
print(result)       '''

"""
def removeEle(nums, val):
    count = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[count] = nums[i]
            count += 1
    return count

nums = [3,2,2,3]
val = 3
result = removeEle(nums, val)
print(result)"""





"""
# Taking multiple inputs separated by spaces
s, u, v = input().split()
print(s, u, v)

# Converting some of the inputs to integer & ASCII
u = ord(u)
v = chr(int(v))
print(s, u, v)

# Splitting the input string by commas
a, b, c = input().split(',')
print(a, b, c)

# strip() method is used to remove any leading or trailing whitespaces from each substring
s = "   Hello (>_<) !   "
print(s.strip())

# taking inputs by spacing & store that in arr
n = int(input())
arr = list(map(int, input().split()))
print(arr)
"""






"""s = "sadbutsad"
# Calculate the length of the string
length = len(s)

# Calculate the length of each portion
portion_length = length // 3

# Split the string into three portions
portion1 = s[:portion_length]
portion2 = s[portion_length:2*portion_length]
portion3 = s[2*portion_length:]

# Print the three portions
print("Portion 1:", portion1)
print("Portion 2:", portion2)
print("Portion 3:", portion3)"""






a = [1,2,3,8,6,0,9]
print(len(a))







