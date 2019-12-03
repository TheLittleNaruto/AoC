

def parse(numbers):
    return list(map(int, numbers.split(',')))


def solve(data):
    ret = 0
    # if data is less than length
    # of 4; returns 0th index value
    n = len(data)
    if n < 4:
        return data[0]

    for x in range(0, n - 4, 4):
        if data[x] == 99:
            break
        else:
            compute(data, x)
    return data[0]


def compute(data, position):
    op_code = data[position]
    first = data[position + 1]
    second = data[position + 2]
    output_position = data[position + 3]
    if op_code == 1:
        try:
            data[output_position] = data[first] + data[second]
        except ValueError as e:
            pass
    elif op_code == 2:
        try:
            data[output_position] = data[first] * data[second]
        except ValueError as e:
            pass
