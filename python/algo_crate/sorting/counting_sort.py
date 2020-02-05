# COUNTING-SORT(A, B, k)
# Sorts the array A by for all x in [0,k], count the numbers less than x in A. These numbers can then be used as indices
# into the sorted array B

# Analysis:
# Time Complexity: O(n + k)

# Chapter 8.2, Page 195


def counting_sort(a, k):

    # PRECONDITION: for all x in a. x in [0, k]
    # POSTCONDITION: The returned array b has a length of len(a), containing all the same elements as a, but in a sorted
    #                order.

    # Initialize the output and count arrays
    b = [0] * len(a)
    c = [0] * (k + 1)

    for x in a:
        c[x] += 1
    # ASSERT: c[x] now contains the number of elements equal to x.

    for i in range(1, k + 1):
        c[i] += c[i - 1]
    # ASSERT: c[x] now contains the number of elements less than or equal to x.

    # for i <- a.length - 1 downto 0 do
    for i in range(len(a) - 1, -1, -1):
        b[c[a[i]] - 1] = a[i]
        c[a[i]] -= 1

    return b



