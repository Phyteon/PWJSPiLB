
from PIL import Image
from Res.task6_func import translate_user_input
import os, os.path


files_to_translate = translate_user_input('.jpg')
if len(files_to_translate) == 0:
    print("No files specified.")
else:
    print('Please specify target directory for converted files:\n')
    target_dir = input()
    for file in files_to_translate:
        img = Image.open(file)
        base_name = os.path.basename(file)
        name_without_type = os.path.splitext(base_name)[0]
        new_name = target_dir + '\\' + 'CONV_' + name_without_type + '.png'
        img.save(new_name)
    print('Finished conversion.\n')
