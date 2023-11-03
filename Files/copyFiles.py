# Check for friends
def friends():
    while True:
        print("Enter no to exit...")
        user_input = input("Enter a name: ")
        if user_input.lower() == "no":
            print("BYE...")
            break
        peoples = people()
        if user_input.title() in peoples:
            add_friends(user_input.title())
            print(user_input.title(), "is your friend")
        else:
            print(user_input.title(), "is not your friend")


# Add find friends to friend db
def add_friends(data):
    friends_files = open("friend.txt", "a")
    friends_files.write(f"{data}\n")
    friends_files.close()


# Reading people's db
def people():
    db = []
    people_files = open("people.txt", "r")
    peoples_db = people_files.readlines()
    people_files.close()
    for people_lis in peoples_db:
        new_people = people_lis.split("\n")
        db.append(new_people[0])
    print(db)
    return db


if __name__ == "__main__":
    friends()
