class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in ans:
                return (ans[needed], i)
            else:
                ans[nums[i]] = i
        
    
        