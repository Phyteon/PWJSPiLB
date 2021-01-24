import json
import os


def print_data(data):
    for a in range(len(data)):
        print("\nNo. " + str(a+1))
        print("name:", data[a]["name"])
        print("description:", data[a]["description"])
        print("date:", data[a]["date"])


def save_json(data, path):
    with open(path, "w") as file:
        json.dump(data, file, indent=4)


def open_json(path):
    if os.path.isfile(path):
        with open(path, "r") as file:
            return json.load(file)
    else:
        return []


def add_note():
    print()
    name = input("\t" + "name: ")
    des = input("\t" + "description: ")
    date = input("\t" + "date: ")

    note = {"name": name, "description": des, "date": date}
    return note


def remove_note():
    print()
    n = int(input("\t" + "Which one u want to remove?: "))
    return n - 1
