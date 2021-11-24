class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # 1st Approach
        # Time: O(sqrt(n))
        # Space: O(n)
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
        if len(res) >= k:
            return res[k-1]
        return -1

        # 2nd Approach:
        # Time: O(n)
        # Space: O(1)
        for i in range(1, n+1):
            if n % i == 0:
                k -= 1
            if k == 0:
                return i
        return -1
