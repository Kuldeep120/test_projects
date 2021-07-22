def pangrams(s):
    # Write your code here
    alpha = set()
    for i in s:
        if i == ' ': continue
        alpha.add(i.lower())
        if len(alpha) == 26:
            return 'pangram'

    return 'not pangram'