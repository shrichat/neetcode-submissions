class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict={}
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num]+=1

        sorted_dict = sorted(dict.items(), key = lambda x: x[1], reverse = True)

        top_k_elements = []
        for item in sorted_dict[:k]:
            top_k_elements.append(item[0])

        return top_k_elements

        