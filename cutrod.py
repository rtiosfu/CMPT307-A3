import time

p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30, 32, 33, 33, 35, 37, 39, 40, 43,
45, 46, 48, 49, 51, 54, 56, 58, 61, 63, 65, 67]

t = [0]

def cutRod(p, n):
	if(n == 0):
		return 0
	q = float('-inf')
	for i in range(1, n + 1):
		q = max(q, p[i] + cutRod(p, n - i))
	return q

def memoizedCutRod(p,n):
	r = [float('-inf')] * (n + 1)
	return memoizedCutRodAux(p, n, r)

def memoizedCutRodAux(p, n, r):
	q = float('-inf')
	if r[n] >= 0:
		return r[n]
	if n == 0:
		q = 0
	for i in range(1, n + 1):
		q = max(q, p[i] + memoizedCutRodAux(p, n - i, r))
	r[n] = q
	return q

def bottomUpCutRod(p, n):
	r = [float('-inf')] * (n + 1)
	r[0] = 0
	for j in range(1, n + 1):
		q = float('-inf')
		for i in range(1, j + 1):
			q = max(q, p[i] + r[j - i])
		r[j] = q
	return r[n]

def perfMeasure(n):
	startTime = time.perf_counter_ns()
	print("Cutrod: ", cutRod(p, n))
	elapsedTime = (time.perf_counter_ns() - startTime) / 10**9
	print("Cutrod time: ", elapsedTime)

	startTime = time.perf_counter_ns()
	print("memo: ", memoizedCutRod(p, n))
	elapsedTime = (time.perf_counter_ns() - startTime) / 10**9
	print("memo time: ", elapsedTime)

	startTime = time.perf_counter_ns()
	print("bottom: ", bottomUpCutRod(p, n))
	elapsedTime = (time.perf_counter_ns() - startTime) / 10**9
	print("bottom time: ", elapsedTime)

perfMeasure(10) #replace the number with the size to be tested