from .lookup_tally import lookup_tally


def lookup_suffix_array(suffix_array, i, l, tally, step, f):
    steps = 0

    row = i

    while row not in suffix_array:
        steps += 1
        c = l[row]
        rank = lookup_tally(tally, row, c, step, l) - 1
        row = f[c] + rank

    return suffix_array[row] + steps
