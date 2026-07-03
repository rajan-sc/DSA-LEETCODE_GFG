class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxi = 0
        temp = 0
        n = len(height)
        s = 0
        e = n-1
        while s <= e:
            temp = min(height[s], height[e]) * (e-s)
            maxi = max(temp, maxi)
            if height[s] < height[e]:
                s += 1
            else:
                e -= 1
        return maxi

         