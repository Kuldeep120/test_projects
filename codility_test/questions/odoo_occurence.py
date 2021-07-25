# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    odd = {}
    already_occured = set()
    odd = set()
    for i in A:
        if i in already_occured:
           if i in odd:
               odd.remove(i)
        else:
            odd.add(i)
            already_occured.add(i)
    return odd.pop() if odd else 0