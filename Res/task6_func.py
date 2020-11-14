import os, os.path


def translate_user_input(file_type):
    print('Please specify files or whole directory (with absolute paths) that you wish to convert.')
    print('Please note that all files of specified type in given directory will be converted.\n')
    print('To stop specifying files, please type \'s\'\n')
    files_to_convert = []
    file_path = input()
    if os.path.isdir(file_path):
        all_files = os.listdir(file_path)
        for file in all_files:
            if os.path.isfile(file_path + '\\' + file) and os.path.splitext(file)[1] == file_type:
                files_to_convert.append(file_path + '\\' + file)
        if len(files_to_convert) == 0:
            print('No files in given directory are of specified type.')
    else:
        while file_path != 's':
            if os.path.isfile(file_path) and os.path.splitext(file_path)[1] == file_type:
                files_to_convert.append(file_path)
            else:
                print('Specified path does not exist or does not point to a valid file!')
            file_path = input()
    return files_to_convert
