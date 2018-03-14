'''Connection layer between the routes and the CSV handling layer.
It should have functions which can be called from the routing layer,
and they should call persistence layer functions.'''

from operator import itemgetter


def sort_list_of_dicts_by_time(dict_list):
    return sorted(dict_list, key=itemgetter('submission_time'))
