class Solution:
    def checkSegment(self, arr, start, end):
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                return False
        return True

    def almostSorted(self, arr):
        n = len(arr)
        mask1 = [True] * n
        mask2 = [True] * n
        for i in range(n):
            if i < n - 1:
                mask1[i] = arr[i] < arr[i + 1]
            if i > 0:
                mask2[i] = arr[i - 1] < arr[i]

        mask = [True] * n
        for i in range(n):
            mask[i] = mask1[i] and mask2[i]

        faults = []
        for i in range(n):
            if not mask[i]:
                faults.append(i)

        gaps = 0
        for i in range(len(faults) - 1):
            if faults[i + 1] - faults[i] > 1:
                gaps += 1
            if gaps > 1:
                return "no"

        # Check swaps
        swap = False
        if len(faults) <= 4:
            n1, n2 = 0, 0
            for i in range(len(faults) - 1):
                for j in range(i + 1, len(faults)):
                    arr[faults[i]], arr[faults[j]] = arr[faults[j]], arr[faults[i]]
                    swap = self.checkSegment(arr, max(0, faults[i] - 1), min(n - 1, faults[j] + 1))
                    arr[faults[i]], arr[faults[j]] = arr[faults[j]], arr[faults[i]]
                    if swap:
                        n1, n2 = faults[i], faults[j]
                        break
                if swap:
                    break
            if swap:
                return f"yes, swap {n1 + 1} {n2 + 1}"

        # Check reverse
        reverse = False
        if not swap:
            n1, n2 = -1, -1
            arr2 = list(reversed(arr[faults[0]:faults[-1] + 1]))
            if self.checkSegment(arr2, 0, len(arr2) - 1):
                if faults[0] > 0:
                    if arr[faults[0] - 1] < arr2[0]:
                        n1 = faults[0]
                else:
                    n1 = 0

                if faults[-1] < n - 1:
                    if arr2[-1] < arr[faults[-1] + 1]:
                        n2 = faults[-1]
                else:
                    n2 = n - 1

                if n1 != -1 and n2 != -1:
                    reverse = True

            if reverse:
                return f"yes, reverse {n1 + 1} {n2 + 1}"

        if not swap and not reverse:
            return "no"
