class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # AB = A×26¹＋B ＝ 1×26¹＋2
        # ABCD＝A×26³＋B×26²＋C×26¹＋D＝1×26³＋2×26²＋3×26¹＋4
        sheet = [chr(i) for i in range(ord("A"), ord("Z")+1)]
        res = []
        while columnNumber > 0:
            res.append(sheet[(columnNumber-1) % 26])
            columnNumber = (columnNumber-1)//26
        return "".join(res[::-1])