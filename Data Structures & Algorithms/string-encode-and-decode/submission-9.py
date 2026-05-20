class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            length = str(len(string))
            delim = "#"
            encoded_string = encoded_string + (length+delim+string)

        return encoded_string
    

    def decode(self, encoded_string: str) -> List[str]:
        original_strings = []
        i = 0
        while i<len(encoded_string):
            hashtag_index = encoded_string.find("#", i)
            length_of_string = int(encoded_string[i:hashtag_index])

            start_of_word = hashtag_index + 1
            end_of_word = start_of_word + length_of_string

            word = encoded_string[start_of_word:end_of_word]
            original_strings.append(word)

            i = end_of_word

        return original_strings
        

        
        
        
        
