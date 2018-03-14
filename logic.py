'''Connection layer between the routes and the CSV handling layer.
It should have functions which can be called from the routing layer,
and they should call persistence layer functions.'''
import persistence
import util
from operator import itemgetter

def get_id(list_dict):
        return len(list_dict)

def answer_dict(question_id, answer):
    ['id','submisson_time','vote_number','question_id','message','image']
    answer_dict={
        'id':0,
        'submisson_time': 0,
        'vote_number': 0,
        'question_id': question_id,
        'message' : answer,
        'image' : ''        
    }
    answer_dict['id'] = get_id(persistence.list_of_dict_from_file('Answer.csv',util.ANS_FIELDS))

    return answer_dict


def sort_list_of_dicts_by_time(dict_list):
    return sorted(dict_list, key=itemgetter('submission_time'))
