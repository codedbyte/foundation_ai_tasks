from collections import deque

graph = {
    'Start': ['A', 'B'],
    'A': ['Start', 'C', 'D'],
    'B': ['Start', 'E'],
    'C': ['A'],
    'D': ['A', 'Goal'],
    'E': ['B', 'Goal'],
    'Goal': ['D', 'E']
}

# bfs function (using queue)
def bfs_search(graph, initial_node, goal_state):
    queue = deque([(initial_node, [initial_node])])
    visited = set()

    print("\n--- BFS Search ---")
    
    while queue:
        current_node, path = queue.popleft()
        
        # stop if we reach the goal
        if current_node == goal_state:
            print(f"Goal found! Path: {' -> '.join(path)}")
            return path
            
        if current_node not in visited:
            visited.add(current_node)
            
            # add neighbors to queue
            for neighbor in graph.get(current_node, []):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
                    
    return None

# dfs function (using stack)
def dfs_search(graph, initial_node, goal_state):
    stack = [(initial_node, [initial_node])]
    visited = set()

    print("\n--- DFS Search ---")
    
    while stack:
        current_node, path = stack.pop()
        
        # stop if we reach the goal
        if current_node == goal_state:
            print(f"Goal found! Path: {' -> '.join(path)}")
            return path
            
        if current_node not in visited:
            visited.add(current_node)
            
            # add neighbors to stack (reversed for left-to-right order)
            for neighbor in reversed(graph.get(current_node, [])):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

    return None

# run tests
if __name__ == "__main__":
    initial = 'Start'
    goal = 'Goal'
    
    bfs_result = bfs_search(graph, initial, goal)
    dfs_result = dfs_search(graph, initial, goal)