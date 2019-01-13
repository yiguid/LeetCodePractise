
def binary_search(num, key):
	start, end = 0, len(num) - 1
	while start <= end:
		mid = start + (end - start) / 2
		if key < num[mid]:
			end = mid - 1
		elif key > num[mid]:
			start = mid + 1
		else:
			return mid
	return -1

def binary_search_low(num, key):
	l, r = 0, len(num) - 1
	while l < r:
		mid = l + (r - l) // 2
		if key <= num[mid]:
			r = mid
		else:
			l = mid + 1
	return num[l]




num2 = [0,1,2,3,4,5,6,7,8,9]
num = [0,1,3,5,7,9]

key = 5

print(binary_search_low(num,key))

print(binary_search_low(num,0))

print(binary_search_low(num,-1))
print(binary_search_low(num,2))
print(binary_search_low(num,4))

print(binary_search_low(num,9))

print(binary_search_low(num,10))
