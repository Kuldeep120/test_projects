def anagram(s):
    # Write your code here
    if len(s) % 2 != 0:
        return -1

    if len(s) == 2:
        return 1
    count = 0
    for i in s[:int(len(s) / 2)]:
        if i not in s[int(len(s) / 2):]:
            count += 1
    return count
from collections import defaultdict, Counter
def anagram_v2(s):
    if len(s) % 2 != 0:
        return -1

    if len(s) == 2:
        return 1
    count = 0
    part_1 = defaultdict(lambda: 0)
    part_2 = defaultdict(lambda: 0)
    for ch in s[:int(len(s) / 2)]:
        part_1[ch] += 1
    for ch in s[int(len(s) / 2):]:
        part_2[ch] += 1
    # a = Counter(s[:int(len(s) / 2)])
    # b = Counter(s[int(len(s) / 2):])

    for k, v in part_1.items():
        if k in part_2:
            part_2[k]-=v
    return sum(filter(lambda x: x>=0, part_2.values()))



def run():
    print(anagram_v2('xaxbbbxx'))
    # print(anagram_v2('fdhlvosfpafhalll'))
    # print(anagram_v2('mvdalvkiopaufl'))