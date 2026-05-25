class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for string in strs:
            length = str(len(string))
            delim = "#"
            s+= (length+delim+string)

        return s


    def decode(self, s: str) -> List[str]:
        original_strings = []
        current_pos = 0

        while current_pos<len(s):
            hashtag_index = s.find("#", current_pos)
            length = int(s[current_pos:hashtag_index])

            start_of_word = hashtag_index + 1
            end_of_word = start_of_word + length

            word = s[start_of_word : end_of_word]

            original_strings.append(word)
            current_pos = end_of_word
        return original_strings


            



