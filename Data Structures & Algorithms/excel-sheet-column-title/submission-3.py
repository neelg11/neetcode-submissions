class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res=""
        while(columnNumber):
            columnNumber-=1
            element = columnNumber%26
            res = chr(ord('A')+element) + res
            columnNumber = columnNumber // 26
        return res