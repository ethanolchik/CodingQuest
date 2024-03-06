x = {}

def type_(t):
    match t:
        case "Rebate" | "Discount":
            return -1
        case _:
            return 1


def calc_cheapest(file):
    with open(file, 'r') as f:
        for i in f:
            item, t, num = i.replace(":", "").split()
            x[item] = x.get(item, 0) + type_(t) * int(num)

    return min(x, key=x.get)

print(calc_cheapest("day1/input.txt"))