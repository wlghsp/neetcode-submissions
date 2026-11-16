class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        ans = []
        while q:
            curr = q.popleft()
            ans.append(curr)
            for nx in graph[curr]:
                indegree[nx] -= 1
                if indegree[nx] == 0:
                    q.append(nx)
        return ans if len(ans) == numCourses else []