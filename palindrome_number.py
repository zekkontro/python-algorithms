# 12321
class Solution:
    def isPalindrome(self, x: int) -> bool:
        xStr = str(x)
        characterList  = [x for x in xStr]
        characterList.reverse()
        reversedStr = ""
        for letter in characterList:
            reversedStr = reversedStr + letter
        if xStr == reversedStr:
            return True
        else:
            return False

print(Solution().isPalindrome(121))