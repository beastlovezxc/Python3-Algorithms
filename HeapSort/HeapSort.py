#/usr/bin/python3
# -*- coding:utf-8 -*-
#构建最大堆
def MaxHeapify(array, i, n):
	j = i * 2 + 1
	while j < n:
		if j + 1 < n and array[j] < array[j+1]:
			j += 1
		if array[i] > array[j]:
			break
		array[i],array[j] = array[j],array[i]
		i = j
		j = i * 2 + 1
#创建堆
def BuildMaxHeap(array):
	size = len(array)
	for i in range(size//2-1, -1, -1):
		MaxHeapify(array,i,size)

#堆排序
def HeapSort(array):
	size = len(array)
	BuildMaxHeap(array)
	for i in range(size-1,0,-1):
		array[0], array[i] = array[i], array[0]
		MaxHeapify(array, 0, i)

a = [1,4,3,2,5,6,8,0]

HeapSort(a)
print(a)