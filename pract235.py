
str = input("Enter a string: ")

while True:
    print("-"  * 25)
    print("          MENU    ")
    print("-"  * 25)
    print("1.Find frequency of a character")
    print("2.Replace a character")
    print("3.Remove first occurrence of a character")
    print("4.Remove all occurrences of a character")
    print("5.Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        ch = input("Enter character: ")
        print("Frequency =", str.count(ch))

    elif choice == 2:
        ch = input("Enter character to replace: ")
        new_ch = input("Enter new character: ")
        str = str.replace(ch, new_ch)
        print("New string =", str)

    elif choice == 3:
        ch = input("Enter character to remove: ")
        pos = str.find(ch)

        if pos != -1:
            str = str[:pos] + str[pos + 1:]

        print("New string =", str)

    elif choice == 4:
        ch = input("Enter character to remove: ")
        str = str.replace(ch, "")
        print("New string =", str)

    elif choice == 5:
        break

    else:
        print("Invalid choice")
