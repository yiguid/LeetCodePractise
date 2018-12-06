class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        l = len(letters)
        for i in range(l):
            if letters[i] <= target:
                continue
            else:
                return letters[i]
        return letters[0]
        

s = Solution()
print(s.nextGreatestLetter(["c","f","j"], "a"))
print(s.nextGreatestLetter(["c","f","j"], "c"))
print(s.nextGreatestLetter(["c","f","j"], "d"))
print(s.nextGreatestLetter(["c","f","j"], "g"))
print(s.nextGreatestLetter(["c","f","j"], "j"))
print(s.nextGreatestLetter(["c","f","j"], "k"))