def solution(A, K):
	size = len(A)
	ans = []

	if K < 0 || 100 < K || size == 0:
		return ans
	if size == 1:
		return A
	for i in range(size):
		ans[(i + K) % size] = A[i]
	return ans

def solution(A, K):

	array = A

	if array == []:
		return A

	for _ in range(K):
		cache = A[-1]
		array.pop(-1)
		array.insert(0, cache)

	return array

def solution(A, K):
    return A[-K % len(A):] + A[:-K % len(A)]