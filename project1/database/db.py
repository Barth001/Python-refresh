database = []


def add_book(name, author):
    if len(database) < 1:
        database.append({"name": name, "author": author, "read": "Unread"})
        print("Name book added")
        return
    else:
        for data in database:
            if data["name"] == name and data["author"] == author:
                print(f"{name} by {author} is already in the database")
                return
        database.append({"name": name, "author": author, "read": "Unread"})
        print("New book added")
        return


def update_book(name, author):
    for data in database:
        if data["name"] == name and data["author"] == author:
            data["read"] = "Read"
            return
        print(f"{name} by {author} is not in the database")
        return


def view_books():
    print(database)
    for i, data in enumerate(database):
        print(f"{i + 1} --- {data['name'][i]} by {data['author'][i]} --> Read: {data['read'][i]}")
        return


def delete_book(name, author):
    for data in database:
        if data["name"] == name and data["author"] == author:
            data.remove()
            return
        print(f"{name} by {author} doesn't exist")
        return


def processing():
    file = input("Enter the name and the book\nand author separated by coma: ")
    book = file.split(",")
    if len(book) != 2:
        print("Enter the name and the book\nand author separated by coma: ")
        return
    return book[0], book[1]
