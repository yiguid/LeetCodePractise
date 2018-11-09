class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # in python you can't do this
        # 'str' object does not support item assignment
        # i = 0
        # j = len(s) - 1
        # while i < j:
        #     s[i], s[j] = s[j], s[i]
        #     i += 1
        #     j -= 1
        return s[::-1]


s = Solution()
print(s.reverseString("A man, a plan, a canal: Panama"))
print(s.reverseString("hello"))