class Solution:
    def calculate(self, s: str) -> int:
        sign = "+"
        stack = []
        i = 0
        res = 0
        n = len(s)
        while i < n:
            ch = s[i]
            if ch.isdigit():
                cur_val = 0
                while i < n and s[i].isdigit():
                    cur_val = cur_val*10+int(s[i])
                    i += 1
                i -= 1
                if sign == "+":
                    stack.append(cur_val)
                elif sign == "-":
                    stack.append(-cur_val)
                elif sign == "*":
                    val = stack.pop()
                    stack.append(val*cur_val)
                elif sign == "/":
                    val = stack.pop()
                    stack.append(int(val/cur_val))
            elif ch != " ":
                sign = ch
            i += 1
        while len(stack) > 0:
            res += stack.pop()
        return res