class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        terms = path.split("/")
        for t in terms:
            if t == '..':
                if stack != []:
                    stack.pop()
            elif t != '' and t != '.':
                stack.append(t)
        if stack == []:
            return '/'
        ans = ''
        for t in stack:
            ans += '/' + t
        return ans

        

s = Solution()

print(s.simplifyPath("/home/"))
print(s.simplifyPath("/a/./b/../../c/"))
print(s.simplifyPath("/a/../../b/../c//.//"))
print(s.simplifyPath("/a//b////c/d//././/.."))