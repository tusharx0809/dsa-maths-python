"""Below is the program for Merge-sort - A very efficient sorting algorithms"""

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2 # to split the array in two halves
    left = nums[:mid]   # left half of the array
    right = nums[mid:]  # right half of the array

    return merge(merge_sort(left), merge_sort(right)) # divide and conquer the until length of array is 1

def merge(left, right):
    merged = [] # final sorted array to be returned
    left_idx = 0
    right_idx = 0

    while left_idx < len(left) and right_idx < len(right): # compare elements of each array until one of the arrays is completely traversed
        if left[left_idx] <= right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    merged.extend(left[left_idx:]) # add any remaining elements
    merged.extend(right[right_idx:]) # add any remaining elements

    return merged

array = [5,4,3,2,1]
sorted_array = merge_sort(array)

print(sorted_array)
    