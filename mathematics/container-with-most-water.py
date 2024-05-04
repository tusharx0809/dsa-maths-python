"""
This problem is a classic problem solving called Container with most water and below is my solution.
You have an array of integers, where each integer represents the height of a vertical line on a chart. The position of each line on the chart corresponds to its index in the array, and the two ends of the line are at (i, 0) and (i, height[i]).

Your task is to identify two lines that, along with the x-axis, form a container. The goal is to find the container that can hold the maximum amount of water.

Your output should be the greatest volume of water that such a container can hold.
Input: heights = [1,8,6,2,5,4,8,3,7] where the area with be 49
Explanation:

8    |         |
7    |         |   |
6    | |       |   |
5    | |   |   |   |
4    | |   | | |   |
3    | |   | | | | |
2    | | | | | | | |
1  | | | | | | | | |
0  0 1 2 3 4 5 6 7 8 

This program uses binary search to solve this problem
"""

def max_area(heights):
    left = 0
    right = len(heights) - 1
    max_area = 0
    while left < right:
        area = min(heights[left],heights[right]) * (right - left)
        max_area = max(max_area,area)
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return max_area

print(max_area([1,8,6,2,5,4,8,3,7]))

