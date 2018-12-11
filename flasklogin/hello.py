from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'Hello'


@app.route('/login/')
@app.route('/login/<username>')
def display_user(username=None):
    return render_template('layout.html', username=username)


@app.route('/<int:dis_id>')
def display_id(dis_id):
    return "Id owner: {}".format(dis_id)

