INPUT = "Inputs\\Day 1.txt"

def calculate_total_distance(left_list, right_list):
    right_set = {}
    for right in right_list: # All these rights and lefts. I need a better naming convention
        if right not in right_set:
            right_set[right] = 0
        right_set[right] += 1
    total_distance = 0
    for left in left_list:
        total_distance += right_set[left] * left if left in right_set else 0
    return total_distance

def split_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    left_list = []
    right_list = []
    for line in lines:
        nums = line.strip().split()
        if len(nums) == 2:
            left_list.append(int(nums[0]))
            right_list.append(int(nums[1]))
    return left_list, right_list

def main():
    left_list, right_list = split_input(INPUT)
    total_distance = calculate_total_distance(left_list, right_list)
    print(f"Total distance between lists: {total_distance}")

if __name__ == "__main__":
    main()