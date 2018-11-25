import time
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        total = 1
        if len(digits) == 0:
            return []
        for num in digits:
            total *= len(dic[num])
        res = [""] * total
        numl = total
        for num in digits:
            k = 0
            ltimes = 0
            numl //= len(dic[num])
            numk = len(dic[num])
            for i in range(total):
                res[i] += dic[num][k]
                ltimes += 1
                if ltimes == numl:
                    ltimes = 0
                    k += 1
                if k == numk:
                    k = 0
        return res

    def letterCombinations2(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        store = [""]
        num = ["", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        for d in digits:
            tmpStore = []
            for val in store:
                for c in num[int(d)]:
                    tmpStore.append(val + c)
            store = tmpStore
        return store

    num = ["", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    res = []
    def lc(self, digits):
        def findCombination(digits, index, s):
            if index == len(digits):
                self.res.append(s)
                return 
            c = digits[index]
            letters = self.num[int(c)]
            for l in letters:
                findCombination(digits, index + 1, s + l)
        if digits == "":
            return []
        self.res = []
        findCombination(digits, 0, "")
        return self.res

s = Solution()

start = time.clock()
# print(s.letterCombinations("556"))
# print(s.letterCombinations("784"))
# print(s.letterCombinations("6248"))
print(s.lc("23"))
print(s.lc(""))
end = time.clock()
print(end - start)