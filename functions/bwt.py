from .generate_suffix_array import generate_suffix_array


def bwt(t):
    l = []

    suffix_array = generate_suffix_array(t)  # call with step=1 so it could be read like a regular list

    for i in suffix_array:
        if suffix_array[i] == 0:
            l.append('$')
        else:
            l.append(t[suffix_array[i] - 1])

    return ''.join(l)
