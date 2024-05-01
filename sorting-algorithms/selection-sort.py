"""Below is the program for selection sort"""

def selection_sort(nums):
    size = len(nums)
    for i in range(size):
        min_index = i
        for j in range(i+1, size):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    print(nums)

nums = [5,4,3,2,1]
selection_sort(nums)