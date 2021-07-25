def weighted_uniform_strings(s, queries):
    weights = set()
    ctr = 1
    for i, char in enumerate(s):
        weight = get_weight(char)
        ctr = ctr + 1 if (i + 1 != len(s) and s[i + 1] == s[i]) else 1
        weights.add(ctr * weight)

    query_result = []
    for k in queries:
        # if k == 1395:
        #     break
        if k in weights:
            query_result.append('Yes')
        else:
            query_result.append('No')
        pass
    return query_result


def get_weight(char):
    return ord(char) - ord('a') + 1

def run():
    with open('questions/input.txt','r') as fp:
        s = fp.readline()[:-1]
        fp.readline()
        queries = []
        while True:
            query = fp.readline()
            if not query:
                break
            integer = int(query[:-1] if '\n' in query else query)
            queries.append(integer)
    query_result = []
    with open('questions/output.txt', 'r') as fp:
        while True:
            query = fp.readline()
            if not query:
                break
            query = query[:-1] if '\n' in query else query
            query_result.append(query)

    process_result = qs.weighted_uniform_string.weighted_uniform_strings(s,queries)
    for i in range(len(process_result)):
        if process_result[i] == query_result[i]:
            print(True)
        else:
            print(False)
            break;

'6','1', '3', '12', '5', '9', '10'