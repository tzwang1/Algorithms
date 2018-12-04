def calculate_frequency(numbers):
    res = 0
    for num in numbers:
        res+=num
    
    return res

if __name__ == "__main__":
    input_nums_file = "Day1_input.txt"
    input_nums = []
    with open(input_nums_file) as f:
        for line in f:
            input_nums.append(int(line))
    
    print(calculate_frequency(input_nums))
