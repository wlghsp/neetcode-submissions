class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        completed = 0
        while q:
            curr = q.popleft()
            completed += 1
            for nx in graph[curr]:
                indegree[nx] -= 1
                if indegree[nx] == 0:
                    q.append(nx)
        return completed == numCourses