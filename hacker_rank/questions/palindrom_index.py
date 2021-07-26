def palindrome_index(s):
    # Write your code here
    if s == s[::-1]:
        return -1
    ri = None
    ir, il = len(s) - 1, 0
    while ir != il:
        if s[il] == s[ir]:
            ir -= 1
            il += 1
        elif s[:il] + s[il + 1:] == (s[:il] + s[il + 1:])[::-1]:
            if ri:
                return -1
            else:
                return il
                ri == il
                il += 1
        elif s[:ir] + s[ir + 1:] == (s[:ir] + s[ir + 1:])[::-1]:
            if ri:
                return -1
            else:
                return ir
                ri == ir
                ir -= 1

        else:
            return -1

    return ir

def run():
    print(palindrome_index('hgygsvlfcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcwflvsgygh'))
    print(palindrome_index('baa'))
    print(palindrome_index('aaa'))