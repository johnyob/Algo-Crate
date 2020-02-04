# INSERTION-SORT(A)
# Sorts the given array by iteratively inserting each element into the sorted subarray of the array

# Analysis:
# Time Complexity: O(n^2)

# Chapter 2.1, Page 18

from algo_crate.util import DEFAULT_CMP


def insertion_sort(a, cmp=DEFAULT_CMP):
    # PRECONDITION: Array a contains len(a) comparable values.

    # POSTCONDITION: Array a contains the same values as before, but the are now sorted in the given order

    for j in range(1, len(a)):
        # ASSERT: The subarray a[:j] positions are already sorted.

        k = a[j]
        i = j - 1
        while i >= 0 and cmp(a[i], k) > 0:
            # ASSERT: For all x in the subarray a[i:j]. x > k
            a[i + 1] = a[i]
            i -= 1

        a[i + 1] = k



