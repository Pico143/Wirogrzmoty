'''The layer that have access to any kind of long term data storage.
In this case, we use CSV files, but later on we'll change this to SQL database.
So in the future, we only need to change in this layer.'''

import csv
import base64


def write_form_to_file(filename, fieldnames, dict):
    encoding_dict(dict)
    with open(filename, 'a') as f:
        w = csv.DictWriter(f, fieldnames)
        w.writerow(dict)


def list_of_dict_from_file(filename, fieldnames):
    try:
        with open(filename) as f:
            reader = csv.DictReader(f, fieldnames)
            dics = [decoding_dict(d) for d in reader]
            return dics
    except FileNotFoundError:
        with open(filename, "w") as f:
            w = csv.DictWriter(f, fieldnames)
        return {}


def del_row_in_file(filename, fieldnames, row_number, row_id):
    list_dict = list_of_dict_from_file(filename, fieldnames)
    new_list = []
    for item in list_dict:
        if not str(item[row_id]) == str(row_number):
            new_list.append(item)
    with open(filename, 'w') as f:
        w = csv.DictWriter(f, fieldnames)
        w.writerows(new_list)


def replace_row_in_file(filename, fieldnames, row_number, dict):
    list_dict = list_of_dict_from_file(filename, fieldnames)
    list_dict[row_number] = encoding_dict(dict)
    with open(filename, 'w') as f:
        w = csv.DictWriter(f, fieldnames)
        w.writerows(list_dict)


def decoding_dict(dict):
    for i in dict:
        print (i)
        print(dict[i])
        if i in ['title', 'message', 'image']:
           dict[i]=base64ToString(bytes(dict[i][2:-1], "utf-8"))
    return dict

def encoding_dict(dict):
    for i in dict:
        print (i)
        print(dict[i])
        if i in ['title', 'message', 'image']:
           dict[i]=stringToBase64(dict[i])
    return dict



def stringToBase64(string):
    return base64.b64encode(string.encode('utf-8'))


def base64ToString(b):
    return base64.b64decode(b).decode('utf-8')
