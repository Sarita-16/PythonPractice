def majorityElement(nums):
    mdic = {}
    for i in nums:
        if i in mdic:
            mdic[i] += 1
        else:
            mdic[i] = 1
    maxCount = 0
    maxEle = None
    for key, value in mdic.items():
        if value > maxCount:
            maxCount = value
            maxEle = key
    return maxEle
nums = [2,2,1,1,1,2,2]
result = majorityElement(nums)
print(result)



