INPUT = "Inputs\\Day 6.txt"

visited_positions = {}
matrix = []
direction_order = ["^", ">", "v", "<"]

def move(pos):
    while True:
        orientation = matrix[pos[0]][pos[1]]
        next_pos = {
            "^": (pos[0] - 1, pos[1]),
            ">": (pos[0], pos[1] + 1),
            "v": (pos[0] + 1, pos[1]),
            "<": (pos[0], pos[1] - 1)
        }[orientation]
        
        if next_pos[0] < 0 or next_pos[0] >= len(matrix) or next_pos[1] < 0 or next_pos[1] >= len(matrix[0]):
            print(len(visited_positions))
            break
        
        if matrix[next_pos[0]][next_pos[1]] == "#": # Notice how this changes in part 2. It's quite interesting to think why this didn't cause issues in part 1.
            orientation = direction_order[(direction_order.index(orientation) + 1) % 4]
            next_pos = {
                "^": (pos[0] - 1, pos[1]),
                ">": (pos[0], pos[1] + 1),
                "v": (pos[0] + 1, pos[1]),
                "<": (pos[0], pos[1] - 1)
            }[orientation]
        
        visited_positions[next_pos] = True
        matrix[next_pos[0]][next_pos[1]] = orientation
        pos = next_pos

def main():
    with open(INPUT, 'r') as file:
        lines = file.readlines()
        start = None
        for line in lines:
            matrix.append([char for char in line.strip()])
            if "^" in matrix[-1]:
                start = (len(matrix) - 1, matrix[-1].index("^"))
        visited_positions[start] = True
        move(start)

if __name__ == "__main__":
    main()