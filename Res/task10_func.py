
def radix_lsd_sort(data):
    volume = len(data)
    sym_data = []
    for integer in data:
        sym_data.append(str(integer))

    # Pre-sorting data
    buckets = []
    for lsd in range(0, 10):
        aux = []
        for element in sym_data:
            if element[-1] == str(lsd):
                aux.append(element)
        buckets.append(aux)

    n_of_digit = -2  # Indexing from the end of the string (LSD)
    while True:
        control = 0
        aux_buckets = []
        for nd in range(0, 10):
            aux = []
            for nested in buckets:
                for element in nested:
                    if -n_of_digit > len(element):
                        control += 1
                        local_idx = nested.index(element)
                        if len(aux_buckets) == 0:
                            aux_buckets.append([nested.pop(local_idx)])
                        elif len(aux_buckets[0][0]) < -n_of_digit: # TODO: Debug this section (string index out of range?)
                            aux_buckets[0].append(nested.pop(local_idx))
                        elif aux_buckets[0][0][n_of_digit] == '0':
                            aux_buckets[0].append(nested.pop(local_idx))
                        else:
                            aux_buckets.insert(0, [nested.pop(local_idx)])
                    elif str(nd) == element[n_of_digit]:
                        local_idx = nested.index(element)
                        aux.append(nested.pop(local_idx))
            aux_buckets.append(aux)
        buckets = aux_buckets
        if control == volume:
            break
        else:
            n_of_digit -= 1
    srtd = []
    for elem_list in buckets:
        for elem in elem_list:
            srtd.append(int(elem))
    return srtd
