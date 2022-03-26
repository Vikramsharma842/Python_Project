# Email Validation Project

email = input("Enter the Email for which you want to validate:")

# vikram.sharma@gmail.com --- v@g.com or v@g.in--minimum 6 letters are required
k = 0
j = 0
d = 0
if len(email) >= 6:            # check the length of string
    if email[0].isalpha():     # check for the first letter is alphabet or not
        if ("@" in email) and email.count("@") == 1:   # check @ is in the string and count the no of @
            if (email[-3] == ".") ^ (email[-4] == "."):  # check for the last 3 and 4 position for "."
                for i in email:
                    if i.isspace():      # check for the ith char is "_" or not
                        k = 1
                    elif i.isdigit():    # check for the ith char is digit or not
                        continue
                    elif i.isupper():     # check for the ith char is upper case letter or not
                        j = 1
                    elif i.islower():     # check for the ith char is lower case letter or not
                        continue
                    elif i == "@" or i == "." or i == "_":  # check for ith char is any one of these
                        continue
                    else:
                        d = 1


                if d == 1 or k == 1 or j == 1:   # if any one of these condition satisfy print wrong
                    print("Wrong Email 5")
                else:
                    print("Correct Email Id")      # else print correct email id
            else:
                print("Wrong Email 4")
        else:
            print("Wrong Email 3")
    else:
        print("Wrong Email 2")

else:
    print("Wrong Email 1")
