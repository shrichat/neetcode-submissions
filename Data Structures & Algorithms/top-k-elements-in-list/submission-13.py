class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            if num in counts:
                counts[num]+=1
            else:
                counts[num] = 1
        

        buckets = [[] for i in range (len(nums)+1)]

        for num,cnt in counts.items():
            buckets[cnt].append(num)

        buckets = buckets[::-1]
        k_freq = []

        for bucket in buckets:
            if len(bucket)!= 0:
                for num in bucket:
                    k_freq.append(num)

                    if len(k_freq) == k:

                        return k_freq




        

        
        