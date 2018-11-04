
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




num = [0,1,2,3,4,5,6,7,8,9]

key = 5

print(binary_search(num,key))

print(binary_search(num,0))

print(binary_search(num,-1))

print(binary_search(num,9))

print(binary_search(num,10))
