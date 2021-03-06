def insert_sort(a):
	''' 将列表分成两个部分，从无序部分中拿出最前面的元素，往前面有序部分插入，与选择排序正好相反，可以类比生活中的打麻将'''
	n = len(a)
	for i in range(1, n):
		j = i
		# 对前半段进行插入，不大于右边的，不小于左边的
		# 类似冒泡的交换位置
	#	while j > 0:
	#		if a[j] < a[j-1]:
	#			a[j], a[j-1] = a[j-1], a[j]
	#			j -= 1
	#		else:
	#			break
		x = a[i] # 为防止覆盖a[i]，先保存它
		while j > 0 and a[j-1] > x:
			a[j] = a[j-1] # 逐步后移元素，确定插入元素
			j -= 1
		a[j] = x

def main():
	a = [1,0,2,9,3,8,7,4,6,5]
	insert_sort(a)
	for i in a:
		print(i, end = ' ')
	print('')


if __name__ == "__main__":
	main()
