class Solution:
    def maxArea(self, heights: List[int]) -> int:
        r, l = 0, len(heights)-1
        max_water = 0

        while r<l:
            max_water = max(max_water, (l - r)  * min(heights[r], heights[l]))

            if heights[r] < heights [l]:
                r += 1
            else:
                l -= 1
        
        return max_water