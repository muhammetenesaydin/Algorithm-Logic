class Solution(object):
    def gcdOfStrings(self, str1, str2):
        if str1+str2 != str2+str1:
            return ""
        index= math.gcd(len(str1),len(str2))

        return str1[:index]