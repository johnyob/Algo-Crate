# BUCKET-SORT(A)
# Sorts the array A containing values that are distributed over the interval [0, 1) given by some given uniform distribution
# X. The interval [0, 1) is divided into n-equal sized buckets (or subintervals). Since the inputs are unformaly distributed,
# bucket sizes should be small. We then simply sort each bucket (using a stable sorting algorithm)

# Analysis:
# Time Complexity: O(n)

# Chapter 8.4, Page 201

from algo_crate.sorting.quicksort import quicksort

from math import floor


def bucket_sort(a):

    n = len(a)
    b = [[]] * n

    for i in range(n):
        j = floor(n * a[i])
        b[j].append(a[i])

    c = []
    for x in b:
        quicksort(x, 0, len(x) - 1)
        c += x

    return c
