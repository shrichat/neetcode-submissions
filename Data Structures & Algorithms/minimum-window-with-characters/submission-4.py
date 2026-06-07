class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #Step 1
        d = defaultdict(int)
        for char in t:
            d[char] += 1

        
        #Step 2
        total = len(d)
        formed = 0
        l = r = 0
        subl, subr = 0, 0 
        len_ans = float("infinity")

        #Step 3
        while r < len(s):
            char = s[r]
            if char in d:
                d[char] -= 1
                
                if d[char] == 0:
                    formed += 1
                
            while l<= r and formed == total:
                curr_len = r - l + 1
                if curr_len < len_ans:
                    len_ans = curr_len
                    subl = l
                    subr = r+1

                char = s[l]
                if char in d:

                    if d[char] == 0:
                        formed-=1
                    
                    d[char] += 1
                
                l+=1
            r+=1
        
        return "" if len_ans == float("inf") else s[subl:subr]


                    
            


            
        


        

        