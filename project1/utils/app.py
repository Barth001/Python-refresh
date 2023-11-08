from project1.database.db import *
import sys

CHOICE = """
Press: 
'l' To list all books
'a' To add book
'd' To remove book
'u' To update book status to read
'q' To quit
"""


def start():
    while True:
        user_input = input(CHOICE)
        if user_input.lower() == 'q':
            print("BYE!")
            break
        if user_input.lower() == 'a':
            name, author = processing()
            add_book(name, author)
        elif user_input.lower() == 'l':
            view_books()
        elif user_input.lower() == 'u':
            name, author = processing()
            update_book(name, author)
        elif user_input.lower() == 'd':
            name, author = processing()
            update_book(name, author)
        else:
            print(CHOICE)


if __name__ == "__main__":
    start()
