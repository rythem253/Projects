def main():
    print("Hello User!")

    """
    x = int(input()) -- To take input.
    &&
    x = int(input("Chose a number: ")) -- Takes input and displays
    a statement.
    """
    x = int(input("Chose a number: "))
    
    """
    If-Statement in Python
    """
    if x > 5:
        print("You chose greater than 5")
    elif x == 5:
        print("You chose 5")
    else:
        print("You chose less than 5")

if __name__ == "__main__":
    main()
