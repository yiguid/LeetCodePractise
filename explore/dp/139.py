class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        dp = [False for i in range(n + 1)]
        dp[0] = True
        for i in range(n):
            if dp[i]:
                for j in wordDict:
                    l = len(j)
                    if i + l <= n and s[i: i + l] == j:
                        dp[i + l] = True
        return dp[n]
        

s = Solution()
print(s.wordBreak("leetcode",[]))
print(s.wordBreak("leetcode",["leet", "code"]))
print(s.wordBreak("applepenapple",["apple", "pen"]))
print(s.wordBreak("catsandog",["cats", "dog", "sand", "and", "cat"]))