# This is the main program to run the book shop
# Add info to sql table

command = "" # This is to define command

# Add validation to all user input eg if enter invalid charachter / author etc. prompt them to enter again instead of just throwing an error

# Welcome message - the "# Shop name" will change depending on the independant shop's name
print("Welcome to #The shop name")

while command != "Q": # This is so after the employee has done one thing they can then do another
    # This is where the user inputs what they want to do, I will add a more
    # elequent way to do this later
    command = input("What do you want to do (B/S/C/A/Q)").upper() # Buy/Sell/stock Check/Add author or title to sql database/Quit

    if command == "B":
        print("Buy")
        buyNum = int(input("How many books are you buying?: "))
        buyCost = float(input("How much are you paying?: "))
        for i in range(buyNum):
            buyTitle = input("Book title: ")
            buyAuthorFirst = input("Book author's first name: ")
            buyAuthorLast = input("Book author's last name: ")
            print("")

    elif command == "S":
        print("Sell")
        sellNum = int(input("How many books are you selling?: "))
        sellCost = float(input("How much are you selling them for?: "))
        for i in range(sellNum):
            sellTitle = input("Book title: ")
            sellAuthorFirst = input("Book author's first name: ")
            sellAuthorlast = input("Book author's last name: ")

    elif command == "C":
        print("Stock Check")
        # Check from file if a copy of the book is avaliable

    # Generate unique IDs for each author and title
    elif command == "A":
        print("Add")
        addType = input("What would you like to add? A/T").upper() # Author or title
        if addType == "A":
            addAuthGenre = input("What genre is the author?: ")
            addAuth = input("Author name: ")
        elif addType == "T":
            addTitleAuth = input("Who is the author of the book?: ")
            addTitle = input("Book title: ")


    elif command == "Q":
        print("Goodbye")
    else:
        print("Invalid")
