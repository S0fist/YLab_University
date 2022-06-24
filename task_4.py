import itertools


def bananas(s):
    result = set()
    for compound in itertools.combinations(range(len(s)), len(s) - 6):
        a = list(s)
        for i in compound:
            a[i] = "-"
        amalgamation = "".join(a)
        if amalgamation.replace("-", " ") == "banana":
            result.add(amalgamation)

    return result
