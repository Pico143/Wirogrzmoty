'''Flask stuff (server, routes, request handling, session, etc.)
This layer should only consist of logic that is hardly related to Flask.'''

from flask import Flask, render_template, request, redirect, url_for
import persistence
import logic
import util

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def list_questions(questions=None):
    questions = persistence.list_of_dict_from_file('Question.csv', fieldnames=None)
    questions = logic.sort_list_of_dicts_by_time(questions)
    return render_template('list_questions.html', questions=questions)


@app.route('/new-question')
def new_question():
    return render_template('ask_question.html')


@app.route('/question/<question_id>/new-answer)')
def post_answer(question_id=None):
    return render_template('post_answer.html', question_id=question_id)


@app.route('/question/<question_id>')
def view_question(question_id=None):
    return render_template('display_question.html', question_id=question_id)


if __name__ == '__main__':
    app.secret_key = 'some_key'
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
