class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        curr = nums[0]
        n = len(nums)
        for i in range(1, n):
            curr = max(curr + nums[i], nums[i])
            maxi = max(curr, maxi)
        return maxi 
