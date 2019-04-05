from copy import copy


def dijkstra(graph, start, end):
    if start == end:
        return "0"
    if start not in graph.keys():
        return "There is no start node called " + str(start) + "."
    if end not in graph.keys():
        return "There is no terminal node called " + str(end) + "."
    distance = {}
    order = {}
    for i in graph.keys():
        if i == start: 
            distance[i] = 0
        else: 
            distance[i] = float("inf")
    dist2 = copy(distance)
    while len(dist2) > 0:
        min_vertex = min(dist2, key = dist2.get)
        for i in graph[min_vertex]:
            if distance[i] > (distance[min_vertex] + graph[min_vertex][i]):
                distance[i] = distance[min_vertex] + graph[min_vertex][i]
                dist2[i] = distance[min_vertex] + graph[min_vertex][i]
                order[i] = min_vertex
        del dist2[min_vertex]
    temp = copy(end)
    rpath = []
    path = []
    while 1:
        rpath.append(temp)
        if temp in graph.keys():
            temp = order[temp]
        else:
            return "There is no path from " + str(start) + " to " + str(end) + "."
        if temp == start:
            rpath.append(temp)
            break
    for j in range(len(rpath)-1,-1,-1):
        path.append(rpath[j])
    return "The shortest path from " + str(start) + " to " + str(end) + " is " + str(path) + ". Minimum distance is " + str(distance[end]) + "."

