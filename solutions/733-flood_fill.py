# ID: 733
# Title: Flood Fill
# Link: https://leetcode.com/problems/flood-fill/
# Difficulty: Easy
# Tags: Array, Depth-First Search, Breadth-First Search, Matrix
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        prev_color = image[sr][sc]
        if prev_color == color:
            return image
        image[sr][sc] = color
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = sr + dr, sc + dc
            if 0 <= nr < len(image) and 0 <= nc < len(image[0]) and image[nr][nc] == prev_color:
                self.floodFill(image, nr, nc, color)
        return image

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        prev_color = image[sr][sc]
        if prev_color == color:
            return image
        s = [(sr, sc)]
        while s:
            r, c = s.pop()
            if image[r][c] == color:
                continue
            image[r][c] = color
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(image) and 0 <= nc < len(image[0]) and image[nr][nc] == prev_color:
                    s.append((nr, nc))
        return image


if __name__ == "__main__":
    print(Solution().floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
