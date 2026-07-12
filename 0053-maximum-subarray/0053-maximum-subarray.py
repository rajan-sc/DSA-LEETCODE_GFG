class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = nums[0]
        curr = nums[0]
        for i in range(1, n):
            curr = max(curr + nums[i], nums[i])
            maxi = max(curr, maxi)
        return maxi


            