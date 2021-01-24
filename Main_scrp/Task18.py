from Res.task18_func import print_data, save_json, open_json, add_note, remove_note


def main():

    path = "files/data_file.json"
    data = open_json(path)

    while(True):
        print_data(data)
        print("\n" + "What do You want to do: ")
        print("\t" + "1. Add note")
        print("\t" + "2. Remove note")
        print("\t" + "0. Exit")
        choice = int(input("Choose number: "))
        if choice == 1:
            data.append(add_note())
        elif choice == 2:
            data.pop(remove_note())
        elif choice == 0:
            break

    save_json(data, path)


if __name__ == '__main__':
    main()