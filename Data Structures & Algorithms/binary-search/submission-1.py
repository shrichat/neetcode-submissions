class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if target in nums:
            return nums.index(target)
        # l = 0 
        # r = len(nums) - 1
        
        # while l<=r:
        #     mid = (l+r)//2

        #     if nums[mid] == target:
        #         return mid

        #     if nums[mid] > target:
        #         r = mid - 1
        #     else:
        #         l = mid + 1
        
        if target not in nums:
            return - 1

        