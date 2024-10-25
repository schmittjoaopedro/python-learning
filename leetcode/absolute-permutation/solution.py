class Solution:
    def absolutePermutation(self, n, k):

        if k == 0:
            return list(range(1, n + 1))

        if n / k % 2 != 0:
            # Not possible to find absolute permutation
            return [-1]

        add = True
        perm = []
        for i in range(1, n + 1):
            if add:
                perm.append(i + k)
            else:
                perm.append(i - k)
            if i % k == 0:
                add = not add

        return perm
