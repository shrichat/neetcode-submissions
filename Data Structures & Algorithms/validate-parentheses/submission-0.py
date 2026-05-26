class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        hashmap = {')':'(',']':'[','}':'{'}

        for c in s:
            if c not in hashmap:
                stk.append(c)
            else:
                if len(stk) == 0:
                    return False
                else:
                    popped = stk.pop()
                    if popped != hashmap[c]:
                        return False

        return bool(len(stk)==0)




        
        