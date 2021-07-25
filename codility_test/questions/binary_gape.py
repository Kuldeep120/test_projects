# Binary Gap


# def binary_gape(numb):
#     binary_str = "{0:b}".format(numb)
#     print(binary_str)
#     already_one = False
#     zero_count = 0
#     gap = 0
#     for i, value in enumerate(binary_str):
#         if value == "1":
#             if already_one:
#                 gap = max(gap, zero_count)
#                 zero_count = 0
#             else:
#                 already_one = 1
#         else:
#             if already_one:
#                 zero_count += 1
#
#     return gap
#
#
# print(binary_gape(401))


def solution(N):
    n_bin = "{:b}".format(N)
    gape = -1
    max_gape = 0
    for i in n_bin:
        if i == '1':
            max_gape = max(gape, max_gape)
            gape = 0
        else:
            gape += 1
    return max_gape

def run():
    print(solution(12))