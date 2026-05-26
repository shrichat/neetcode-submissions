class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {')':'(', ']':'[', '}':'{'}

        for c in s:
            if c not in hashmap:
                stack.append(c)
            else:
                if len(stack)== 0:
                        return False
                else:
                    popped = stack.pop()
                    if popped != hashmap[c]:
                        return False

        return bool(len(stack)==0)



           

        