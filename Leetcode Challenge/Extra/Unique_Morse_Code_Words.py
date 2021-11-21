class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        out = []
        for word in words:
            res = [code[ord(char)-97] for char in word]
            out.append("".join(res))
        return len(set(out))
