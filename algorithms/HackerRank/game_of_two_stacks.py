'''
Alexa has two stacks of non-negative integers, stack  and stack  where index  denotes the top of the stack. Alexa challenges Nick to play the following game:

In each move, Nick can remove one integer from the top of either stack  or stack .
Nick keeps a running sum of the integers he removes from the two stacks.
Nick is disqualified from the game if, at any point, his running sum becomes greater than some integer  given at the beginning of the game.
Nick's final score is the total number of integers he has removed from the two stacks.
Given , , and  for  games, find the maximum possible score Nick can achieve.

Example


The maximum number of values Nick can remove is . There are two sets of choices with this result.

Remove  from  with a sum of .
Remove  from  and  from  with a sum of .
Function Description
Complete the twoStacks function in the editor below.

twoStacks has the following parameters: - int maxSum: the maximum allowed sum
- int a[n]: the first stack
- int b[m]: the second stack

Returns
- int: the maximum number of selections Nick can make

Input Format

The first line contains an integer,  (the number of games). The  subsequent lines describe each game in the following format:

The first line contains three space-separated integers describing the respective values of  (the number of integers in stack ),  (the number of integers in stack ), and  (the number that the sum of the integers removed from the two stacks cannot exceed).
The second line contains  space-separated integers, the respective values of .
The third line contains  space-separated integers, the respective values of .
Constraints

Subtasks

 for  of the maximum score.
Sample Input 0

1
5 4 10
4 2 4 6 1
2 1 8 5
Sample Output 0

4
Explanation 0

The two stacks initially look like this:

image

The image below depicts the integers Nick should choose to remove from the stacks. We print  as our answer, because that is the maximum number of integers that can be removed from the two stacks without the sum exceeding .

image

(There can be multiple ways to remove the integers from the stack, the image shows just one of them.)
'''


# Complexity O(a+b) 

def twoStacks(maxSum, a, b):
    running_sum = 0
    count_1 = 0
    count_2 = 0
    result = 0
    
    # Go through stack A first
    for el in a:
        if (running_sum + el) > maxSum:
            break
        running_sum += el
        count_1 += 1
        
    result = count_1
        
    # Go through stack B
    for el in b:
        running_sum += el
        count_2 += 1
        
        while (running_sum > maxSum) and (count_1 != 0):
            running_sum -= a[count_1 - 1]
            count_1 -= 1
        
        # For the case when there are no values from stack A to remove
        if running_sum > maxSum:
            break
            
        result = max(result, count_1 + count_2)
        
    return result
