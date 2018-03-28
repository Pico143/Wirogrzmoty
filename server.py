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
    questions = persistence.get_all_questions()
    questions = logic.sort_list_of_dicts_by_time(questions)
    labels = logic.get_list_of_headers(questions)
    return render_template('list_questions.html', questions=questions, labels=labels, search=False)


@app.route('/new-question')
def new_question():
    return render_template('ask_question.html')


@app.route('/new-question', methods=["POST"])
def submit_question():
    dict = logic.question_dict(request.form["title"], request.form["question"])
    persistence.add_row_to_db(dict, "question")
    return redirect('/list')


@app.route('/question/<int:question_id>/new-answer')
def write_answer(question_id):
    questions = persistence.get_all_questions()
    return render_template('post_answer.html', questions=questions, question_id=question_id)


@app.route('/question/<int:question_id>/new-answer', methods=['POST'])
def submit_answer(question_id):
    dict = logic.answer_dict(question_id, request.form['answer'])
    persistence.add_row_to_db(dict, "answer")
    return redirect('/question/' + str(question_id))


@app.route('/delete/<int:question_id>')
def delete_question(question_id=None):
    persistence.delete_item('question', question_id)
    return redirect('/')


@app.route('/question/<question_id>')
def view_question(question_id=None):
    question = persistence.get_item_by_id("question", question_id)
    questions_answer = persistence.get_item_by_question_id('answer', question_id)
    labels = logic.get_list_of_headers(question)
    labels_answer = logic.get_list_of_headers(questions_answer)
    return render_template('display_question.html', question=question, questions_answer=questions_answer,
                           labels=labels, question_id=question_id, labels_answer=labels_answer)


@app.route('/question/<int:question_id>/vote-up')
def vote_question_up(question_id=None):
    logic.vote_question(question_id, True)
    return redirect('/question/' + str(question_id))


@app.route('/question/<int:question_id>/vote-down')
def vote_question_down(question_id=None):
    logic.vote_question(question_id, False)
    return redirect('/question/' + str(question_id))


@app.route('/question/<int:question_id>/<int:answer_id>/vote-up')
def vote_answer_up(question_id=None, answer_id=None):
    logic.vote_answer(answer_id, True)
    return redirect('/question/' + str(question_id))


@app.route('/question/<int:question_id>/<int:answer_id>/vote-down')
def vote_answer_down(question_id=None, answer_id=None):
    logic.vote_answer(answer_id, False)
    return redirect('/question/' + str(question_id))


@app.route('/search', methods=["POST", "GET"])
def search():
    questions = persistence.search(search=request.form)
    if questions:
        questions = logic.sort_list_of_dicts_by_time(questions)
        labels = logic.get_list_of_headers(questions)
        return render_template('list_questions.html', questions=questions, labels=labels, search=True)
    else:
        return render_template('search_failed.html', term=request.form['search_questions'])


if __name__ == '__main__':
    app.secret_key = 'some_key'
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
