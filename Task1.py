with open("rows.txt") as fp:
    total = 0
    for count, line in enumerate(fp):
        line = [int(num) for num in line.split()]
        total += sum(line)
        diff = max(line) - min(line)
        print(f"Diff max-min value in line {count} is: {diff}")
    print(f"The CheckSum is : {total}")
