def parse_l(l, step=1):
    chars = sorted(set(l))
    chars.remove('$')

    c_cnt = {}
    for c in chars:
        c_cnt[c] = 0

    tally = []

    for i in range(len(l)):
        c = l[i]

        if c != '$':
            c_cnt[c] += 1

        if not (i % step):
            row = {}

            for c in chars:
                row[c] = c_cnt[c]

            tally.append(row)

    f = {}

    i = 0
    for c in chars:
        if i == 0:
            f[c] = 1
        else:
            f[c] = f[prev_c] + c_cnt[prev_c]

        i += 1
        prev_c = c

    return f, tally

