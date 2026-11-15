class CountSquares:

    def __init__(self):
        self.points_map = collections.defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        self.points_map[tuple(point)] += 1
        

    def count(self, point: List[int]) -> int:
        total = 0
        x1, y1 = point
        for (x2, y2), count_diag in self.points_map.items():
            if abs(x2 - x1) == abs(y2 - y1) and abs(x2 - x1) > 0:
                total += count_diag * self.points_map.get((x1, y2), 0) * self.points_map.get((x2, y1), 0)
        return total