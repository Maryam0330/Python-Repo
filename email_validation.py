#Email validation in python (using string functions)
email = input("Enter your email: ")  #a@g.in  #a@g.com
k,j,d = 0,0,0

if len(email) >= 6:           #email should be greater than or equal to 6 characters
    if email[0].isalpha():    #checks whether the first letter (i.e at index 0) is alphabet or not 
        if ("@" in email) and (email.count("@") == 1):  #@ should be in email and the position of @ should be at index 1
            if (email[-4] == ".") ^ (email[-3] == "."): #checks whether the position of . is at index -3 or -4 using Ex-OR operator
                for i in email:  
                    if i == i.isspace(): #checks if there is space in between
                        k = 1
                    elif i.isalpha():        #checks whether the letters are alphabet 
                        if i == i.upper():   #converts i to uppercase
                            j = 1
                    elif i.isdigit():        #if i is digit then continue
                        continue
                    elif i == "_" or i == "." or i == "@":  #if i is _ . @ then continue
                        continue
                    else:
                        d = 1                #if any other sign is used 
                if k == 1 or j == 1 or d == 1:
                    print("Invalid email 5")
            else:
                print("Invalid email 4")
        else:
            print("Invalid email 3")
    else:
        print("Invalid email 2")
else:
    print("Invalid email 1") 
