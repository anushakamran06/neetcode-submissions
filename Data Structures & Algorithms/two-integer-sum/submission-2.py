class Solution:  # output is a list of int
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# 01 02 03 04
# 12 13 14
# 23 24
# guaranteed one sol, no need to worry abt no/multiple sol
