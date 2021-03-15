from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home_page():
    # Source files from https://github.com/html5up/identity
    return render_template('identity-master/index.html')


if __name__ == '__main__':
    app.run(debug=True)
