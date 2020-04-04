def generate_suffix_array(t, step=1):
    elems = sorted([[t[i:], i, 0] for i in range(len(t))])  # use list instead of tuple

    i = 0

    for i in range(len(elems)):
        elems[i][2] = i

    elems = filter(lambda e: not (e[1] % step), elems)

    suffix_array = {}

    for e in elems:
        suffix_array[e[2]] = e[1]

    return suffix_array
