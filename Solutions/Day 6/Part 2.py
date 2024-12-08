INPUT = "Inputs\\Day 6.txt"

import copy

visited_positions = {}
matrix_backup = []
matrix = []
direction_order = ["^", ">", "v", "<"]
infinite_loops = 0
first = True

def move(pos):
    num_of_moves = 0
    global first
    global infinite_loops
    while True:
        orientation = matrix[pos[0]][pos[1]]
        next_pos = {
            "^": (pos[0] - 1, pos[1]),
            ">": (pos[0], pos[1] + 1),
            "v": (pos[0] + 1, pos[1]),
            "<": (pos[0], pos[1] - 1)
        }[orientation]
        
        if next_pos[0] < 0 or next_pos[0] >= len(matrix) or next_pos[1] < 0 or next_pos[1] >= len(matrix[0]):
            if first:
                print(len(visited_positions))
            break
        
        while matrix[next_pos[0]][next_pos[1]] == "#":
            orientation = direction_order[(direction_order.index(orientation) + 1) % 4]
            next_pos = {
                "^": (pos[0] - 1, pos[1]),
                ">": (pos[0], pos[1] + 1),
                "v": (pos[0] + 1, pos[1]),
                "<": (pos[0], pos[1] - 1)
            }[orientation]
        
        if first:
            visited_positions[next_pos] = True
        matrix[next_pos[0]][next_pos[1]] = orientation
        pos = next_pos
        num_of_moves += 1
        if num_of_moves > 6000:
            infinite_loops += 1
            break
    if first:
        first = False



def main():
    global matrix
    with open(INPUT, 'r') as file:
        lines = file.readlines()
        start = None
        for line in lines:
            matrix.append([char for char in line.strip()])
            if "^" in matrix[-1]:
                start = (len(matrix) - 1, matrix[-1].index("^"))
        matrix_backup = copy.deepcopy(matrix)
        move(start)

    for key, value in visited_positions.items():
        if key == start:
            continue
        matrix = copy.deepcopy(matrix_backup)
        matrix[key[0]][key[1]] = "#"
        move(start)

    print(infinite_loops)


if __name__ == "__main__":
    main()