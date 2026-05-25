class Solution(object):
        def twoSum(self, nums, target):
                """
                :type nums: List[int]
                :type target: int
                :rtype: List[int]
                """
                for i in range(len(nums)):
                    for j in range(i + 1,len(nums)):
                        if nums[i] + nums[j] == target :
                            return [i,j]
print(Solution().twoSum([1,3,5,7],8))