class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n = len(pref)
        count = 0
        for i in words:
            ans = ""
            for j in i:
                ans += j
                if ans == pref:
                    count += 1
                    break
        return count
            





