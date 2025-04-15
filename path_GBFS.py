import heapq
import random

def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def generate_grid(num_nodes, num_obstacles):
    size = int(num_nodes ** 0.5)
    grid = [[0 for _ in range(size)] for _ in range(size)]
    
    obstacles = set()
    while len(obstacles) < num_obstacles:
        x, y = random.randint(0, size - 1), random.randint(0, size - 1)
        if (x, y) != (0, 0) and (x, y) != (size-1, size-1):
            grid[x][y] = 1
            obstacles.add((x, y))
    
    return grid, (0, 0), (size - 1, size - 1)

def get_neighbors(pos, grid):
    x, y = pos
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    neighbors = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
            neighbors.append((nx, ny))
    return neighbors

def reconstruct_path(came_from, current):
    length = 0
    while current in came_from:
        current = came_from[current]
        length += 1
    return length

def greedy_bfs_path_length(grid, start, goal):
    open_list = [(manhattan(start, goal), start)]
    came_from = {}
    visited = set()

    while open_list:
        _, current = heapq.heappop(open_list)
        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            return reconstruct_path(came_from, goal)

        for neighbor in get_neighbors(current, grid):
            if neighbor not in visited and neighbor not in came_from:
                came_from[neighbor] = current
                heapq.heappush(open_list, (manhattan(neighbor, goal), neighbor))
    
    return -1  # path not found

# Jalankan eksperimen GBFS
experiments = [
    (5000, 10),
    (50000, 100),
    (500000, 1000),
    (5000000, 10000),
    (50000000, 100000)
]

for idx, (nodes, obstacles) in enumerate(experiments, 1):
    print(f"\n[GBFS] Experiment #{idx} - Nodes: {nodes}, Obstacles: {obstacles}")
    grid, start, goal = generate_grid(nodes, obstacles)
    path_length = greedy_bfs_path_length(grid, start, goal)
    print(f"Path length: {path_length}")