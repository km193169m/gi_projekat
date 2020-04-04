def lookup_tally(tally, i, c, step, l):
    nearest_i = int(round(i / step))

    if (nearest_i == len(tally)) and (i % step):
        nearest_i -= 1

    result = tally[nearest_i][c]

    if i % step:
        x = nearest_i * step
        y = i

        asc = x < y
        lower = (x if asc else y) + 1
        upper = (y if asc else x) + 1

        for l_c in l[lower:upper]:
            if l_c == c:
                result += (1 if asc else -1) * 1

    return result
