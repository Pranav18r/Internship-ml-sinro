def main():
    while True:
        print("1.Write\n2.Read\n3.Exit")
        choice = int(input("Enter your choice: "))
        if(choice == 1):
            with open("sample.txt","a+") as f:
                content = str(input("Enter to write: ")) 
                f.write(content)
                f.write("\n")
        elif(choice == 2):
            with open("sample.txt","r") as f:
                output = f.read()
                print(output)
        else:
            break
            

if __name__ == "__main__":
    main()