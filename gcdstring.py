import math
class Greatest(object):
     def gcdOfStrings(self,str1,str2):
         if(str1+str2 == str2+str1):
            gcd=math.gcd(len(str1),len(str2))
            return str1[:gcd]
         else:
            return ''

sol=Greatest()
result=sol.gcdOfStrings("ABABAB","AB")
print(result)                    