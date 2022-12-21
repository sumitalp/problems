'''
Skyline Real Estate Developers is planning to demolish a number of old, unoccupied buildings and construct a shopping mall in their place. Your task is to find the largest solid area in which the mall can be constructed.

There are a number of buildings in a certain two-dimensional landscape. Each building has a height, given by . If you join  adjacent buildings, they will form a solid rectangle of area .

Example

A rectangle of height  and length  can be constructed within the boundaries. The area formed is .

Function Description

Complete the function largestRectangle int the editor below. It should return an integer representing the largest rectangle that can be formed within the bounds of consecutive buildings.

largestRectangle has the following parameter(s):

int h[n]: the building heights
Returns
- long: the area of the largest rectangle that can be formed within the bounds of consecutive buildings

Input Format

The first line contains , the number of buildings.
The second line contains  space-separated integers, each the height of a building.

Constraints

Sample Input

STDIN       Function
-----       --------
5           h[] size n = 5
1 2 3 4 5   h = [1, 2, 3, 4, 5]
Sample Output

9
Explanation

An illustration of the test case follows.
image
'''

'''
Approaches:

For every bar ‘x’, we calculate the area with ‘x’ as the smallest bar in the rectangle. If we calculate the such area for every bar ‘x’ and find the maximum of all areas, our task is done. 

How to calculate the area with ‘x’ as the smallest bar? 

We need to know the index of the first smaller (smaller than ‘x’) bar on the left of ‘x’ and the index of the first smaller bar on the right of ‘x’. Let us call these indexes as ‘left index’ and ‘right index’ respectively. We traverse all bars from left to right and maintain a stack of bars. Every bar is pushed to stack once. A bar is popped from the stack when a bar of smaller height is seen. When a bar is popped, we calculate the area with the popped bar as the smallest bar. 

How do we get the left and right indexes of the popped bar?

The current index tells us the right index and the index of the previous item in the stack is the left index

1. Create an empty stack.
2. Start from the first bar, and do the following for every bar hist[i] where ‘i‘ varies from 0 to n-1
	2.1. If the stack is empty or hist[i] is higher than the bar at top of the stack, then push ‘i‘ to stack. 
	2.2. If this bar is smaller than the top of the stack, then keep removing the top of the stack while the top of the stack is greater. 
	2.3. Let the removed bar be hist[tp]. Calculate the area of the rectangle with hist[tp] as the smallest bar. 
	2.4. For hist[tp], the ‘left index’ is previous (previous to tp) item in stack and ‘right index’ is ‘i‘ (current index).
3. If the stack is not empty, then one by one remove all bars from the stack and do step (2.2 and 2.3) for every removed bar
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangle(h):
    stack = []
    index, maxArea = 0, 0
    
    while index < len(h):
        if not stack or h[stack[-1]] <= h[index]:
            stack.append(index)
            index += 1
        else:
            top = stack.pop()
            area = h[top] * (index - stack[-1] - 1 if stack else index)
            
            maxArea = max(area, maxArea)
            
    while stack:
        top = stack.pop()
        area = h[top] * (index - stack[-1] - 1 if stack else index)
        maxArea = max(area, maxArea) 

    return maxArea


'''
Another approach

Largest Rectangular Area in a Histogram by finding the next and the previous smaller element:
To solve the problem follow the below idea:

Find the previous and the next smaller element for every element of the histogram, as this would help to calculate the length of the subarray in which this current element is the minimum element. So we can create a rectangle of size (current element * length of the subarray) using this element. Take the maximum of all such rectangles.

Follow the given steps to solve the problem:

First, we will take two arrays left_smaller[] and right_smaller[] and initialize them with -1 and n respectively
For every element, we will store the index of the previous smaller and next smaller element in left_smaller[] and right_smaller[] arrays respectively
Now for every element, we will calculate the area by taking this ith element as the smallest in the range left_smaller[i] and right_smaller[i] and multiplying it with the difference of left_smaller[i] and right_smaller[i]
We can find the maximum of all the areas calculated in step 3 to get the desired maximum area


Complexity for both solution: T: O(n), S: O(n)
'''
def getMaxArea(arr):
    s = [-1]
    n = len(arr)
    area = 0
    i = 0
    left_smaller = [-1]*n
    right_smaller = [n]*n
    while i < n:
        while s and (s[-1] != -1) and (arr[s[-1]] > arr[i]):
            right_smaller[s[-1]] = i
            s.pop()
        if((i > 0) and (arr[i] == arr[i-1])):
            left_smaller[i] = left_smaller[i-1]
        else:
            left_smaller[i] = s[-1]
        s.append(i)
        i += 1
    for j in range(0, n):
        area = max(area, arr[j]*(right_smaller[j]-left_smaller[j]-1))
    return area




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()

