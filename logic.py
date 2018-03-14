'''Connection layer between the routes and the CSV handling layer.
It should have functions which can be called from the routing layer,
and they should call persistence layer functions.'''

from operator import itemgetter


def sort_list_of_dicts_by_time(dict_list):
    return sorted(dict_list, key=itemgetter('submission_time'))


def get_list_of_headers(dict_list):
    example_dict = dict_list[0]
    key_list = []
    for key in example_dict.keys():
        key_list.append(key)
    return key_list
