class Solution:
    res = []
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def backtrace(s, ans):
            if s == '':
                self.res.append(ans[:]) #deep copy, important 1
                return #return, important 2
            for i in range(len(s)):
                part = s[:i + 1]
                if part == part[::-1]:
                    ans.append(part)
                    backtrace(s[i + 1:], ans)
                    ans.pop() #pop up, important 3

        if len(s) == 0:
            return []
        self.res = []
        backtrace(s, [])
        return self.res

        

s = Solution()
print(s.partition("aab"))
print(s.partition("abc"))
# print(s.partition("aaaaaab"))
print(s.partition("aabcba"))