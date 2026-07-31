class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for i in range(numCourses):
            graph[i] = set()
        for course, prereq in prerequisites:
            graph[course].add(prereq)

        visiting = set()
        visited = set()
        def dfs(courseNum, visiting, visited):
            if courseNum in visited:
                return True
            if courseNum in visiting:
                return False
                
            visiting.add(courseNum)

            verdict = True
            for num in graph[courseNum]:
                verdict = verdict and dfs(num, visiting, visited)
            
            visiting.remove(courseNum)
            visited.add(courseNum)

            return verdict

        res = True    
        for i in range(numCourses):
            res = res and dfs(i, visiting, visited)
        return res
    
        