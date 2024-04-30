#Bubble sort program to sort an array

def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    print(nums)

nums = [5,4,3,2,1]

bubble_sort(nums)