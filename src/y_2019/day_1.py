

def parse(lines):
    ans = []
    for line in lines:
        ans.append(int(line))
    return ans


def solve(data):
    total = 0
    for num in data:
        total = total + get_required_fuel(num)
    return total


def get_required_fuel(num):
    ret: int = num//3  # divide by 3, and rounding down
    ret = ret - 2  # subtract 2
    return ret
