class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_length = len(s1)
        s2_length = len(s2)

        if s1_length>s2_length:
            return False

        counts_s1 = [0]*26
        counts_s2 = [0]*26

        for i in range (s1_length):
            counts_s1[ord(s1[i]) - 97] += 1
            counts_s2[ord(s2[i]) - 97] += 1
        
        if counts_s1 == counts_s2:
            return True
        
        else:
            for i in range(s1_length, s2_length):
                counts_s2[ord(s2[i]) - 97] += 1
                counts_s2[ord(s2[i-s1_length]) - 97] -= 1
                if counts_s1 == counts_s2:
                    return True
        
        return False


        
        