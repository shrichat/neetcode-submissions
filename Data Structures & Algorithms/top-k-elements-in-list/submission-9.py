class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1


        keys = []
        values = []
        for key,v in freq.items():
            keys.append(key)
            values.append(v)
        

        k_elements = []
        while len(k_elements)<=k-1:
            max_index = values.index(max(values))
            k_elements.append(keys[max_index])
            values.pop(max_index)
            keys.pop(max_index)
        
        return k_elements

            
            
        

        


        


       
        