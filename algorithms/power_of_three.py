# LeetCode: Power of Three problem

class Solution(object):
	def isPowerOfThree(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		if n == 0:
			return False

		return self.generateN(n) == 1

	def generateN(self, n):
		if n%3 == 0:
			n /= 3
			n = self.generateN(n)

		return n


if __name__ == '__main__':
	print(Solution().isPowerOfThree(27))
