class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vovel=set("aeiou")
        currentcount=0
        max_count=0
        for i in range (k):
            if s[i] in vovel:
                currentcount+=1
                max_count=currentcount

        for i in range(k,len(s)):
            if s[i] in vovel:
                currentcount+=1
            if s[i-k] in vovel:
                currentcount-=1
            max_count=max(max_count,currentcount)
        return max_count
             

        
        