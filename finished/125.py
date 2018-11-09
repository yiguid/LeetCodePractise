class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                if not s[l].isalnum():
                    l += 1
                elif not s[r].isalnum():
                    r -= 1
                else:
                    return False
        return True

    #use too many libs
    def isPalindrome2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parsed = re.sub(r'[^0-9a-zA-Z]', '', s).lower()
        return parsed == parsed[::-1]



s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("race a car"))