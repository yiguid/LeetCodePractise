class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c in ["(","[","{"]:
                stack.append(c)
            elif c in [")","]","}"]:
                if len(stack) == 0:
                    return False
                tmp = stack.pop()
                if c == ')' and tmp != '(' or c == ']' and tmp != '[' or c == '}' and tmp != '{':
                    return False
        if len(stack) != 0:
            return False
        return True

s = Solution()
print(s.isValid(")"))
print(s.isValid("()[]{}"))
print(s.isValid("([)]"))
print(s.isValid("()"))
print(s.isValid("{[]}"))
