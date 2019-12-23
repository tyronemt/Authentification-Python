
dict = {}

def create(key,value):
    if key not in dict.keys():
        dict[key] = value
        print("CREATED")
    else:
        print("USERNAME already exist")
        
def login(key,value):
    if key in dict.keys():
        if dict[key] == value:
            print("SUCCEEDED")
        else:
            print("FAILED")
    else:
        print("FAILED")

def remove(key):
    if key in dict.keys():
        dict.remove(key)
    else:
        print("NONEXISTENT")

def clear():
    temp = dict.keys()
    if len(temp) != 0:
        for i in temp:
            dict.remove(i)
    print("CLEARED")




if __name__ == '__main__':
    user_input = "START"
    while user_input != "QUIT":
        user_input = input()
        user_split = user_input.split(" ")
        if user_split[0] == "CREATE":
            if len(user_split) == 3:
                create(user_split[1],user_split[2])
            else:
                print("INVALID")
        elif user_split[0] == "LOGIN":
            if len(user_split) == 3:
                login(user_split[1],user_split[2])
            else:
                print("INVALID")
        elif user_split[0] == "REMOVE":
            if len(user_split) == 2:
                remove(user_split[1])
            else:
                print("INVALID")
        elif user_input == "CLEAR":
            clear()
        elif user_input == "QUIT":
            pass
        else:
            print("INVALID")
