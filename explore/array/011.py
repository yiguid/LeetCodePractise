class Solution:
    def maxAreaTakesTooLongTime(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxWater = 0
        for i in range(len(height) - 1):
        	for j in range(i + 1, len(height)):
        		maxWater = max(maxWater, abs(j - i) * min(height[i], height[j]))
        return maxWater

    def maxArea(self, height):
    	"""
        :type height: List[int]
        :rtype: int
        """
        maxWater = 0
        i = 0
        j = len(height) - 1
        while(i < j):
        	width = j - i
        	if(height[i] < height[j]):
        		minH = height[i]
        		i += 1
        	elif(height[i] > height[j]):
        		minH = height[j]
        		j -= 1
        	else:
        		minH = height[i]
        		i += 1
        		j -= 1
        	area = width * minH
        	if area > maxWater:
        		maxWater = area
        return maxWater



s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))



