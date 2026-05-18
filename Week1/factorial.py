number_to_find = int(input("Enter number to find: "))
fact = 1

for i in range(1,number_to_find+1):
    fact = fact * i

print("factorial : ",fact)