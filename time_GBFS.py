import heapq
import time
from random import randint

# Arah pergerakan: atas, bawah, kiri, kanan
DIRS = [(-1,0), (1,0), (0,-1), (0,1)]

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def generate_grid(size, obstacles):
    grid = [[0 for _ in range(size)] for _ in range(size)]
    for _ in range(obstacles):
        x, y = randint(0, size-1), randint(0, size-1)
        grid[x][y] = 1
    return grid

def neighbors(grid, node):
    n = len(grid)
    result = []
    for dx, dy in DIRS:
        nx, ny = node[0]+dx, node[1]+dy
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
            result.append((nx, ny))
    return result

def gbfs(grid, start, goal):
    visited = set()
    heap = [(heuristic(start, goal), start)]
    while heap:
        _, current = heapq.heappop(heap)
        if current == goal:
            return True
        visited.add(current)
        for neighbor in neighbors(grid, current):
            if neighbor not in visited:
                heapq.heappush(heap, (heuristic(neighbor, goal), neighbor))
    return False

def run_gbfs_experiments():
    sizes = [5000, 50000, 500000, 5000000, 50000000]
    obstacles = [10, 100, 1000, 10000, 100000]

    for i in range(len(sizes)):
        n = int(sizes[i]**0.5)
        grid = generate_grid(n, obstacles[i])
        start = (0, 0)
        goal = (n-1, n-1)

        print(f"GBFS Experiment #{i+1} with {sizes[i]} nodes and {obstacles[i]} obstacles")

        start_time = time.time()
        gbfs(grid, start, goal)
        duration = (time.time() - start_time) * 1000
        print(f"Execution Time: {duration:.2f} ms\n")

run_gbfs_experiments()
