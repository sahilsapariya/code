'''login for students, admin to their portal. 
This file is made by programmer.'''

import sqlite3
from flask import (
            Flask,
            render_template, 
            request, 
            url_for, 
            redirect, 
            abort, 
            session 
)
from flask_sqlalchemy import SQLAlchemy
import uuid
from admin import admin_file
from flask_sessionstore import Session
from flask_session_captcha import FlaskSessionCaptcha


app = Flask(__name__)
db = SQLAlchemy(app)
app.register_blueprint(admin_file)

app.config["SECRET_KEY"] = uuid.uuid4()
app.config['CAPTCHA_ENABLE'] = True
app.config['CAPTCHA_LENGTH'] = 5
app.config['CAPTCHA_WIDTH'] = 260
app.config['CAPTCHA_HEIGHT'] = 100
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
# In case you want to use another key in your session to store the captcha:
app.config['CAPTCHA_SESSION_KEY'] = 'captcha_image'
app.config['SESSION_TYPE'] = 'sqlalchemy'
Session(app)
captcha = FlaskSessionCaptcha(app)

def get_data(name):
    conn = get_db_connection()
    data = conn.execute("SELECT * FROM userlist WHERE _name=?", (name,)).fetchone()
    conn.close()
    if data is None:
        abort(404)
    return data

def get_db_connection():
    conn = sqlite3.connect("C:\\Users\\jsk\\Desktop\\school project\\code\\code\\database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    list = conn.execute('SELECT * FROM userlist').fetchall()
    conn.close()
    return render_template("index.html", list=list)


@app.route('/login/', methods=('GET', 'POST'))
def login():
    session.pop('admin', None)
    session.pop('student', None)
    if request.method == 'POST':

        if captcha.validate():
            username = request.form['username']
            password = request.form['password']
            
            conn = get_db_connection()
            data = conn.execute('SELECT * FROM userlist WHERE _name=? AND _password=?', (username, password)).fetchone()
            if data is None:
                abort(404)
            if data['isAdmin']:
                session['admin'] = data['_name']
                conn.close()
                return redirect(url_for('home', name=data['_name']))
            else:   
                session['student'] = data['_name']
                conn.close()
                return redirect(url_for('home', name=data['_name']))
        else:
            return redirect(url_for('login')) 

    return render_template("login_page.html")


@app.route('/<name>/home/')
def home(name):
    data = get_data(name)
    if data['_name'] == session.get('student'):
        conn = get_db_connection()
        s_profile = conn.execute('SELECT * FROM studentprofile WHERE s_fname=?', (name,)).fetchone()
        s_contact = conn.execute('SELECT * FROM student_contact WHERE s_fname=?', (name,)).fetchone()
        conn.commit()
        conn.close()
        return render_template('student_homepage.html', list=data, details=s_profile, contacts=s_contact)

    elif data['_name'] == session.get('admin'):
        conn = get_db_connection()
        a_profile = conn.execute('SELECT * FROM adminprofile WHERE a_fname=?', (name,)).fetchone()
        conn.commit()
        conn.close()
        return render_template('admin_homepage.html', list=data, details=a_profile)
    else:
        return redirect(url_for('login'))

@app.route('/<id>/hall-ticket/')
def HallTicket(id):
    data = get_data(id)
    if data['_name'] == session.get('student'):
        return render_template('hallticket_stu.html', list=data)
    else:
        return abort(404)



@app.route('/<name>/hallticket-download/<exam_code>/')
def DownloadHallTicket(exam_code, name):
    conn = get_db_connection()
    s_data = conn.execute("SELECT s_fname, s_mname, s_lname, standard, permenent_id FROM studentprofile WHERE s_fname = ?", (name))
    exam_data = conn.execute("SELECT * FROM 'Hall Ticket' WHERE 'Exam Code' = ?", (exam_code))


    return render_template('hallticket.html', s_data=s_data, data=exam_data)





@app.route('/<name>/fee-voucher/')
def FeeVoucher(name):
    data = get_data(name)
    if(data['_name'] == session.get('student')):
        return render_template('fee-voucher-student.html', list=data)
    else:
        return abort(404, "Student fee voucher page does not found")

@app.route('/<name>/examresult/')
def ExamResult(name):
    data = get_data(name)
    if(data['_name'] == session.get('student')):
        return render_template('examresult_student.html', list=data)
    else:
        return abort(404, "Student examresult page does not found")


@app.route('/<name>/mysubjects/')
def MySubjects(name):
    data = get_data(name)
    if data['_name'] == session.get('student'):
        conn = get_db_connection()
        subject = conn.execute("SELECT * FROM 'Subjects'").fetchall()
        conn.commit()
        conn.close()
        return render_template('subjects.html', subjects=subject, list=data)
    else:
        return abort(404)

@app.route('/logout')
def logout():
    session.pop('student', None)
    session.pop('admin', None)

    return redirect(url_for('login'))


app.run(debug=True, use_reloader=True)
