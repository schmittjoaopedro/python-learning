from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        sorted_points = sorted(points, key=lambda x: (x[1], x[0]))

        arrows = 1
        rightMost = sorted_points[0][1]

        for balloon in sorted_points[1:]:
            if rightMost < balloon[0]:
                arrows += 1
                rightMost = balloon[1]

        return arrows
