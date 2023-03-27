from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def meke():
    # rqst = request.form['chur-form']
    # rqst1 = request.form['churr-form']
    # return f'<h1> {rqst}, {rqst1} </h1>'
    return render_template('index2.html')


if __name__ == '__main__':
    app.run(debug=True)
