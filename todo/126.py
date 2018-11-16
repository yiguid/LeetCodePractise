class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        q = []
        q.append(beginWord)
        l = 0
        words = set(wordList)
        c = 'abcdefghijklmnopqrstvuwxyz'
        while q != []:
            k = len(q)
            while k > 0:
                k -= 1
                w = q.pop(0)
                if w == endWord:
                    return l + 1
                for i in range(len(w)):
                    newWord = list(w)
                    for j in range(len(c)):
                        newWord[i] = c[j]
                        s = ''.join(newWord)
                        if s != w and s in words:
                            q.append(s)
                            words.remove(s)
            l += 1
            #todo
            #todo
            #save path
        return 0

s = Solution()
print(s.findLadders("hit","cog",["hot","dot","dog","lot","log","cog"]))

print(s.findLadders("hit","cog",["hot","dot","dog","lot","log"]))

print(s.findLadders("a","c",["a","b","c"]))

print(s.findLadders("leet","code",["lest","leet","lose","code","lode","robe","lost"]))
