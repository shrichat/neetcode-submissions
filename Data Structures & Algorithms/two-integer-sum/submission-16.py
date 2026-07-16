class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx,num in enumerate (nums):
            seen[num] = idx
        
        for idx,num in enumerate(nums):
            remainder = target - num
            if remainder in seen and idx!=seen[remainder]:
                return [idx,seen[remainder]]
