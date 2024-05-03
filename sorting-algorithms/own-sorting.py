"""This is my own Sorting algorithm (not much efficient but works :) ).It arranges the numbers in a specific pattern where smaller and larger numbers alternate and converge towards the middle of the list"""
"""
Working Alogorithm:
nums = [5,4,3,2,1]
final = []
Add the min and max from nums to final araay so arr becomes [1,5]
Remove min and max from nums which is 1 and 5 so that nums = [4,3,2]
After removing, find the middle index by using mid = len(final) // 2 and add the min and max at position mid and mid + 1
Repeat this until nums is empty
final array will be the sorted array

"""
def unique_sort(nums):
  final = []
  while len(nums) != 0:
      if len(nums) == 1:
        mid = len(final) // 2
        final.insert(mid, nums[0])
        nums.remove(nums[0])
      else:
        if len(final) == 0:
          final.append(min(nums)) # change this to final.append(max(nums)) to sort it descending order
          final.append(max(nums)) # change this to final.append(min(nums)) to sort it descending order
        else:
          mid = len(final) // 2
          final.insert(mid,min(nums)) # change this to final.insert(mid,max(nums)) tp
          final.insert(mid+1,max(nums)) # change this to final.insert(mid+1,min(nums)) to sort it descending order
        nums.remove(min(nums))
        nums.remove(max(nums))
  return final 
nums = [100,98,12,45,67,43]
print(unique_sort(nums))
