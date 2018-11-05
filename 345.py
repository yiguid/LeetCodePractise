class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        j = len(s) - 1
        ret = ''
        a = ['a','i','u','e','o','A','I','U','E','O']
        for i in range(len(s)):
            if not s[i] in a:
                ret += s[i]
            else:
                while not s[j] in a:
                    j -= 1
                ret += s[j]
                j -= 1
        return ret

    def reverseVowels2(self, s):
        # convert to list and process, then convert back to string
        s = list(s)
        vows = set('aeiouAEIOU')
        l, r = 0, len(s) - 1
        while l <= r:
            while l <= r and s[l] not in vows: 
                l += 1
            while l <= r and s[r] not in vows: 
                r -= 1
            if l > r: 
                break
            s[l], s[r] = s[r], s[l]
            l, r = l + 1, r - 1
        return ''.join(s)

        


s = Solution()
print(s.reverseVowels("hello"))
print(s.reverseVowels("leetcode"))