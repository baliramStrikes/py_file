import datetime
while True:
    name = str(input("hello sir! can you tell me your name please:- "))
    create_all_name = open("all_name.txt","a")
    create_all_name.close()
    all_name = open("all_name.txt","r+")
    file_read = all_name.read()
    if name == "exit":
        print("thank you sir:- ")
        exit()
    if name not in file_read:
        print("sir you told your name is:- "+name)
        work = input("what do you want to do today sir:- ")
        print("sir your today work is:- "+work)
        place = input("sir you are to go anyware today:- ")
        all_name.write(name+"\n")
        all_name.close()
        create_user_file = open(name+".txt","a")
        create_user_file.close()
        open_user_file = open(name+".txt","r+")
        read_open_file = open_user_file.readline().replace("\t","")
        if read_open_file != "nameworkplace\n":
            open_user_file.write("name"+"\twork"+"\tplace\n")
            open_user_file.write(("-x"*50)+"\n")
            open_user_file.write(name + "\t"+work +"\t"+place)
            open_user_file.write("\n"+str(datetime.datetime.now()))
            open_user_file.write("\n"+("-"*50))
            open_user_file.close()
    else:
        print("sir you told your name is:- "+name)
        work = input("what do you want to do today sir:- ")
        print("sir your today work is:- "+work)
        place = input("sir you are to go anyware today:- ")
        user_file = open(name+".txt","r+")
        open_user_file = open(name+".txt","r+")
        read_open_file = open_user_file.readline().replace("\t","")
        if read_open_file == "nameworkplace\n":
            open_user_file.write("\n"+name + "\t"+work +"\t"+place)
            open_user_file.write("\n"+str(datetime.datetime.now()))
            open_user_file.write("\n"+("-"*50))
            open_user_file.close()

    check_files = input("if you want to find any name write Y or N:- ")
    if check_files == "Y":
        check_name = input("want to find your name write a name:- ")
        all_name = open("all_name.txt")
        check_all_name = all_name.read()
        if check_name in check_all_name:
            print("yes your name is persent in list...")
            detail_input = input("want to see detail about the name... write Y or N:- ")
            if detail_input == "Y":
                all_history = open(check_name+".txt")
                read_history = all_history.read()
                print("sir your list is here:-- \n\n")
                print(read_history+"\n\n")
                all_history.close()
                all_name.close
            else:
                pass
        else:
            print("sorry your name is not in list...")

# op = open("tony.txt","r")
# ref = op.readline().replace("\t","")
# print(ref)
# if ref == "nameworkplace":
#     print("yes")
# else:
#     print("no")
# op.close()


# a = open("all_name.txt")
# b = a.read()
# print(b)