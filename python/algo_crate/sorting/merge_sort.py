# MERGE-SORT(A, l, r)
# Sorts the subarray a[l:r + 1] using the following divide-and-conquer approach:
# Divide: Divide the n-element array to be sorted into two subarrays of n/2 elements
# Conquer: Sort the two subarrays recursively using merge sort
# Combine: Merge the two sorted arrays to produce the sorted answer.

# Analysis:
# O(n lg n)

# Chapter 2.3, Page 34

from math import floor

from algo_crate.util import DEFAULT_CMP


def merge(a, l, m, r, cmp=DEFAULT_CMP):

    # PRECONDITION: The two subarrays a[l:m+1] and a[m+1:r+1] are sorted and contain n_l and n_r elements respectively

    # POSTCONDITION: The array a[l:r+1] is sorted and contains the same (r + 1) - l = n_l + n_r elements the two subarrays
    # contained initially.

    # Calculate the sizes of the two subarrays
    n_l = (m + 1) - l
    n_r = r - m

    # Create temporary arrays. We could simply create a left temporary array and store the right one in the initial
    # array.
    a_l = a[l:m + 1]
    a_r = a[m + 1:r + 1]

    # Create the initial indices for the left and right subarrays and the main array
    i = j = 0
    k = l


    while i < n_l and j < n_r:
        # ASSERT: a_l and a_r aren't empty and the subarray a[l:k] is sorted

        if cmp(a_l[i], a_r[j]) < 0:
            a[k] = a_l[i]
            i += 1
        else:
            a[k] = a_r[j]
            j += 1
        k += 1

    # ASSERT: At least one of the subarrays a_l or a_r are empty.

    # Merge the remaining elements of a_l
    while i < n_l:
        a[k] = a_l[i]
        i += 1
        k += 1

    # Merge the remaining elements of a_r
    while j < n_r:
        a[k] = a_r[j]
        j += 1
        k += 1


def merge_sort(a, cmp=DEFAULT_CMP):

    # PRECONDITION: Array a contains len(a) comparable values.

    # POSTCONDITION: Array a contains the same values as before, but the are now sorted in the given order

    def merge_sort(a, l, r):
        # PRECONDITION: The subarray a[l:r + 1] contains (r + 1) - l comparable values.

        # POSTCONDITION: The subarray a[l:r + 1] contains the same values as before, but the are now sorted in the given order

        if l < r:
            # ASSERT: The subarray a[l:r + 1] has more than 1 element (non-trivial case)

            m = floor((l + r) / 2)

            # Divide and Conquer
            merge_sort(a, l, m)
            merge_sort(a, m + 1, r)

            # Combine
            merge(a, l, m, r, cmp)

    merge_sort(a, 0, len(a) - 1)



