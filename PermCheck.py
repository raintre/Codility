#O(N) or O(N * log(N))
def solution(A):
	# if 1, 2, ... , len(A) are in A -> return 1
    if set(A) == set(range(1 , 1 + len(A))):
        return 1
    else:
        return 0