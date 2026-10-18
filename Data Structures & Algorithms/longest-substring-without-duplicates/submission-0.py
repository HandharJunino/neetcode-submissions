class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        windowStart = 0
        freq = defaultdict(int)
        maxLength = 0

        for windowEnd in range(len(s)):
            endChar = s[windowEnd]
            freq[endChar] += 1

            while freq[endChar] > 1:
                startChar = s[windowStart]

                freq[startChar] -= 1

                if freq[startChar] == 0:
                    del freq[startChar]

                windowStart += 1

            maxLength = max(maxLength, windowEnd - windowStart + 1)

        return maxLength