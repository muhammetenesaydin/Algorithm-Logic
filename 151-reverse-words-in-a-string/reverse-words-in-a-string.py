class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        parts = s.split()
        parts.reverse()
        return " ".join(parts)
        