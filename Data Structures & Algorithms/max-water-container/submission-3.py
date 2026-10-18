class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Initialize left and right pointers
        l, r = 0, len(heights) - 1
        max_water = 0

        while l < r:
            # Calculate the area for the current pointers
            width = r - l
            height = min(heights[l], heights[r])
            max_water = max(max_water, width * height)

            # Move the pointer pointing to the shorter line inward
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_water