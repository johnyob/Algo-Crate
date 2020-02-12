# CUT-ROD(p, n)
# This algorithm returns the maximum possible profit produced from cutting a rod of length n. The
# prices p[0:n] that a rod of length i + 1 costs.
# The profit (or revenue) r_n = max_{1<=i<=n}(p_i + r_{n - i}) where r_0 = 0.

# Analysis:
# Top-Down Recursive (Non-Dynamic Programming Approach): O(2^n)
# Top-Down Memoized: O(n^2)
# Bottom-Up: O(n^2)

# Chapter 15.1, Page 360-370


def cut_rod(p, n):

    q = p[n - 1]
    for i in range(1, n):
        q = max(q, p[i - 1] + cut_rod(p, n - i))

    return q


def memoized_cut_rod(p, n):

    # Instantiate the "memo" array
    r = [-1] * n

    def cut_rod(n):

        # Has the sub-problem been previously calculated?
        if r[n - 1] >= 0: return r[n - 1]

        q = p[n - 1]
        for i in range(1, n):
            q = max(q, p[i - 1] + cut_rod(n - i))

        r[n - 1] = q
        return q

    return cut_rod(n)


def bottom_up_cut_rod(p, n):

    r = [0] * n
    s = [0] * n

    for j in range(n):
        q = p[j]
        for i in range(j):
            if q < p[i] + r[j - i - 1]:
                q = p[i] + r[j - i - 1]
                s[j] = 1 + s[j - i - 1]

        r[j] = q

    return r[n - 1], s[n - 1]


if __name__ == "__main__":
    p = [1,5,8,9,10,17,17,20,24,30]
    for i in range(1, 11):
        print(bottom_up_cut_rod(p, i))
