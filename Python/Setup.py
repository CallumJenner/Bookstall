# This it the initial file the company will use to set up the program

adminCode = ""
adminPassword = ""
adminPassConfirm = " "
staffCode = ""
staffPassword = ""
staffPassConfirm = " "

print("Welcome to #Program name")

# Export below to file which is encrypted
shopName = input("Shop name: ")

signIn = input("Login or Register L/R: ").upper()

if signIn == "L":
    loginUsername = input("Username: ")
    loginPassword = input("Password: ")
elif signIn == "R":
    shopID = input("Shop ID: ")
    shopPassword = input("Shop Password: ")
    if shopID == shopID and shopPassword == shopPassword:
        regLevel = input("Admin or Staff A/S: ").upper()
        if regLevel == "A":
            adminCode = input("Admin code (To get this code contact your superior): ")
            if adminCode == adminCode:
                while adminPassword != adminPassConfirm:
                    adminFirst = input("First name: ")
                    adminLast = input("Last name: ")
                    adminUsername = input("Username: ")
                    adminPassword = input("Password: ")
                    adminPassConfirm = input("Password Confirm: ")
                    adminEmail = input("Email: ")
                    if adminPassword != adminPassConfirm:
                        print("Passwords do not match\n")
            else:
                print("Admin code invalid")
        elif regLevel == "S":
            if staffCode == staffCode:
                while staffPassword != staffPassConfirm:
                    staffFirst = input("First name: ")
                    staffLast = input("Last name: ")
                    staffUsername = input("Username: ")
                    staffPassword = input("Password")
                    staffPassConfirm = input("Password Confirm: ")
                    staffEmail = input("Email: ")
            else:
                print("Staff code invalid\n")
                print("")



        #registerFirst = input("First name: ")
        #registerLast = input("Last name: ")
