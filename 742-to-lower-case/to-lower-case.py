class Solution:
    def toLowerCase(self, s: str) -> str:
        str = list(s)

        for i in range(len(str)):
            if str[i] >= 'A' and str[i] <= 'Z':
                str[i] = chr(ord(str[i]) + 32)

        return "".join(str)