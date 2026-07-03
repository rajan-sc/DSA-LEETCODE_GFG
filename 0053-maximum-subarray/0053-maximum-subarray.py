class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = nums[0]
        current = nums[0]
        
        for i in range(1, n):
            current = max(nums[i], current + nums[i])
            maxi = max(current, maxi)
        return maxi


            