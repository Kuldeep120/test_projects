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
print('sdfasdfasdfasdf')


# def append_and_delete(s, t, k):
#     # Write your code here
#     s = list(s)
#     t = list(t)
#     mov = 0
#     match = 0
#     for i in range(min(len(t), len(s))):
#         if s[i] == t[i]:
#             match = i + 1
#         else:
#             break
#     # delete till
#     while mov < k:
#         if len(s) == match:
#             break
#         else:
#             del s[-1]
#             mov += 1
#     while mov < k:
#         if s == t:
#             break
#         else:
#             s.append(t[match])
#             match += 1
#             mov += 1
#     if s == t:
#         print('Yes')
#         return "Yes"
#     else:
#         print('No')
#         return "No"
#
#
# append_and_delete('abcd', 'abcdert', 9)
# print('112121')

def birthdayCakeCandles(candles):
    # Write your code here
    max_height, count = 0, 0
    for candle in candles:
        if candle > max_height:
            max_height = candle
            count = 1
        elif candle == max_height:
            count += 1

    return count


def timeConversion(s):
    # Write your code here
    am_or_pm = s[-2:]
    time = s[:-2]
    time_array = time.split(':')
    if (time_array[0] == '12' and am_or_pm == 'PM') or (am_or_pm == 'AM' and time_array[0] == '12'):
        time_array[0] = str((int(time_array[0]) + 12) % 24).zfill(2)

    return ':'.join(time_array)

if __name__ == "__main__":
    print(birthdayCakeCandles([3, 2,1,3]))
    print(timeConversion('12:40:22AM'))


