class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[1 for i in range(m+n)] for j in range(n+m)]
        return self.ans(m-1,n-1,dp)
    def ans(self,m,n,dp):
        if m<0 or n<0 :
            return 0
        if m==0 or n==0:
            return 1
        if dp[m][n]==1:
            dp[m][n]=self.ans(m,n-1,dp)+self.ans(m-1,n,dp)
        return dp[m][n]
