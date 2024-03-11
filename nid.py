nid = []
# patched the error and added a few extra features
def add_entry(entry):
    nid.append(entry)

def display_entry():
    for item in nid:
        print(item)

def delete_entry(entry):
    nid.remove(entry)

def update_entry(entry, new_entry):
    for i in range(len(nid)):
        if nid[i] == entry:
            nid[i] = new_entry


while True:
    try:
        user_input = input("Enter 1 to add, 2 to display, 3 to delete and 4 to update: ")

        if user_input == "1":
            add_num = input("Enter NID num: ")
            add_entry(add_num)
        elif user_input =="2":
            display_entry()
        elif user_input =="3":
            remove_num = input("Enter NID num that you want to remove: ")
            delete_entry(remove_num)
        elif user_input=="4":
            num_to_update = input("Enter the number you want to remove: ")
            enter_new_num = input("Enter new number: ")
            update_entry(num_to_update,enter_new_num)
        else:
            print("Invalid entry!")
    except Exception as ex:
        print("Something went wrong")
