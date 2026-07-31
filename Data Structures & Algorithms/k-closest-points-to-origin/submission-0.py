class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def eucledian(x, y):
            return math.sqrt(x**2 + y**2)

        
        points.sort(key = lambda point: eucledian(point[0], point[1]))

        return points[:k]