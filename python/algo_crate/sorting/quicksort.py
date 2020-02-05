# QUICKSORT(A, l, r)
# Sorts the subarray a[l:r + 1] using the following divide-and-conquer approach
# Divide: Partition the array a[l:r + 1] into two subarrays a[l:p] and a[p + 1:r + 1]
#         such that for all x in a[l:p]. x < a[p] and for all y in a[p + 1:r + 1]. a[p] <= y
# Conquer: Sort the two subarrays a[l:p] and a[p + 1:r + 1].
# Combine: The subarrays are sorted. No work is needed to combined them.

# Analysis:
# O(n log n)

# Chapter 7, Page 171

from algo_crate.util import DEFAULT_CMP


def quicksort(a, l, r, cmp=DEFAULT_CMP):
    # PRECONDITION: The subarray a[l:r + 1] contains (r + 1) - l comparable values.

    # POSTCONDITION: The subarray a[l:r + 1] contains the same values as before, but the are now sorted in the given order

    if l < r:
        # ASSERT: The subarray a[l:r + 1] has more than 1 element (non-trivial case)

        p = partition(a, l, r, cmp)
        quicksort(a, l, p - 1)
        quicksort(a, p + 1, r)




def partition(a, l, r, cmp=DEFAULT_CMP):
    # PRECONDITION: The subarray a[l:r + 1] contains (r + 1) - l comparable values.

    # POSTCONDITION: The subarray a[l:r + 1] contains the same values as before, but a[p] is in it's final position

    x = a[r]
    i = l - 1

    for j in range(l, r):
        # ASSERT: l <= k <= i => A[k] <= x
        #         i + 1 <= k <= j => A[k] > x
        #         k = r => A[k] = x

        if cmp(a[j], x) <= 0:
            i += 1
            a[i], a[j] = a[j], a[i]

    # Calculate p
    i += 1

    a[i], a[r] = a[r], a[i]
    return i
