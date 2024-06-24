class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)  
        ans = []  
        i = n - 1 

        while i >= 0:
            if s[i] == ' ':
                i -= 1 
            else:
                temp = [' '] 
                j = i
                while j >= 0 and s[j] != ' ':
                    temp.append(s[j]) 
                    j -= 1
                ans.extend(reversed(temp))  
                i = j  
        ans.pop() 
        return ''.join(ans)
sol=Solution()
result=sol.reverseWords(" the sky is blue ")
print(result)  