class Solution:
    def Kcandies(self, candies, extraCandies):
        result = []
        maxc = max(candies)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxc:
                result.append(True)
            else:
                result.append(False)

        return result


solution_instance = Solution()


candies = [2, 3, 5, 1, 3]
extraCandies = 3


result = solution_instance.Kcandies(candies, extraCandies)

print(result)
