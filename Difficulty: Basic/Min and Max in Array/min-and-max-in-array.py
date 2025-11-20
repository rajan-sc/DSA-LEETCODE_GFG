class Solution:
    def getMinMax(self, arr):
        # code here
        mini = float('inf')
        maxi = -float('inf')
        for i in arr:
            if i > maxi:
                maxi = i
            if i < mini:
                mini = i
        return [mini, maxi]