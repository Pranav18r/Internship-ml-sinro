with open("sample.txt","a+") as f:
    content = str(input("Enter content: "))
    f.write(content)


with open("sample.txt") as f:
    output = f.read()
    print(output)