from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        ix_ratings = [(n, i) for i, n in enumerate(ratings)]
        ix_ratings.sort()

        outputs = [0] * len(ratings)
        for item in ix_ratings:
            n, i = item
            cap = 1
            if i > 0 and ratings[i - 1] < n:
                cap = outputs[i - 1] + 1
            if i < len(ratings) - 1 and ratings[i + 1] < n:
                cap = max(cap, outputs[i + 1] + 1)

            outputs[i] = cap

        return sum(outputs)
