class Solution:
    def minWindow(self, s: str, t: str) -> str:

        #Step 1 : create dictionary with count of characters in string t , assign an empty
        # dictionary with default values as integer types
        d = {}
        for char in t:
            if char in d:
                d[char]+=1
            else:
                d[char] = 1
            
        #Step 2 : create variables to track how many letters we formed, vs total needed
        formed, total = 0, len(d)

        l = r = 0
        len_ans = float("inf")
        subl, subr = 0,0

        #Step 3: initialize while loop that goes element by element until 
        # r cannot expand anymore and is at the last element in s

        while r < len(s):
            char = s[r]
            if char in d:
                d[char] -= 1

                if d[char] == 0:
                    formed+=1
            while l <= r and formed == total:
                curr_len = r - l + 1
                if curr_len < len_ans:
                    len_ans = curr_len
                    subl = l
                    subr = r+1
                
                char = s[l]
                if char in d:
                    if d[char] == 0:
                        formed -=1
                    d[char] += 1
                l+=1
            r+=1
        
        return "" if len_ans == float("inf") else s[subl:subr]




        


            

 

         

        