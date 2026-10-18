class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        elem = []

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        for key , val in freq.items():
            elem.append([val, key])
        elem.sort()

        res = []
        while len(res) < k:
            res.append(elem.pop()[1])
        
        return res