# -*- coding: utf-8 -*-
# @Time    : 2020/5/17 10:51
# @Author  : xyh
from flask import Flask, request, render_template
from model.db import session,student,subject,timetable

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    try:
        username = request.form['username']
        password = request.form['password']
        stulist = session.query(student).all()
        for i in stulist:
            if i.id == username and i.password == password:
                return render_template('signin-ok.html', username=i.name)
        return render_template('form.html', message='Bad username or password', username=username)
    except Exception as e:
        print(e)
    finally:
        session.close()


@app.route('/signin/choose',methods=['GET','POST'])
def choose():
    try:






    except Exception as e:
        print(e)



if __name__ == '__main__':
    app.run()