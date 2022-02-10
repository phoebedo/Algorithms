#LC207m Time Limit Exceeded
#  find if there's a cycle in a directed graph.

import collections


def can_finish(numCourses, prerequisites):
    graph = collections.defaultdict(list)
    # create adjacency list 

    for edge in prerequisites:
        graph[edge[0]].append(edge[1])
    
    visited = set()

    def is_cycle(vertex):
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor in visited or is_cycle(neighbor):
                return True
        visited.remove(vertex)
        return False
    for i in range(numCourses):
        if is_cycle(i):
            return False 
    return True

