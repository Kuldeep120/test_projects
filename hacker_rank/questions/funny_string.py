def is_funny(s):
    re = s[::-1]
    for i in range(len(s)-1):
        if abs(ord(re[i])-ord(re[i+1])) != abs(ord(s[i])-ord(s[i+1])): return "Not Funny"
    return 'Funny'

def run():
    print(is_funny())