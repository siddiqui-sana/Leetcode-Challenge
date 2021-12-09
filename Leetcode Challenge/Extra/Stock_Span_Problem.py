class Solution:
    def calculateSpan(self, price, n):
        # Approach 1:
        hey = [1]*len(price)
        for i in range(1, len(price)):
            a = i
            while price[i] > price[a-1] and a > 0:
                hey[i] += 1
                a -= 1
        return hey

        # Approach 2:
        stck = []
        res = []
        span = []
        for i in range(0, n):
            while len(stck) != 0 and stck[-1][0] <= price[i]:
                stck.pop()
            if len(stck) == 0:
                res.append(-1)
            else:
                res.append(stck[-1][1])
            stck.append((price[i], i))
        for i in range(0, n):
            span.append(i-stck[i])
        return span
