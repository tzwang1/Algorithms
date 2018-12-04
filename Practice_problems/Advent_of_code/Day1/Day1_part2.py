def first_repeating_freq(numbers):
    res = 0
    seen = set()
    found = False
    while not found:
        for num in numbers:
            if res in seen:
                return res
            seen.add(res)
            res+=num

    print("No repeating frequency!")


if __name__ == "__main__":
    input_nums_file = "Day1_input.txt"
    input_nums = []

    with open(input_nums_file) as f:
        for line in f:
            input_nums.append(int(line))

    print(first_repeating_freq(input_nums))