# Robert Jerye


def connectedComponent(graph: dict, node: str):

    pass


# depth first search algo
def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")  # Process the node
            visited.add(node)
            # Push neighbors in reverse order to visit left-to-right
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)


from collections import deque

# bredth first search
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()  # Dequeue the first node
        print(node, end=" ")  # Process the node (e.g., print it)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


g = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A"], "D": ["B"], "E": ["F"], "F": ["A","E"]}

dfs(g, "A")
bfs(g, "A")
