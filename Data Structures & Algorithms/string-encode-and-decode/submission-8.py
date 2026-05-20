class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            length = str(len(word))
            delim = "#"

            encoded_string+=(length + delim + word)

        return encoded_string
            


    def decode(self, s: str) -> List[str]:
        original_strings = []
        i = 0

        while i<len(s):
            hashtag_index = s.find("#",i)
            length_of_word = int(s[i:hashtag_index])

            start_of_word = hashtag_index + 1
            end_of_word = start_of_word + length_of_word

            word = s[start_of_word : end_of_word]

            original_strings.append(word)

            i = end_of_word
        
        return original_strings
