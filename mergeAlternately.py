class Solution:
    def __init__(self,word1,word2):
        self.word1 = word1
        self.word2 = word2
        
    def mergeAlternately(self):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = []
        i = 0
        while i < len(self.word1) or i < len(self.word2):
            if i < len(self.word1):
                result.append(self.word1[i])
            if i < len(self.word2):
                result.append(self.word2[i])
            i += 1
        return ''.join(result)
        
sol=Solution("anu","grah")  
print(sol.mergeAlternately())