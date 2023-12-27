import time


def part1(lines):
    count = 0
    for line in lines:
        num_list = []
        for character in line:
            if character.isnumeric():
                num_list.append(character)

        first_num = num_list[0]
        last_num = num_list[-1]
        joint_num = f"{first_num}{last_num}"
        count += int(joint_num)

    return count


def string_num_to_int(line):
    num_names = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for digit, name in enumerate(num_names):
        line = line.replace(name, f"{name}{digit}{name}")
    return line


def part2(lines):
    count = 0
    for line in lines:
        line = string_num_to_int(line)
        num_list = []
        for character in line:
            if character.isnumeric():
                num_list.append(character)

        first_num = num_list[0]
        last_num = num_list[-1]
        joint_num = f"{first_num}{last_num}"
        count += int(joint_num)

    return count


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        puzzle_input = f.read()
        puzzle_lines = puzzle_input.split("\n")

    start = time.perf_counter()
    result = part1(puzzle_lines)
    end = time.perf_counter()
    print(f"Part 1 result is: {result}, computed in: {end - start :.3} seconds")

    start = time.perf_counter()
    result = part2(puzzle_lines)
    end = time.perf_counter()
    print(f"Part 2 result is: {result}, computed in: {end - start :.3} seconds")
