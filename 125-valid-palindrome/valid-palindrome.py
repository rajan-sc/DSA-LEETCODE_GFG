class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ""
        for i in s:
            if i.isalnum():
                temp += i.lower()
        start = 0
        end = len(temp)-1
        is_palindrome = True
        while start <= end:
            if temp[start] != temp[end]:
                is_palindrome = False
                break
            start += 1
            end -= 1
        if is_palindrome:
            return True
        else:
            return False

                
        