# Maximum palindrome number from a product of two 3 digit number

def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False

# Efficient 
def max_palindrome(num):
    max_product = 1

    for i in range(num, 1, -1):
        for j in range(num-1, 1, -1):
            if is_palindrome(i*j) and i*j > max_product:
                max_product = i*j
                break
            elif i*j < max_product:
                break

    return max_product


# Non Efficient
def longest_palindrome(num):
    return max(i*j for i in range(num,1,-1) for j in range(num-1, 1, -1) if is_palindrome(i*j))

'''
import time

print("***First Test***")
start1 = time.time()
print(max_palindrome(999))
end1 = time.time() - start1
print(end1)

print("***Second Test***")
start2 = time.time()
print(longest_palindrome(999))
end2 = time.time() - start2
print(end2)
''' 
