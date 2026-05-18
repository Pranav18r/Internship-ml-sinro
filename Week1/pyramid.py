row_count = int(input("Enter no of rows: "))

for i in range(1, row_count + 1):
    for j in range(row_count - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()