class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n = len(pref)
        count = 0
        ans = ""
        for i in words:
            
            for j in i:
                ans += j
                if ans == pref:
                    count += 1
                    break
            ans = ""
        return count
            





