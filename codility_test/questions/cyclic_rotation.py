
def solution(A, K):
    # write your code in Python 3.6
    K = (K % len(A)) if len(A) else 0
    return A[-K:]+A[:len(A)-len(A[-K:])]

def run():
    # print(solution([], 20))
    print(solution([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15], 20))
    print(solution([1, 2, 3, 4],20))