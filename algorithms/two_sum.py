# Two Sum problem in LeetCode OJ

class Solution(object):
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		final_dict = {}
		for i, v in enumerate(nums):
			final_dict[v] = i

		# Check if 'target-v' is key in my created dictionary and simultaneously assert 
		# that value pointed to by that key is not i.
		# If this is ever true, return tuple i, final_dict.get(target-v)
		ret_list = next(( (i, final_dict.get(target-v)) for i, v in enumerate(nums) if final_dict.get(target-v) != i), None)

		return ret_list
