def getdate():
    import datetime
    return datetime.datetime.now()


h = "harry"
r = "rohan"
ha = "hammad"
print("       WELCOME TO HELTH MANAGEMENT SYSTEM")
print("For which client are you here\n1 for harry\n2 for rohan\n3 for hammad")
client = int(input())

if client == 1:
    print("What do you want\n1 for log\n2 for retrive")
    want = int(input())
    if want == 1:
        print("What do you want to log\n1 for diet\n2 for exercise")
        log = int(input())
        if log == 1:
            print("Tell what did you eat?")
            eat = input()
            f = open("harry1.txt", "a")
            f.write("\nat time==")
            f.write(str(getdate()))
            f.write(" you eat--- ")
            f.write(eat)

        elif log == 2:
            print("Tell what did you do?")
            log = input()
            f = open("harry2.txt", "a")
            f.write("\nat time==")
            f.write(str(getdate()))
            f.write(" you did--- ")
            f.write (log)

        else:
            print("wrong number")

    elif want == 2:
        print("What do you want to retrive\n1 for diet\n2 for exercise")
        retrive = int(input())
        if retrive == 1:
            f = open("harry1.txt", "rt")
            for line in f:
                print(line)

        elif retrive == 2:
            f = open("harry2.txt", "rt")
            for line in f:
                print(line)

        else:
            print("wrong number")

    else:
        print("wrong number")


elif client == 2:
    print("What do you want\n1 for log\n2 for retrive")
    want = int(input())
    if want == 1:
        print("What do you want to log\n1 for diet\n2 for exercise")
        log = int(input())
        if log == 1:
            print("Tell what did you eat?")
            eat = input()
            f = open("rohan1.txt", "a")
            f.write("\nat time==")
            f.write(str(getdate()))
            f.write(" you eat--- ")
            f.write(eat)

        elif log == 2:
            print("Tell what did you do?")
            log = input()
            f = open("rohan2.txt", "a")
            f.write("\nat time==")
            f.write(str(getdate()))
            f.write(" you did--- ")
            f.write (log)

        else:
            print("wrong number")

    elif want == 2:
        print("What do you want to retrive\n1 for diet\n2 for exercise")
        retrive = int(input())
        if retrive == 1:
            f = open("rohan1.txt", "rt")
            for line in f:
                print(line)

        elif retrive == 2:
            f = open("rohan2.txt", "rt")
            for line in f:
                print(line)

        else:
            print("wrong number")

    else:
        print("wrong number")


elif client == 3:
    print("What do you want\n1 for log\n2 for retrive")
    want = int(input())
    if want == 1:
        print("What do you want to log\n1 for diet\n2 for exercise")
        log = int(input())
        if log == 1:
            print("Tell what did you eat?")
            eat = input()
            f = open("hammad1.txt", "a")
            f.write("\nat time==")
            f.write(str(getdate()))
            f.write(" you eat--- ")
            f.write(eat)

        elif log == 2:
            print("Tell what did you do?")
            log = input()
            f = open("hammad2.txt", "a")
            f.write("at time==")
            f.write(str(getdate()))
            f.write(" you did--- ")
            f.write (log)

        else:
            print("wrong number")

    elif want == 2:
        print("What do you want to retrive\n1 for diet\n2 for exercise")
        retrive = int(input())
        if retrive == 1:
            f = open("hammad1.txt", "rt")
            for line in f:
                print(line)

        elif retrive == 2:
            f = open("hammad2.txt", "rt")
            for line in f:
                print(line)

        else:
            print("wrong number")

    else:
        print("wrong number")

else:
    print("wrong number")
