from typing import List

def findPeakElement(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return left


# Example usage
nums = list(map(int, input("Enter the numbers : ").split()))
print("Peak element's Index is : ", findPeakElement(nums))
