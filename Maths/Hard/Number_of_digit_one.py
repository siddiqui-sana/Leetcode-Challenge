class Solution:
    def countDigitOne(self, n: int) -> int:
        # No. of 1s at one's Position (n/10) + (n%10!=0)
        # No. of 1s at ten's Position (n/1OO)*1O + min(max(n%1OO - 10 +1,0),10)
        # No. of 1s at Hundread's Dosition (n/1OOO)*1OO + min(max(n%1OOO - 100  +1,0),100)
        res = 0
        cur = 1
        while cur <= n:
            res += ((n//(cur*10))*cur)+min(max(n % (cur*10)-cur+1, 0), cur)
            cur *= 10
        return res