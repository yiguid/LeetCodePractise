class Solution:

    res = []
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def findValidIp(s, numOfDots, prefix):
            if numOfDots == 3 and int(s) >=0 and int(s) <= 255:
                if s[0] != '0' or len(s) == 1:
                    self.res.append(prefix + s)
                return
            l = len(s)
            if l < 4 - numOfDots or l > 3 * (4 - numOfDots):
                return 
            for i in range(3):
                if l >= 4 - numOfDots + i:
                    cur = int(s[:i + 1])
                    if (s[0] == '0' and len(s[:i + 1]) > 1) or cur > 255:
                        continue
                    findValidIp(s[i + 1:], numOfDots + 1, prefix + s[0:i + 1] + '.')

        if len(s) < 4 or len(s) > 12:
            return []
        self.res = []
        findValidIp(s, 0, '')
        return self.res


s = Solution()
print(s.restoreIpAddresses("25525511135"))
print(s.restoreIpAddresses("000"))
print(s.restoreIpAddresses("2333"))
print(s.restoreIpAddresses("44566"))
print(s.restoreIpAddresses("010010"))
print(s.restoreIpAddresses("0000"))