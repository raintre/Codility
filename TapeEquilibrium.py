#O(N)
def solution(A):
    # first -> head
    former = A[0]
    #except first -> tail
    latter = sum(A[1:])
    diff = abs(former - latter)
    #2nd element -> (last - 1) element
    for number in A[1:-1]:
        former += number
        latter -= number
        diff = min(diff , abs(former - latter))
    return diff    
A = [3, 1, 2, 4, 3]
print(solution(A))
