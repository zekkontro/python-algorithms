class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        characters = [x for x in strs[0]]
        text = ""
        print(characters)
        for char in characters:
            for string in strs:
                if text in string:
                    text = text + char
                else:
                    return text   
            

print(Solution().longestCommonPrefix(["flow", "floresan", "floor"]))
