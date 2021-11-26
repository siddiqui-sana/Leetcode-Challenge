class Solution:
    def checkPerfectNumber(self, n: int) -> bool:
        res = []
        ans = []
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                if n // i == i:
                    res.append(i)
                else:
                    res.append(i)
                    ans.insert(0, n//i)
        res.extend(ans)
        res.pop()
        return sum(res) == n