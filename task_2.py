import task_1


def dfs(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_node(start):
        return []
    paths = []
    for node in graph.neighbors(start):
        if node not in path:
            newpaths = dfs(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def bfs(graph, start, end):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next_node in graph.neighbors(vertex):
            if next_node not in path:
                if next_node == end:
                    return path + [next_node]
                else:
                    queue.append((next_node, path + [next_node]))


def main():
    start_node = 'A'
    end_node = 'F'
    road_graph = task_1.create_graph()
    dfs_paths = dfs(road_graph, start_node, end_node)
    bfs_paths = bfs(road_graph, start_node, end_node)

    print(f"DFS paths from {start_node} to {end_node}: {dfs_paths}")
    print(f"BFS path from {start_node} to {end_node}: {bfs_paths}")


if __name__ == '__main__':
    main()
