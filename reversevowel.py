class Solution:
    def reverseVowels(self, s: str) -> str:
        left,right=0,len(s)-1
        v='aeiouAEIOU'
        s=list(s)
        while left<right:
            if s[left] not in v:
                left+=1
            if s[right] not in v:
                right-=1
            if s[right] in v and s[left] in v:
               s[left],s[right]=s[right],s[left]
               left+=1
               right-=1
        return ''.join(s)      
       
ab=Solution()
res=ab.reverseVowels("hello")
print(res)