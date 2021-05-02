import collections


def is_isogram(string: str) -> bool:

    no_space_hyphens = string.replace('-', '').replace(' ', '').upper()
    no_repeat = True

    d = collections.defaultdict(int)
    for c in no_space_hyphens:
        d[c] += 1

    for item in d:
        if d[item] > 1:
            no_repeat = False

    return no_repeat
