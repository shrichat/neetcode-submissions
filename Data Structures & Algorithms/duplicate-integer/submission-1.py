class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums2 = set()
        for num in nums:
            if num not in nums2:
                nums2.add(num)
            else:
                return True
        return False
