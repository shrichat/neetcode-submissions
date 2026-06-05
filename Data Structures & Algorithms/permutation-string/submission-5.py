class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)

        if l1>l2:
          return False
        
        counts_1 = [0] * 26
        counts_2 = [0] * 26

        for i in range(l1):
            counts_1[ord(s1[i]) - 97] += 1
            counts_2[ord(s2[i]) - 97] += 1

        if counts_1 == counts_2:
            return True

        for i in range (l1,l2):
            counts_2[ord(s2[i]) - 97] += 1
            counts_2[ord(s2[i - l1]) - 97] -= 1

            if counts_2 == counts_1:
                return True
        
        return False

            
            

        
        
        