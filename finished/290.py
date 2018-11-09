class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        dic = {}
        arr = str.split(' ')
        if len(pattern) != len(arr):
            return False
        for i, p in enumerate(pattern):
            if p in dic:
                if dic[p] != arr[i]:
                    return False
            else:
                if not arr[i] in dic.values():
                    dic[p] = arr[i]
                else:
                    return False
        return True

s = Solution()

print(s.wordPattern("abba", "dog cat cat dog"))

print(s.wordPattern("abba", "dog cat cat fish"))

print(s.wordPattern("aaaa", "dog cat cat dog"))

print(s.wordPattern("abba", "dog dog dog dog"))

print(s.wordPattern("jquery", "jquery"))