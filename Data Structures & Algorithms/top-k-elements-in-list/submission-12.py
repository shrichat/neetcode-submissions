class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Creating hashmaps of counts
        counts = {}
        for num in nums:
            if num in counts:
                counts[num]+=1
            else:
                counts[num] = 1

        # Creating buckets of keys 

        '''The keys are added to the buckets or sublists 
        belonging to the index corresponding to the number of 
        times they appear in the list'''

        freq = []
        for i in range(len(nums)+1):
            freq.append([])


        for num, cnt in counts.items():
            freq[cnt].append(num)

        k_elements = []
        for sublists in range(len(freq)-1,-1,-1):
            for num in freq[sublists]:
                k_elements.append(num)
            if len(k_elements) == k:
                return k_elements




            
        