class Solution:  # output is a list of int
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# guaranteed one sol, no need to worry abt no/multiple sol

class Solution2: 
    def twoSum(self, nums:List[int], target: int) -> List[int]:
        check = {}
        for i, num1 in enumerate(nums):
            seen[num1] = i #index is key
        for i, num1 in enumerate(nums):
            num2 = target - num1 
            if num2 in check and check[num2] != i:
                return [i, check[num2]]

        















