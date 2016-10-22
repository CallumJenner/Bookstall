# This is the main program to run the book shop

print("Welcome to #The shop name")

# This is where the user inputs what they want to do, I will add a more
# elequent way to do this later
command = input("What do you want to do (B/S/C/Q)").upper() # Buy/Sell/stock Check/Quit

if command == "B":
    print("Buy")
    buyNum = int(input("How many books are you buying?: "))
    buyCost = float(input("How much are you paying?: "))
    for i in range(buyNum):
        buyTitle = input("Book title: ")
        buyAuthor = input("Book author: ")

elif command == "S":
    print("Sell")
    sellNum = int(input("How many books are you selling?: "))
    sellCost = float(input("How many books are you selling?"))
    for i in range(sellNum):
        sellTitle = input("Book title: ")
        sellAuthor = input("Book author: ")

elif command -- "C":
    print("Stock Check")
    # Check from file if a copy of the book is avaliable
    
elif command == "Q":
    print("Goodbye")
else:
    print("Invalid")
