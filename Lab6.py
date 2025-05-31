def max_experience(pyramid):
    dp = pyramid[-1][:]
    for level in range(len(pyramid) - 2, -1, -1):
        for i in range(len(pyramid[level])):
            dp[i] = pyramid[level][i] + max(dp[i], dp[i + 1])
    return dp[0]


def read_input(filepath):
    try:
        with open(filepath, "r") as file:
            lines = file.readlines()
        l = int(lines[0].strip())
        pyramid = [list(map(int, lines[i + 1].strip().split())) for i in range(l)]
        return pyramid
    except Exception as e:
        raise FileNotFoundError(f"Input file error: {e}")


def write_output(filepath, result):
    with open(filepath, "w") as file:
        file.write(f"{result}\n")


if __name__ == "__main__":
    input_path = "lab6.in"
    output_path = "lab6.out"
    try:
        pyramid = read_input(input_path)
        result = max_experience(pyramid)
        write_output(output_path, result)
    except FileNotFoundError as err:
        print(err)
