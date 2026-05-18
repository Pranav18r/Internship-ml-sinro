def sum_function(a,b):
    sum_value = a + b
    return sum_value



def main():
    num1 = int(input("Enter no 1: "))
    num2 = int(input("Enter no 2: "))
    sum_result = sum_function(num1,num2)
    print(f"sum of {num1} and {num2} is {sum_result}")




if __name__ == "__main__":
    main()