class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_length = len(s1)
        s2_length = len(s2)
        s1_counts = [0] * 26

        for i in range (s1_length):
            s1_counts[ord(s1[i]) - 97] += 1
        
        for i in range (s2_length):
            window = s2[i:i+s1_length]
            s2_counts = [0]*26
            for j in range(len(window)):
                s2_counts[ord(window[j]) - 97] += 1
            if s2_counts == s1_counts:
                return True

        
        return False



            


            

            

        

    



        