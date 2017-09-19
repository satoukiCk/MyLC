# 70.Climbing Stairs
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        dic = [-1 for x in range(n)]
        dic[0],dic[1] = 1,2
        return self.helper(n-1,dic)

    def helper(self,n,dic):
        if dic[n] < 0:
            dic[n] =  self.helper(n-1,dic) + self.helper(n-2,dic)
        return dic[n]