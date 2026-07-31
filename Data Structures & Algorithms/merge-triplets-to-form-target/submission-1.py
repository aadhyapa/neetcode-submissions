class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = 0, 0, 0
        for a, b, c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            x = x if x == target[0] else max(a, x)
            y = y if y == target[1] else max(b, y)
            z = z if z == target[2] else max(c, z)

        return [x, y, z] == target
