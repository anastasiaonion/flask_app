from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = b'd840d014a1de8cbb5b53f77a2c37e34c'


@app.route("/")
def index():
    if 'user_name' not in session:
        return redirect(url_for('login'))
    else:
        session['visits_count'] += 1
        visits_count = session['visits_count']
        user_name = session['user_name']
        return render_template('count_visits_page.html', user_name=user_name, visits_count=visits_count)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'user_name' not in session:
        user_name = request.form['user_name']
        session['user_name'] = user_name
        session['visits_count'] = 0
        return render_template('welcome_page.html', user_name=user_name)
    elif 'user_name' in session:
        return render_template('welcome_page.html', user_name=session['user_name'])
    else:
        return render_template('login_page.html')


@app.route("/logout")
def logout():
    'user_name' in session and session.pop('user_name')
    'visits_count' in session and session.pop('visits_count')
    return redirect(url_for('login'))


