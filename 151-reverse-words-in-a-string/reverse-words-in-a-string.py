class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        parts = s.split()
        parts.reverse()
        result= " ".join(parts)
        return result