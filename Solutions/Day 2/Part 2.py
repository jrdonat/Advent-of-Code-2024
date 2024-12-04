INPUT = "Inputs\\Day 2.txt"

import itertools

def is_safe_line(levels):
    initial_direction = 1 if levels[0] > levels[1] else -1
    
    for i in range(len(levels) - 1):
        if abs(levels[i] - levels[i+1]) > 3 or levels[i] == levels[i+1]:
            return False
        
        current_direction = 1 if levels[i] > levels[i+1] else -1
        if current_direction != initial_direction:
            return False
    
    return True

def is_safe_line_recursive(levels):
    # Try every combinatition of levels with only one level removed
    for combination in itertools.combinations(levels, len(levels) - 1):
        if is_safe_line(combination):
            return True



def count_safe_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        safe_lines = sum(1 for line in lines if is_safe_line_recursive(list(map(int, line.strip().split()))))
    
    return safe_lines

def main():
    print(f"Safe levels: {count_safe_lines(INPUT)}")

if __name__ == "__main__":
    main()