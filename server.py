'''Flask stuff (server, routes, request handling, session, etc.)
This layer should only consist of logic that is hardly related to Flask.'''

from flask import Flask, render_template, request, redirect, url_for
import persistence
import logic
import util

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def list_questions():
    questions = persistence.list_of_dict_from_file('Question.csv', fieldnames=None)
    questions = logic.sort_list_of_dicts_by_time(questions)
    labels = logic.get_list_of_headers(questions)
    return render_template('list_questions.html', questions=questions, labels=labels)


@app.route('/new-question')
def new_question():
    return render_template('ask_question.html')


@app.route('/new-question', methods=["POST"])
def submit_question():
    dict = logic.question_dict(request.form["title"], request.form["question"])
    persistence.write_form_to_file('Question.csv', util.QUEST_FIELDS, dict)
    return redirect('/list')


@app.route('/question/<int:question_id>/new-answer')
def write_answer(question_id):
    questions = persistence.list_of_dict_from_file('Question.csv', fieldnames=None)
    return render_template('post_answer.html', questions=questions, question_id=question_id)


@app.route('/question/<int:question_id>/new-answer', methods=['POST'])
def submit_answer(question_id):
    dict = logic.answer_dict(question_id, request.form['answer'])
    persistence.write_form_to_file('Answer.csv', util.ANS_FIELDS, dict)
    return redirect('/question/<question_id>')


@app.route('/question/<question_id>')
def view_question(question_id=None):
    questions = persistence.list_of_dict_from_file('Question.csv', fieldnames=None)
    questions_answer = persistence.list_of_dict_from_file('Answer.csv', fieldnames=None)
    questions_answer = logic.get_answers_in_question(questions_answer, question_id)
    labels = logic.get_list_of_headers(questions)
    labels_answer = logic.get_list_of_headers(questions_answer)
    return render_template('display_question.html', question_id=question_id,
                           questions=questions, labels=labels,
                           questions_answer=questions_answer, labels_answer=labels_answer)


if __name__ == '__main__':
    app.secret_key = 'some_key'
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
