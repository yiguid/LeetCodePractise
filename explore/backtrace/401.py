class Solution:

    #small scale problem, list all probable situation
    def readBinaryWatch0(self, num):
        ans = []
        for h in range(12):
            for m in range(60):
                if (bin(h) + bin(m)).count('1') == num:
                    ans.append('$d:$02d' % (h, m))
        return ans

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        def toTime(ans):
            hour = 0
            minute = 0
            times = [1,2,4,8,1,2,4,8,16,32]
            for num in ans:
                if num < 4:
                    hour += times[num]
                else:
                    minute += times[num]
            if hour > 11 or minute > 59:
                return None
            if minute < 10:
                minute = "0" + str(minute)
            return str(hour) + ":" + str(minute)
        def dfs(num, start, ans):
            if len(ans) == num:
                #get time from ans
                timeStr = toTime(ans)
                if timeStr:
                    res.append(timeStr)
                return
            for j in range(start, 10):
                ans.append(j)
                dfs(num, j + 1, ans)
                ans.pop()
            return

        res = []
        if num < 0 or num > 8:
            return []
        if num == 0:
            return ["0:00"]
        dfs(num, 0, [])
        return res
        

s = Solution()
# print(s.readBinaryWatch(1))
print(s.readBinaryWatch(2))
# print(s.readBinaryWatch(3))
# print(s.readBinaryWatch(5))
# print(s.readBinaryWatch(6))
# print(s.readBinaryWatch(7))
# print(s.readBinaryWatch(8))