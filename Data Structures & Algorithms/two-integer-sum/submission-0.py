class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = {}
        for i in range(len(nums)):
            other = target - nums[i]
            if other in num_set:
                return [num_set[other], i]
            num_set[nums[i]] = i
            

        return []
