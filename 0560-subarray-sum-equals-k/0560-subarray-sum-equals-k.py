class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        seen = {0:1}
        prefix_sum = 0
        count = 0


        for num in nums:
            prefix_sum += num

            if (prefix_sum - k) in seen:
                count += seen[prefix_sum - k]

            if prefix_sum in seen:
                seen[prefix_sum] += 1
            else:
                seen[prefix_sum] = 1

        return count