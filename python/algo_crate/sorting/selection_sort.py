from algo_crate.util import DEFAULT_CMP


def min_index(a, cmp=DEFAULT_CMP):

    m, j = a[0], 0

    for i in range(1, len(a)):
        if cmp(a[i], m) < 0:
            m, j = a[i], i

    return j


def selection_sort(a, cmp=DEFAULT_CMP):

    for i in range(len(a)):
        j = min_index(a[i:], cmp)
        a[i], a[j] = a[j], a[i]

