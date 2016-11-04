def CountingSort(inputArray, k):
	size = len(inputArray)
	array = [0] * (k+1)
	outputArray = [0]*(size)
	for i in range(size):
		array[inputArray[i]] = array[inputArray[i]] + 1
	for i in range(1, k+1, 1):
		array[i] = array[i] + array[i-1]
	for i in range(size-1, -1, -1):
		outputArray[array[inputArray[i]]-1] = inputArray[i]
		array[inputArray[i]] = array[inputArray[i]] - 1
	return outputArray

inputArray = [3, 3, 5, 4, 4, 2, 2, 1, 0, 0, 4]

print(CountingSort(inputArray, max(inputArray)))