class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ans_1 = {}
        ans_2 = {}
        for i in s:
            if i in ans_1:
                ans_1[i] += 1
            else:
                ans_1[i] = 1
        for j in t:
            if j in ans_2:
                ans_2[j] += 1
            else:
                ans_2[j] = 1
        return ans_1 == ans_2