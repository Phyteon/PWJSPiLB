import os, os.path


def list_dir(path):
    read = os.listdir(path)
    spacers = len(path.split("\\"))
    buff = (spacers - 1) * "| "
    for name in read:
        if os.path.isdir(path + "\\" + name):
            print(buff + "--" + name)
            content = os.listdir(path + "\\" + name)
            for cont in content:
                if os.path.isdir(path + "\\" + name + "\\" + cont):
                    list_dir(path + "\\" + name + "\\" + cont)
                else:
                    print(buff + "| " + cont)
        else:
            print(buff + name)