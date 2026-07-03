class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = {}
        f_ans = []
        for i in nums:
            if i in ans:
                ans[i] += 1
            else:
                ans[i] = 1
        a = sorted(ans.items(), key=lambda x: x[1], reverse=True)

        for i in range(k):
            f_ans.append(a[i][0])
        return f_ans

