from .bwt import bwt
from .generate_suffix_array import generate_suffix_array
from .parse_l import parse_l
from .lookup_suffix_array import lookup_suffix_array
from .lookup_tally import lookup_tally


def search(t, p, suffix_array_step=1, tally_step=1):
    l = bwt(t + '$')
    suffix_array = generate_suffix_array(t + '$', suffix_array_step)
    f, tally = parse_l(l, tally_step)

    occurences = []

    p_upper = len(p)

    f_list = list(f)
    range_c = p[p_upper - 1]
    range_c_i = f_list.index(range_c)

    range_min = f[range_c]
    range_max = f[f_list[range_c_i + 1]] - 1 if (range_c_i < len(f_list) - 1) else (len(l) - 1)  # if last c in f

    for p_lower in range(p_upper - 1, -1, -1):
        if p_lower == 0:
            for i in range(range_min, range_max + 1):
                occurences.append(lookup_suffix_array(suffix_array, i, l, tally, tally_step, f))
        else:
            c = p[p_lower - 1]

            tally_min = lookup_tally(tally, range_min - 1, c, tally_step, l)
            tally_max = lookup_tally(tally, range_max, c, tally_step, l)

            cnt = tally_max - tally_min

            if cnt == 0:
                break;

            range_min = f[c] + tally_min
            range_max = range_min + cnt - 1

    return occurences
