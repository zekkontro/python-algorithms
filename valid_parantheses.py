
# () {} []
class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '[]'in s or '{}' in s:
            s = s.replace('()','').replace('[]','').replace('{}','')
        return False if len(s) !=0 else True
                    
                    
test_input = input("Enter a text: ")
print("Response: " + str(Solution().isValid(test_input)))
                
                
            
         