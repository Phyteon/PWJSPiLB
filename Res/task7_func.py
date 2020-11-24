import io

# TODO: Fix the function!!!


def change_words(dictionary, file):
    with io.open(file, 'r', encoding='utf8') as f:
        text = f.read()
        lst_of_words = text.split()
        indices = {}
        for i in range(0, len(lst_of_words)):
            indices[str(i)] = 0
        for phrase, replacement in dictionary.items():
            aux = [i for i, x in enumerate(lst_of_words) if x == phrase]
            for i in aux:
                indices[str(i)] += 1
                if indices[str(i)] < 2:
                    lst_of_words[i] = replacement
        text = ' '.join(lst_of_words)

    with io.open(file, 'w', encoding='utf8') as f_prim:
        f_prim.write(text)
