class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ""
        for char in s:
            if char.isalnum():
                temp+=char.lower()
        
        reverse = temp[::-1]

        if reverse == temp:
            return True
        else:
            return False
        
        

        