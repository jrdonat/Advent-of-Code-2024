INPUT = "Inputs\\Day 8.txt"

import itertools

matrix_dimensions = [0, 0]
antenna_positions = {}
nodes = {}

def main():
    with open(INPUT, 'r') as file:
        lines = file.readlines()
        matrix_dimensions[0] = len(lines)
        matrix_dimensions[1] = len(lines[0].strip())
        for y, line in enumerate(lines):
            for x, char in enumerate(line.strip()):
                if char != ".":
                    if char not in antenna_positions:
                        antenna_positions[char] = []
                    antenna_positions[char].append((x, y))
                    nodes[(x, y)] = True
    
    for key in antenna_positions:
        combos = itertools.combinations(antenna_positions[key], 2)
        for combo in combos:
            x_diff = combo[0][0] - combo[1][0]
            y_diff = combo[0][1] - combo[1][1]
            new_x = x_diff
            new_y = y_diff
            while True:
                both_failed = False
                if combo[0][0] + new_x >= 0 and combo[0][0] + new_x < matrix_dimensions[1] and combo[0][1] + new_y >= 0 and combo[0][1] + new_y < matrix_dimensions[0]:
                    nodes[(combo[0][0] + new_x, combo[0][1] + new_y)] = True
                else:
                    both_failed = True
                if combo[1][0] - new_x >= 0 and combo[1][0] - new_x < matrix_dimensions[1] and combo[1][1] - new_y >= 0 and combo[1][1] - new_y < matrix_dimensions[0]:
                    nodes[(combo[1][0] - new_x, combo[1][1] - new_y)] = True
                    both_failed = False
                if both_failed:
                    break
                new_x += x_diff
                new_y += y_diff
    print(len(nodes))


if __name__ == "__main__":
    main()