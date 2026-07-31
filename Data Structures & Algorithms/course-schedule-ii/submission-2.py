class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        indegree = [0 for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        queue = deque()

        result = []
        
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            length = len(queue)
            for i in range(length):
                course = queue.popleft()
                result.append(course)
                for preq in graph[course]:
                    indegree[preq] -= 1
                    if indegree[preq] == 0:
                        queue.append(preq)

        if len(result) != numCourses:
            return []
            
        return result




        