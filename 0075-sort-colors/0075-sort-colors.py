class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        s = 0
        e = n - 1
        m = 0
        while m <= e:
            if nums[m] == 0:
                nums[m], nums[s] = nums[s], nums[m]
                m += 1
                s += 1
            elif nums[m] == 1:
                m += 1
            else:
                nums[m], nums[e] = nums[e], nums[m]
                e -= 1
            