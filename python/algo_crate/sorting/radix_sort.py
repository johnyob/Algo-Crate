# RADIX-SORT(A, d)
# Sorts an array of d digit integers by sucessively sorting the least significant digit first (using a stable sorting algorithm)
# This is repeated for each successive digit producing a sorted array

# Analysis:
# Time Complexity O(d(n + k)) for an O(n + k) stable sorting alg.
# Note: We use a modified version of counting sort.

# Chapter 8.3, Page 198


def get_digit(n, d):

    for i in range(d):
        n //= 10
    # ASSERT: n has been shifted d - 1 times => unit digit of n is dth digit of the original n.

    return n % 10


def radix_sort(a, d):

    for i in range(0, d):
        a = counting_sort(a, i)

    return a


def counting_sort(a, i):

    b = [0] * len(a)
    c = [0] * 10

    for x in a:
        c[get_digit(x, i)] += 1

    for j in range(1, 10):
        c[j] += c[j - 1]

    # for i <- a.length - 1 downto 0 do
    for j in range(len(a) - 1, -1, -1):
        b[c[get_digit(a[j], i)] - 1] = a[j]
        c[get_digit(a[j], i)] -= 1

    return b

