class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        n1 = len(str1)    
        n2 = len(str2)
        i = n2
        while i > 0:
            if n1 % i == 0 and n2 % i == 0:
                if str2[0:i] * (n2//i) == str2 and str2[0:i] * (n1//i) == str1:
                    return (str2[0:i])
            i -= 1
        return("")
