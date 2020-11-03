import os, os.path


def list_dir(path):
    read = os.listdir(path)
    spacers = len(path.split("\\"))
    buff = (spacers - 1) * "| "
    for name in read:
        if (path + "\\" + name).isdir:
            print(buff + "|--" + name)
            content = os.listdir(path + "\\" + name)
            for cont in content:
                if (path + "\\" + name + "\\" + cont).isdir:
                    list_dir(path + "\\" + name + "\\" + cont)
                else:
                    print(buff + "| " + cont)
        else:
            print(buff + name)