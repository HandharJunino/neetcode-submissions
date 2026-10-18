class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = max(piles)

        l, r = 1, n

        k = n

        while l <= r:
            m = (l + r) // 2
            total_hrs = 0
            for p in piles:
                total_hrs += math.ceil(p/m)

            if total_hrs > h:
                l = m + 1

            else:
                r = m - 1
                k = min(k, m)

        return k