'''
Input :
5
8 8 78 8 8
Output :
3 (Index of odd/ different number)
'''

def find_impostor_index(n, arr):
    # Count occurrences of each element
    element_count = {}
    for i in range(n):
        if arr[i] in element_count:
            element_count[arr[i]] += 1
        else:
            element_count[arr[i]] = 1
    
    # Find the element with count 1 (the impostor)
    impostor = None
    for key, value in element_count.items():
        if value == 1:
            impostor = key
            break
    
    # Find the index of the impostor
    impostor_index = arr.index(impostor) + 1
    return impostor_index

# Input reading
n = int(input())
arr = list(map(int, input().split()))

# Output the result
result = find_impostor_index(n, arr)
print(result)

