"""Below is the python program to perform binary search on arrays
   Binary search only works on sorted arrays
"""


def binary_search(nums, target):
    if len(nums) == 0:
        print("Empty Array!")
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid #index location of the target element
        elif nums[mid] < target:
            left += 1
        else:
            right -= 1
    return "Target not found!"
nums = [4, 6, 9, 13, 87, 102, 203, 405]
print(binary_search(nums, 103))#This will print target not found as 103 is not in nums
print(binary_search(nums, 87))#This will print 4, which is index location of target 87