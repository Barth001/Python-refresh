r_file = open("data.txt", "r")
info = r_file.read()
print(info)
r_file.close()

name = input("Enter your name: ")
w_file = open("data.txt", "a")
info = w_file.writelines(f"{name}\n")
w_file.close()