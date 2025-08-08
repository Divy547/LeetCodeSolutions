# Last updated: 8/9/2025, 2:27:27 AM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        area = 0
        while i < j:
            currarea = min(height[i], height[j])*(j-i)
            area = max(area, currarea)
            if height[i] < height[j]:
                i += 1
            else:
                j-=1
            
        return area