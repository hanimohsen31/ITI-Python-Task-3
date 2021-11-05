import datetime


# insert function
def insertinfo():
    # id validation
    while True:
        try:
            id101 = int(input("Enter ID : "))
            break
        except:
            print("Not a Valid id")

    # -------------------------------------------------------
    # title validation
    while True:
        title = input("Enter Project Title : ")
        if title.isalpha() == False:
            print('Not Valid')
        else:
            # print(title)
            break

    while True:
        details = input("Enter Project Details : ")
        if details == '':
            print('Not Valid')
        else:
            # print(details)
            break
    # -------------------------------------------------------
    # target validation
    while True:
        target = input("Enter Project Trget : ")
        if target.isdigit() == False:
            print('Not Valid')
        else:
            # print(target)
            break
    # -------------------------------------------------------
    # start date validation
    while True:
        try:
            nowtime = datetime.datetime.now()

            while True:
                year = int(input("Enter Project Campaign start year : "))
                if year < int(nowtime.year):
                    print('Wrong Year')
                else:
                    break

            while True:
                month = int(input("Enter Project Campaign start Month : "))
                if month < 0 or month > 12:
                    print('Wrong month')
                else:
                    break

            while True:
                day = int(input("Enter Project Campaign start Day : "))
                if day < 0 or day > 31:
                    print('Wrong day')
                else:
                    break

            startdate = datetime.datetime(year, month, day)
            startdateourput = startdate.strftime("%Y-%m-%d")
            # print('Valid Date')
            break

        except:
            print('Not a Valid Date')
    # -------------------------------------------------------
    # end date validation
    while True:
        try:
            while True:
                year = int(input("Enter Project Campaign End year : "))
                if year < int(startdate.year):
                    print('Wrong Year')
                else:
                    break

            while True:
                month = int(input("Enter Project Campaign End Month : "))
                if month < 0 or month > 12:
                    print('Wrong month')
                else:
                    break

            while True:
                day = int(input("Enter Project Campaign End Day : "))
                if day < 0 or day > 31:
                    print('Wrong day')
                else:
                    break

            enddate = datetime.datetime(year, month, day)
            enddateourput = enddate.strftime("%Y-%m-%d")
            # print('Valid Date')
            break

        except:
            print('Not a Valid Date')

    userinputsnew = ":".join([str(id101), title, details, target, startdateourput, enddateourput])
    return f'\n{userinputsnew}'


# register function
def register():
    fnamelist = []
    while len(fnamelist) == 0:
        fname = input('Enter Your First Name : ')
        if fname.isalpha() == False:
            print('Invalid Name')
        else:
            fnamelist.append(fname)

    lnamelist = []
    while len(lnamelist) == 0:
        lname = input('Enter Your Last Name : ')
        if lname.isalpha() == False:
            print('Invalid Name')
        else:
            lnamelist.append(lname)

    emaillist = []
    while len(emaillist) == 0:
        email = input('Enter Your Email : ')
        if "@" not in email:
            print("invalid")
        else:
            newemail1 = email.replace('@', '')
            newemail2 = newemail1.replace('.', '')
            if newemail2.isalpha() == False:
                print('InValid')
            else:
                emaillist.append(email)

    passwordlist = []
    while len(passwordlist) == 0:
        password = input('Enter Your Password : ')
        if len(password) < 4:
            print('Short Password')
        else:
            passwordlist.append(password)

    while True:
        confirm_password = input('Confirm password : ')
        if password != confirm_password:
            print('Password Does not Match')
        else:
            break

    while True:
        phone = input('Enter Your Phone Number : ')
        if phone.isdigit() == False:
            print('Enter Numbers Only')
        elif len(phone) != 11:
            print('Number Should Contains 11 Digits')
        elif int(phone[0]) != 0:
            print('First Number Should be 0')
        elif int(phone[1]) != 1:
            print('Second Number Should be 1')
        else:
            break

    userinputs = ":".join([fname, lname, email, phone, password])
    usersfile = open('usersfile.txt', 'a')
    usersfile.write(f'\n{userinputs}')


# editing line in project file
def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()


# removing a line in project file
def remove_line(lineToSkip):
    """ Removes a given line from a file """
    with open('projects.txt', 'r') as read_file:
        lines = read_file.readlines()
    currentLine = 1
    with open('projects.txt', 'w') as write_file:
        for line in lines:
            if currentLine == lineToSkip:
                pass
            else:
                write_file.write(line)
            currentLine += 1


# search by date function
def searchfunc():
    usersfile = open('projects.txt', 'r')
    while True:
        try:
            while True:
                year = int(input("Enter Project Campaign End year : "))
                if year < 2020:
                    print('Wrong Year')
                else:
                    break

            while True:
                month = int(input("Enter Project Campaign End Month : "))
                if month < 0 or month > 12:
                    print('Wrong month')
                else:
                    break

            while True:
                day = int(input("Enter Project Campaign End Day : "))
                if day < 0 or day > 31:
                    print('Wrong day')
                else:
                    break

            searchdate = datetime.datetime(year, month, day)
            searchdateout = searchdate.strftime("%Y-%m-%d")
            print('Valid Date ... Going to Compare now with database')

            for line in usersfile.readlines():
                # splitted = line.split(':')
                if str(searchdateout) in line:
                    print(line)
                else:
                    print("Not Found")
                    break

        except:
            print('Not a Valid Date')


# login function
def login():
    emaillist = []
    while len(emaillist) == 0:
        email = input('Enter Your Email : ')
        if "@" not in email:
            print("invalid")
        else:
            newemail1 = email.replace('@', '')
            newemail2 = newemail1.replace('.', '')
            if newemail2.isalpha() == False:
                print('InValid')
            else:
                emaillist.append(email)

    passwordlist = []
    while len(passwordlist) == 0:
        password = input('Enter Your Password : ')
        if len(password) < 4:
            print('Shorter than Expected Password')
        else:
            passwordlist.append(password)
    # print('Data Recived')
    # comparing data with users data
    usersfile = open('usersfile.txt', 'r')
    for line in usersfile.readlines():
        if email in line and password in line:
            print('Successfully logged in')
            projenter = input('Choose Register or Login (v/i/e/d/s)')
            if projenter == 'v':
                print('File Content View')
                file = open('projects.txt', 'r')
                print(file.readlines())

            elif projenter == 'i':
                returner = insertinfo()
                projects = open('projects.txt', 'a')
                projects.write(returner)
                projects.close()

            elif projenter == 'e':
                while True:
                    try:
                        line = int(input("Enter Line Number : "))
                        break
                    except:
                        print("Not a Valid line")
                newdata = insertinfo()
                replace_line('projects.txt', line - 1, f'{newdata}\n')

            elif projenter == 'd':
                while True:
                    try:
                        line = int(input("Enter Line Number : "))
                        break
                    except:
                        print("Not a Valid line")
                remove_line(line)
            elif projenter == 's':
                searchfunc()
            else:
                print('Not A valid Choice')
