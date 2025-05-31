def read_graph(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        n = int(lines[0])
        graph = {i: [] for i in range(1, n + 1)}
        for line in lines[1:]:
            numbers = list(map(int, line.strip().split()))
            if numbers:
                u = numbers[0]
                graph[u] = numbers[1:]
    return graph, n


def dfs(graph, node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


def find_root(graph, n):
    for node in range(1, n + 1):
        visited = set()
        dfs(graph, node, visited)
        if len(visited) == n:
            return node
    return -1


def write_result(filename, result):
    with open(filename, "w") as f:
        f.write(str(result))


def main():
    graph, n = read_graph("input.txt")
    root = find_root(graph, n)
    write_result("output.txt", root)


if __name__ == "__main__":
    main()
