class HillClimbing:
    def __init__(self, graph, heuristics):
        self.graph = graph
        self.heuristics = heuristics
    
    def hill_climb(self, start, goal):
        current = start
        path = [current]
        visited = set([current])  # To keep track of visited nodes
        
        while current != goal:
            neighbors = self.graph.get(current, [])
            if not neighbors:
                print("No more neighbors to explore, stopping.")
                return None
            
            # Filter out already visited neighbors to prevent loops
            unvisited_neighbors = [node for node in neighbors if node not in visited]
            
            if not unvisited_neighbors:
                print(f"No unvisited neighbors left from {current}, stopping.")
                return None

            # Choose the neighbor with the lowest heuristic value
            next_node = min(unvisited_neighbors, key=lambda node: self.heuristics[node])

            # Check if the current node is better or not (to avoid getting stuck in local maxima)
            if self.heuristics[next_node] >= self.heuristics[current]:
                # If the best neighbor is not better than current, explore all unvisited neighbors
                unvisited_neighbors_sorted = sorted(unvisited_neighbors, key=lambda node: self.heuristics[node])
                
                for neighbor in unvisited_neighbors_sorted:
                    if self.heuristics[neighbor] < self.heuristics[current]:
                        next_node = neighbor
                        break
                else:
                    # No better neighbor found, stop
                    print(f"Reached a peak at {current}, no better neighbors.")
                    return None
            
            # Move to the next node
            current = next_node
            path.append(current)
            visited.add(current)
        
        return path

# Example graph and heuristic values
graph = {
    'A': ['B', 'S', 'D'],
    'B': ['C', 'S','A'],
    'C': ['B','E'],
    'D': ['A','G'],
    'E': ['C'],
    'S': ['A','B'],
    'G': ['D']
}

heuristics = {
    'A': 7,
    'B': 6,
    'C': 7,
    'D': 5,
    'E': 4,
    'S': 10,
    'G': 0
}

# Instantiate the algorithm
hc = HillClimbing(graph, heuristics)

# Perform the search from 'S' to 'G'
start_node = 'S'
goal_node = 'G'
path = hc.hill_climb(start_node, goal_node)

if path:
    print(f"Path to goal: {path}")
else:
    print("No path found.")
