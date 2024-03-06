def parse_ip(bytes):
    return '.'.join(str(int(bytes[i:i+2], 16)) for i in range(0, len(bytes), 2))

def calc_ratio(file):
    x = 0
    y = 0

    with open(file, 'r') as f:
        for i in f:
            l = int(i[4:8], 16)
            src = parse_ip(i[24:32])
            dest = parse_ip(i[32:40])

            if src.startswith('192.168.') or dest.startswith('192.168.'):
                x += l
            elif src.startswith('10.') or dest.startswith('10.'):
                y += l

    return x, y

x, y = calc_ratio("input2.txt")
print(f"{x}/{y}")
