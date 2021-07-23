"""
author: Kuldeep
challenge: from hackerranck
"""

import copy
def separate_numbers(s):
    # Write your code here
    ln, bt = "", ""
    first = ""
    is_bt = "NO"
    half = int(len(s)/2)
    for i in s[:half]:
        bt = "{}{}".format(first, i)
        ln = "{}{}".format(first, i)
        first = int(ln)
        while len(bt) < len(s):
            ln = str(int(ln) + 1)
            bt = "{}{}".format(bt, ln)

            pass
        if bt == s:
            is_bt = "YES"
            break

    print(is_bt, first if is_bt == "YES" else '')


def run():
    separate_numbers('13')
