from algo_crate.util import DEFAULT_CMP


def bubble_sort(a, cmp=DEFAULT_CMP):

    for i in range(0, len(a)):

        for j in range(i + 1, len(a)):

            if cmp(a[i], a[j]) > 0:
                a[i], a[j] = a[j], a[i]