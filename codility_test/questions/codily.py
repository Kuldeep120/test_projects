#
#
# def solution(l1):
#     smallest = 1
#     sorted_li = sorted(l1)
#     # positive =
#     # for i, a in enumerate(sorted_li):
#     #     if a>1:
#     #         positive = sorted_li[i:]
#     min_num = None
#     for i in range(1, 1000000):
#         if i in l1:
#             continue
#         else:
#             return i
#         # for a in l1:
#         #     if a == i:
#         #         min_num = i+1
#         #         break
#         #     else:
#         #         min_num = i
#
#     return min_num
#
#
#
#
# print(solution([-1,-2,-3,1,2,3,4,5]))


# import re
# def solution(str1):
#     splited = re.split('\.|!|\?', str1)
#     print(splited)
#     max_n = 0
#     for sen in splited:
#         print(sen.split(' '))
#         max_n = max(max_n, len(list(filter(lambda x: x != '', sen.split(' ')))))
#         print(max_n)
#
#     return max_n
# print(solution('Forget  CVs..Save time . x    x'))
# from collections import defaultdict
#
# def solution(A, D):
#     # write your code in Python 3.6
#     months = defaultdict(lambda: [0, 0])
#     amount_total = 0
#     for i, amount in enumerate(A):
#         if amount < 0:
#             months[D[i].split('-')[1]][0] += 1
#             months[D[i].split('-')[1]][1] += amount
#
#         amount_total += amount
#     charged_months = (12 - len([x for x in months.values() if x[0] >= 3 and abs(x[1]) >= 100]))
#     amount_total = amount_total - (5 * charged_months)
#     return amount_total
#
# print(solution([100, 100, 40, -10, -20, -70], ['2020-01-01', '2020-02-01', '2020-02-11', '2020-02-16', '2020-02-05', '2020-02-08']))
# # print(solution([100, 100, 70, -10, -20, -70], ['2020-01-01', '2020-02-01', '2020-02-11', '2020-02-16', '2020-02-05', '2020-02-08']))

# import io
# import csv
# from collections import defaultdict
# # import pandas as pd
# def solution(S):
#     # write your code in Python 3.6
#     S = "name,city,date\n"+S
#     data = io.StringIO(S)
#     dict_reader=csv.DictReader(data)
#     max_num = defaultdict(lambda: 0)
#     filenames = list(dict_reader)
#     return_names = []
#     for line in list(dict_reader):
#         max_num[line['city']]+=1
#     for item in filenames:
#         if return_names:
#             return_names.append( str(item['city'].zfill(max_num[item['city']])))
#     return max_num
# print(solution("""a,b,c
# 3,4,5
# 3,4,1"""))

def timeConversion(s):
    # Write your code here
    am_or_pm = s[-2:]
    time = s[:-2]
    time_array = time.split(':')
    if (time_array[0] == '12' and am_or_pm == 'PM') or (am_or_pm == 'AM' and time_array[0] == '12'):
        time_array[0] = str((int(time_array[0]) + 12) % 24).zfill(2)

    return ':'.join(time_array)
