import math
def findMedianSortedArrays(nums1, nums2) :
    totalLen = len(nums1) + len(nums2)
    arr = nums1 + nums2
    arr = sorted(arr)

    if totalLen % 2 == 0:
        index = totalLen // 2
        median = (arr[index] + arr[index - 1]) / 2

    else:
        index = math.floor(totalLen / 2)
        median = arr[index]

    return median


nums1 = list(map(int, input("Enter numbers in 1st array by space : ").split()))
nums2 = list(map(int, input("Enter numbers in 2nd array by space : ").split()))
result = findMedianSortedArrays(nums1, nums2)
print("The median of two sorted array : ", result)