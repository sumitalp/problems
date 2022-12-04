# LeetCode 'Longest Prefix problem'

def longest_prefix(strs):
	if not strs:
		return ""

	prefix = strs[0]

	for i in range(1, len(strs)):
		prefix = find_longest_common_prefix(prefix, strs[i])

	return prefix

def find_longest_common_prefix(s1, s2):
	if len(s2) > len(s1):
		s1, s2 = s2, s1

	output = ""
	for i in range(len(s2)):
		if s1[i] != s2[i]:
			break
		output += s2[i]
	return output


print(longest_prefix(["flower","flow","flight"]))

def longest_common_prefix(strs):
	import os

	return os.path.commonprefix(strs)

print(longest_common_prefix(["flower","flow","flight"]))

def longest_prefix_divide_conquer(a: list, low, high):
	# Time Complexity: O(NM) N=length of strs, M=length of characters
	# Space Complexity: O(M log N)
  if not a:
    return ""
    
  if low==high:
    return a[low]
  
  # Using divide and conquer
  if high > low:
    mid = low + (high-low)//2
    s1 = longest_prefix_divide_conquer(a, low, mid)
    s2 = longest_prefix_divide_conquer(a, mid+1, high)
    
    return find_longest_common_prefix(s1, s2)

strs = ["flower","flow","flight"]
print(longest_prefix_divide_conquer(strs, 0, len(strs)-1))