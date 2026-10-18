class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = defaultdict(int)
        n = len(s1)
        windowMap = defaultdict(int)
        windowStart = 0

        if n > len(s2):
            return False

        for i in range(n):
            s1_map[s1[i]] += 1

        for windowEnd in range(len(s2)):
            windowMap[s2[windowEnd]] += 1

            if windowEnd >= n - 1:
                if s1_map == windowMap:
                    return True

                windowMap[s2[windowStart]] -= 1

                if windowMap[s2[windowStart]] == 0:
                    del windowMap[s2[windowStart]]

                windowStart += 1

        return False