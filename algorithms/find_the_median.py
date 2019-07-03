# Hackerrank Find the Medain problem

import math


n = int(input().strip())
ar = [int(i) for i in input().split()]

def quicksort(myList, start, end):
    if start < end:
        # partition the list
        pivot = partition(myList, start, end)
        # sort both halves
        quicksort(myList, start, pivot-1)
        quicksort(myList, pivot+1, end)
    return myList

def partition(myList, start, end):
    pivot = myList[start]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            # swap places
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
    # swap start with myList[right]
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right

ar = quicksort(ar, 0, len(ar)-1)
if n%2 == 1:
    print(ar[math.floor(n/2)])
elif n%2 == 0:
    low_median = ar[math.floor(n/2)]
    high_median = ar[math.ceil(n/2)]
    median = (low_median+high_median)/2
    print(median)
