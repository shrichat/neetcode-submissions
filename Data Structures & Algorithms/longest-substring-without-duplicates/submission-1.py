class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        seen = set()
        longest = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            
            w = (r-l)+1
            longest = max(longest, w)
            seen.add(s[r])

        return longest



        