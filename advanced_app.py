from flask import Flask, render_template, redirect, url_for
from time import gmtime, strftime
app = Flask(__name__)

@app.route('/profile')
def profile():
    timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    return render_template('advanced_profile.html', timestamp=timestamp)

@app.route('/')
def index():
    return redirect(url_for('profile'))

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
