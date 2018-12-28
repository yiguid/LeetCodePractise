class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"

        ret = "1"
        i = 1
        while i < n:
            ans = ""
            cur = ""
            count = 0
            for c in ret:
                if cur == "" or cur == c:
                    cur = c
                    count += 1
                elif cur != "" and cur != c:
                    ans += str(count) + cur
                    cur = c
                    count = 1
            ans += str(count) + cur
            ret = ans
            i += 1
        return ret


s = Solution()
print(s.countAndSay(10))
