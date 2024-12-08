INPUT = "Inputs\\Day 7.txt"

import itertools

def generate_equation(string, operators):
    indices = [i for i, char in enumerate(string) if char == ' ']
    
    combos = itertools.product(operators, repeat=len(indices))
    
    results = []
    for combo in combos:
        temp = list(string)
        for index, replacement in zip(indices, combo):
            temp[index] = replacement
        results.append(''.join(temp))
    for i in range(len(indices)):
        results = [f"({result}" for result in results]
    return results

def main():
    operations = [")+",")*"]
    with open(INPUT, 'r') as file:
        lines = file.readlines()
        total = 0
        for line in lines:
            goal = int(line.split(":")[0])
            nums = line.strip().split(":")[1].strip()
            eqns = generate_equation(nums, operations)
            for eqn in eqns:
                if eval(eqn) == goal: # Could I use backtracking? Yes. Should I? Also yes. This is funnier
                    total += goal
                    break
            
        print(total)

if __name__ == "__main__":
    main()