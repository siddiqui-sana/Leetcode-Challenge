class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        res = [0]*(len(num1)+len(num2))
        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                res[i+j+1] += (ord(num1[i])-ord('0'))*(ord(num2[j])-ord('0'))
                res[i+j] += res[i+j+1]//10
                res[i+j+1] = res[i+j+1] % 10
        i = 0
        out = ""
        while res[i] == 0:
            i += 1
        while i < len(res):
            out += str(res[i])
            i += 1
        return out