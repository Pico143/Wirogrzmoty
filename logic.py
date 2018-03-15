'''Connection layer between the routes and the CSV handling layer.
It should have functions which can be called from the routing layer,
and they should call persistence layer functions.'''
import persistence
import util
import os.path
import base64
from operator import itemgetter
from datetime import datetime


def get_id(list_dict):
    if len(list_dict) > 0:
        return int(list_dict[-1]['id']) + 1
    else:
        return 0


def answer_dict(question_id, answer):
    answer_dict = {
        'id': get_id(persistence.list_of_dict_from_file('Answer.csv', util.ANS_FIELDS)),
        'submission_time': os.path.getmtime('Answer.csv'),
        'vote_number': 0,
        'question_id': question_id,
        'message': stringToBase64(answer),
        'image': ''
    }

    return answer_dict

def question_dict(question, message):
    ['id','submisson_time','view_number','vote_number','title', 'message', 'image']
    question_dict={
        'id': get_id(persistence.list_of_dict_from_file('Question.csv', util.QUEST_FIELDS)),
        'submisson_time': os.path.getmtime('Question.csv'),
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


def stringToBase64(string):
    return base64.b64encode(string.encode('utf-8'))


def base64ToString(b):
    return base64.b64decode(b).decode('utf-8')
