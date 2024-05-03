"""Below is the program for merge-sort"""

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]

    return merge(merge_sort(left, right))



