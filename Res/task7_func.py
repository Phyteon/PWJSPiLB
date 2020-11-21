import io

# TODO: Fix the function!!!


def change_words(list, to_replace, file):
    with io.open(file, 'r', encoding='utf8') as f:
        text = f.read()
        if len(to_replace) == 0:
            i = 0
            while i < len(list):
                to_replace.append('')
                i += 1

        for (phrase, replacement) in zip(list, to_replace):
            text = text.replace(phrase, replacement)

    with io.open(file, 'w', encoding='utf8') as f_prim:
        f_prim.write(text)
