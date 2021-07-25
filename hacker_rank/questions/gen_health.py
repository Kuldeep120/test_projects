from collections import defaultdict
def find_max_min(genes, health, strands):
    min_h, max_h = -1, -1
    max_gen = max([len(x) for x in genes])
    gmap = defaultdict(lambda: 0)

    for strand in strands:

        first = strand[0]

        last = strand[1]

        d = strand[2]
        health_amount = 0
        for i, item in enumerate(genes[first: last+1]):
            gmap[item] += health[i+first]
        for i, a in enumerate(d):
            sub = a
            for hi, gene in enumerate(genes[first: last+1]):
                if sub == gene:
                    health_amount += health[hi+first]

            for j, b in enumerate(d[i + 1: i+max_gen]):
                sub = "{}{}".format(sub, b)
                for hi, gene in enumerate(genes[first: last+1]):
                    if sub == gene:
                        health_amount += health[hi+first]

        min_h = min(min_h, health_amount) if min_h>= 0 else health_amount
        max_h = max(max_h, health_amount) if max_h>= 0 else health_amount
    print(min_h, max_h)

def find_max_min_optimized(genes, health, strands):
    min_h, max_h = -1, -1
    max_gen = max(list(map(len, genes)))
    for strand in strands:
        first = strand[0]
        last = strand[1]
        d = strand[2]
        health_amount = 0
        gmap = defaultdict(lambda: 0)
        for i, item in enumerate(genes[first: last+1]):
            gmap[item] += health[i+first]
        for i, a in len(d):
            sub = a
            health_amount += gmap.get(sub, 0)

            for j, b in enumerate(d[i + 1: i+max_gen]):
                sub = "{}{}".format(sub, b)
                health_amount += gmap.get(sub, 0)

        min_h = min(min_h, health_amount) if min_h>= 0 else health_amount
        max_h = max(max_h, health_amount) if max_h>= 0 else health_amount
    print(min_h, max_h)


def run():
    genes = ['a', 'b', 'c', 'aa', 'd', 'b']
    health = [1, 2, 3, 4, 5, 6]
    strands = [
        [1, 5, 'caaab'],
        [0, 4, 'xyz'],
        [2, 4, 'bcdybc'],
        ]
    gMap = defaultdict(lambda: [[], [0]])
    subs = set()
    for id, gene in enumerate(genes):
        gMap[gene][0].append(id)
        for j in range(1, min(len(gene), 500) + 1): subs.add(gene[:j])
    for v in gMap.values():
        for i, ix in enumerate(v[0]): v[1].append(v[1][i] + health[ix])
    find_max_min_optimized(genes,health, strands)
# 0 3063762714