def read_file():
    filename = input("Enter the filename: ")
    try:
        with open(filename, "r") as file:
            data = file.read()
            print("File content:\n", data)
    except FileNotFoundError:
        print("Error: File not found.")
    except IOError:
        print("Error: File can't be read.")

read_file()