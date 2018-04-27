# Leetcode Zigzag problem

def convert(s, num_rows):
	if not s or num_rows <= 1:
		return s

	output = ''

	for i in range(len(s)):
		k = i; temp = num_rows - 1
		while k < len(s):
			output += s[k]
			if (k%(num_rows-1) != 0) and (2*temp - k < len(s)):
				output += s[2*temp-k]

			k += (2 * num_rows - 2)
			temp += (2 * num_rows - 2)
		
		if len(s) == len(output):
			break

	return output

print(convert("PAYPALISHIRING", 3))
print(convert("PAYPALISHIRING", 4))

print(convert("FREIGHTHUBISHIRING", 3))