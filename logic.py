'''Connection layer between the routes and the CSV handling layer.
It should have functions which can be called from the routing layer,
and they should call persistence layer functions.'''

from operator import itemgetter

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

    return answer_dict

def question_dict(question, message):
    ['id','submisson_time','view_number','vote_number','title', 'message', 'image']
    question_dict={
        'id':0,
        'submisson_time': 0,
        'view_number': 0,
        'vote_number': 0,
        'title': question,
        'message': message,
        'image': ''
    }

    return question_dict

def sort_list_of_dicts_by_time(dict_list):
    return sorted(dict_list, key=itemgetter('submission_time'))


def get_list_of_headers(dict_list):
    example_dict = dict_list[0]
    key_list = []
    for key in example_dict.keys():
        key_list.append(key)
    return key_list
