class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L",
                 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
        roman = dict(reversed(list(roman.items())))
        res = ""
        for key, value in roman.items():
            if not num:
                break
            div = num//key
            res += div*value
            num %= key
        return res