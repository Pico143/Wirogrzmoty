'''Connection layer between the routes and the CSV handling layer. 
It should have functions which can be called from the routing layer, 
and they should call persistence layer functions.'''

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