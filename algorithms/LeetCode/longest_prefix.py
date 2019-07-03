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