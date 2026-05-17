class Solution:
    def isPalindrome(self, s: str) -> bool:
        non_alphanumeric_s = ""
        for element in s:
            if element.isalnum():
                non_alphanumeric_s+=element
            else:
                continue

        reversed_s = non_alphanumeric_s[::-1]
        if non_alphanumeric_s.lower() == reversed_s.lower():
            return True
        return False


        