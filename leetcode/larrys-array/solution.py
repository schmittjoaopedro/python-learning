class Solution:
    def rotate(self, array, start_idx):
        temp = array[start_idx]
        array[start_idx] = array[start_idx + 1]
        array[start_idx + 1] = array[start_idx + 2]
        array[start_idx + 2] = temp

    def larrysArray(self, A):
        count = 0
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                if A[i] > A[j]:
                    count += 1

        return "YES" if count % 2 == 0 else "NO"

    def larrysArrayBruteForce(self, A):
        n = len(A)
        i = 0

        while i < n - 2:
            # Skip already sorted elements
            while i < n - 1:
                if A[i] == i + 1:
                    i += 1
                else:
                    break

            # Find the position of num in A
            j = n - 1
            while A[j] != i + 1:
                j -= 1

            if (j - i) > 1:
                self.rotate(A, j - 2)
            elif (j - i) == 1 and j != n - 1:
                self.rotate(A, j - 1)

        return "YES" if A[n - 2] < A[n - 1] else "NO"
