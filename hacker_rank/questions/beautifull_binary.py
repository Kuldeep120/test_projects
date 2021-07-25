def beautiful_binary_string(b):
    # Write your code here
    steps = 0
    for i in range(len(b)):
        if i >= 2:
            if b[i - 2:i + 1] == '010':
                b = "{}{}{}".format(b[:i], 1, b[i:])
                steps += 1
    return steps


def run():
    print(beautiful_binary_string(
        '0100101010100010110100100110110100011100111110101001011001110111110000101011011111011001111100011101'))
