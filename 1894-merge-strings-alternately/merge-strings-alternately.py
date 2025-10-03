class Solution(object):
    def mergeAlternately(self,word1,word2 ):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        text=[]
        maxLength=max(len(word1),len(word2))
        for i in range (maxLength):
            if i<len(word1):
                text+=word1[i]
            if i<len(word2):
                text+=word2[i]
        return "".join(text)

        