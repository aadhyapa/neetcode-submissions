class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for curr, preq in prerequisites:
            graph[curr].append(preq)

        visited = set()
        visiting = [0] * numCourses

        def dfs(i):
            if i in visited:
                return True
            if visiting[i]:
                return False 
            
            res = True
            visiting[i] = 1
            for preq in graph[i]:
                res = res and dfs(preq)
            visiting[i] = 0
            visited.add(i)
            return res

        res = True
        for i in range(numCourses):
            if i not in visited:
                res = res and dfs(i)
            
        return res