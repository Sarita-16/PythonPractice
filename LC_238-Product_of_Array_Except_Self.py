def solution(nums):

    ''' answer = []

    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if j == i:
                continue
            else:
                product = product * nums[j]

        answer.append(product)

    print("Product of all element except self : ", answer)      '''

    n = len(nums)
    ans = [0] * n
    product = 1
    zeros = 0

    for num in nums:
        if num == 0:
            zeros += 1
            continue
        product *= num

    if zeros == 1:
        for i in range(n):
            ans[i] = product if nums[i] == 0 else 0
    elif zeros == 0:
        for i in range(n):
            ans[i] = product // nums[i]

    print(ans)



n = int(input("How many numbers you want to insert : "))
nums = []
for i in range(n):
    nums.append(int(input()))
solution(nums)