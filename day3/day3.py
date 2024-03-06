def code_to_image(file):
    with open(file, 'r') as f:
        output = ""
        x = False
        for a, i in enumerate(f.read().split(" ")):
            if ((a-1) % 2 == 0):
                output += "#"*int(i)
            else:
                output += "."*int(i)
        
        for i in range(0, len(output), 100):
            print(output[i:i+100])

code_to_image("day3/input3.txt")