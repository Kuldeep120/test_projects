def append_and_delete(s, t, k):
    # Write your code here
    s = list(s)
    t = list(t)
    mov = 0
    match = 0
    for i in range(min(len(t), len(s))):
        if s[i] == t[i]:
            match = i + 1
        else:
            break
    # delete till
    while mov < k:
        if len(s) == match:
            break
        else:
            del s[-1]
            mov += 1
    while mov < k:
        if s == t:
            break
        else:
            s.append(t[match])
            match += 1
            mov += 1
    if s == t:
        print('Yes')
        return "Yes"
    else:
        print('No')
        return "No"



