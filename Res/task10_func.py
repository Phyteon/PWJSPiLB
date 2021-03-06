
import copy


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
        if len(aux) > 0:
            buckets.append(aux)

    n_of_digit = -2  # Indexing from the end of the string (LSD)
    while True:
        control = 0
        aux_buckets = []
        for nd in range(0, 10):
            wtf = copy.deepcopy(buckets)
            aux = []
            for nested in buckets:
                if len(nested) > 0:
                    for element in nested:
                        global_idx = buckets.index(nested)
                        if -n_of_digit > len(element):
                            control += 1
                            local_idx = wtf[global_idx].index(element)
                            aux.append(element)
                            wtf[global_idx].pop(local_idx)
                        elif str(nd) == element[n_of_digit]:
                            local_idx = wtf[global_idx].index(element)
                            aux.append(element)
                            wtf[global_idx].pop(local_idx)

            if len(aux) > 0:
                aux_buckets.append(aux)
            buckets = wtf
        buckets = aux_buckets
        if control == volume:
            break
        else:
            control = 0
            n_of_digit -= 1
    srtd = []
    for elem_list in buckets:
        if len(elem_list) > 0:
            for elem in elem_list:
                srtd.append(int(elem))
    return srtd
