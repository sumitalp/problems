'''
You are a waiter at a party. There is a pile of numbered plates. Create an empty  array. At each iteration, , remove each plate from the top of the stack in order. Determine if the number on the plate is evenly divisible by the  prime number. If it is, stack it in pile . Otherwise, stack it in stack . Store the values in  from top to bottom in . In the next iteration, do the same with the values in stack . Once the required number of iterations is complete, store the remaining values in  in , again from top to bottom. Return the  array.

Example



An abbreviated list of primes is . Stack the plates in reverse order.



Begin iterations. On the first iteration, check if items are divisible by .


Move  elements to .


On the second iteration, test if  elements are divisible by .


Move  elmements to .


And on the third iteration, test if  elements are divisible by .


Move  elmements to .


All iterations are complete, so move the remaining elements in , from top to bottom, to .

. Return this list.

Function Description

Complete the waiter function in the editor below.

waiter has the following parameters:

int number[n]: the numbers on the plates
int q: the number of iterations
Returns

int[n]: the numbers on the plates after processing
Input Format

The first line contains two space separated integers,  and .
The next line contains  space separated integers representing the initial pile of plates, i.e., .

Constraints




Sample Input 0

5 1
3 4 7 6 5
Sample Output 0

4
6
3
7
5
Explanation 0

Initially:

 = [3, 4, 7, 6, 5]<-TOP

After 1 iteration (divide by 2, the 1st prime number):

 = [5, 7, 3]<-TOP

 = [6, 4]<-TOP

Move  elements to .


All iterations are complete, so move  elements to .

.

Sample Input 1

5 2
3 3 4 4 9
Sample Output 1

4
4
9
3
3
Explanation 1

Initially:

A = [3, 3, 4, 4, 9]<-TOP

After 1st  iteration (divide by 2):

A1 = [9, 3, 3]<-TOP

B1 = [4, 4]<-TOP

Move B1  to answers.


After 2nd iteration (divide by 3):

A2 = []<- TOP

B2 = [3, 3, 9]<-TOP

Move B2  elements to answers.


There are no values remaining in A2.
'''

def waiter(number, q):
    answers = []
    def prime_generator(end):
        for n in range(2, end+1):     # n starts from 2 to end
            for x in range(2, n):   # check if x can be divided by n
                if n % x == 0:      # if true then n is not prime
                    break
            else:                   # if x is found after exhausting all values of x
                yield n             # generate the prime
    g = list(prime_generator(10000))       # give first 10000 prime numbers
    
    for i in range(q):
        prime = g[i]
        A, B = [], []
        while number:
            n = number.pop()
            if n % prime == 0:
                B.append(n)
            else:
                A.append(n)
        
        number = A
        answers += B[::-1]
    
    return answers + number[::-1]
    
