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
    return results

def main():
    operations = [")+",")*","||"]
    with open(INPUT, 'r') as file:
        lines = file.readlines()
        total = 0
        for line in lines:
            goal = int(line.split(":")[0])
            nums = line.strip().split(":")[1].strip()
            eqns = generate_equation(nums, operations)
            for eqn in eqns:
                while len(eqn.split("||")) > 1:
                    first_section = eqn.split("||")[0]
                    closing_braces = first_section.count(")")
                    first_section = "(" * closing_braces + first_section
                    evalution = eval(first_section)
                    neweqn = ""
                    for section in eqn.split("||")[1:]:
                        neweqn += section + "||"
                    eqn = (str(evalution) + neweqn).removesuffix("||")
                closing_braces = eqn.count(")")
                eqn = "(" * closing_braces + eqn
                if eval(eqn) == goal:
                    total += goal
                    break
            
        print(total)





if __name__ == "__main__":
    main()