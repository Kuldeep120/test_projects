def non_repeating_character(strParam):
    char = set()
    no = {}
    for i, v in enumerate(strParam):
        if v in no:
            no[v] = i
            char.add(v)
        elif v in char:
            if v in no:
                del no[v]
            else:
                no[v] = i
        else:
            no[v] = i
            char.add(v)
    # code goes here
    return min(no, key=lambda k: no[k])


def run():
    print(non_repeating_character('abcdef'))
