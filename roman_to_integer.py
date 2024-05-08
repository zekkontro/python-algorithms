roman_numbers = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
            "IV" : 4,
            "IX" : 9,
            "XL" : 40,
            "XC" : 90,
            "CD" : 400,
            "CM" : 900,
        }

    
def calculateValue(strList : list[str]) -> int:
        value = 0
        for roman in strList:
            value = value + roman_numbers[roman]
        return value


class Solution:

    def romanToInt(self, s: str) -> int:
        words = list(s)
        parsed_romans = []
        if (len(words) > 1):
            for word in words:
                index = words.index(word)
                roman_value =  roman_numbers[word]
                if index < len(words )-1 :
                    next_roman = words[index+1]
                    next_roman_value = roman_numbers[words[index+1]]
                    if next_roman_value > roman_value:
                        parsed_romans.append(word+next_roman)
                        words.remove(next_roman)
                    else :
                        parsed_romans.append(word)
                else : 
                    parsed_romans.append(word)
            return calculateValue(parsed_romans)
        else: 
            return calculateValue(words)
                
        
print(Solution().romanToInt("LVIII"))