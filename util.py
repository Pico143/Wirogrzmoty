'''Helper functions which can be called from any other layer.
(but mainly from the business logic layer)'''

# fieldnames:
QUEST_FIELDS = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']
ANS_FIELDS = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']
