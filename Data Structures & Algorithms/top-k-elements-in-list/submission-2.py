class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        count = 1
        for num in nums:
            keys = num

            if keys not in dict:
                dict[keys] = count
            else:
                dict[keys]+=1

        sorted_dict = sorted(dict.items(), key = lambda x: x[1], reverse=True)

        top_k_keys = []
        for item in sorted_dict[:k]:
            top_k_keys.append(item[0])


        return top_k_keys

        



        

        