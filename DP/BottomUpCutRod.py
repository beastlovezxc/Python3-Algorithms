# def BottomUpCutRod(p, n):
# 	r[0] = 0

# 	for i in range(1, n+1):
# 		q = -1
# 		for j in range(1, i+1):
# 			q = max(q, p[j] + r[i-j])
# 		r[i] = q
# 	return r[n]

# def ExtendedBottomUpCutRod(p, n):
# 	r[0] = 0

# 	for i in range(1, n+1):
# 		q = -1
# 		for j in range(i, i+1):
# 			if q <= p[j] + r[i-j]:
# 				q = p[j] + r[i-j]
# 				s[i] = j
# 		r[i] = q
# 	return r[n]

# s = [0]*100
# r = [0]*100
# p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

# for i in range(1, 110):
# 	print(BottomUpCutRod(p, i))
# 	# print(ExtendedBottomUpCutRod(p,i))


