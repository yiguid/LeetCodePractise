class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        queue = []
        for s in tokens:
            if s == '+':
                t = int(queue.pop())
                res = int(queue.pop()) + t
                queue.append(res)
            elif s == '-':
                t = int(queue.pop())
                res = int(queue.pop()) - t
                queue.append(res)
            elif s == '*':
                t = int(queue.pop())
                res = int(queue.pop()) * t
                queue.append(res)
            elif s == '/':
                t = int(queue.pop())
                res = int(int(queue.pop()) * 1.0 / t)
                queue.append(res)
            else:
                queue.append(s)
        return int(queue[0])



s = Solution()

print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))