from .parse_l import parse_l


def reverse_bwt(l):
    f, tally = parse_l(l)  # call with step=1 so that tally could be read like a regular list

    i = 0
    t = '$'

    while l[i] != '$':
        c = l[i]
        t = c + t
        i = f[c] + tally[i][c] - 1

    return t
