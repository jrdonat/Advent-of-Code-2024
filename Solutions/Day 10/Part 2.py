INPUT = "Inputs\\Day 10.txt"

import heapq
from collections import defaultdict

graph = []
start_nodes = []
goal_nodes = []

step = 1

def pathfind(start, goal):
    def backtrack(current, path):
        if current == goal:
            paths.append(path[:])
            return
        for neighbour in get_neighbours(current):
            if neighbour not in path: # Kind of redundant, it won't be
                path.append(neighbour)
                backtrack(neighbour, path)
                path.pop()
    paths = []
    backtrack(start, [start])
    return paths

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
            total += len(pathfind(start, goal))
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