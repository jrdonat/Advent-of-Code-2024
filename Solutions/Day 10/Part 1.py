INPUT = "Inputs\\Day 10.txt"

import heapq

graph = []
start_nodes = []
goal_nodes = []

step = 1

def heuristic(start, goal):
    return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

def pathfind(start, goal): # A*
    open_set = []
    closed_set = set()
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    heapq.heappush(open_set, (f_score[start], start))
    while open_set:
        current = heapq.heappop(open_set)[1]
        if current == goal:
            return True
        closed_set.add(current)
        for neighbor in get_neighbours(current):
            if neighbor in closed_set: # Only here because A* standard, redundant
                continue
            tentative_g_score = g_score[current] + graph[neighbor[0]][neighbor[1]]
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
    return False

def get_neighbours(coord):
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for direction in directions:
        neighbor = (coord[0] + direction[0], coord[1] + direction[1])
        if 0 <= neighbor[0] < len(graph) and 0 <= neighbor[1] < len(graph[0]):
            if graph[neighbor[0]][neighbor[1]] - graph[coord[0]][coord[1]] == step:
                neighbors.append(neighbor)
    return neighbors

def find_trails():
    total = 0
    for start in start_nodes:
        for goal in goal_nodes:
            total += 1 if pathfind(start, goal) else 0
    return total


def main():
    with open(INPUT, 'r') as file:
        for line in file:
            graph.append([int(x) for x in line.strip()])
        file.close()
    for i, row in enumerate(graph):
        for j, value in enumerate(row):
            if value == 0:
                start_nodes.append((i, j))
            elif value == 9:
                goal_nodes.append((i, j))
    
    print(find_trails())

if __name__ == "__main__":
    main()