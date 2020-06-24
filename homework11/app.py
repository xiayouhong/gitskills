# -*- coding: utf-8 -*-
# @Time    : 2020/5/17 10:51
# @Author  : xyh
from flask import Flask, request, render_template,redirect,url_for
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

                return redirect(url_for('choose',username=username))

        return render_template('form.html', message='Bad username or password', username=username)
    except Exception as e:
        print(e)
    # finally:
    #     session.close()


@app.route('/choose/<username>/',methods=['GET'])
def choose(username):
    try:
        subjects = session.query(subject).all()
        stu_timetable = session.query(timetable).filter_by(id=username).one()
        stu_timelist = []
        stu_timelist.append(stu_timetable.mon)
        stu_timelist.append(stu_timetable.tue)
        stu_timelist.append(stu_timetable.wed)
        stu_timelist.append(stu_timetable.thu)
        stu_timelist.append(stu_timetable.fri)
        stu_timelist.append(stu_timetable.sat)
        stu_timelist.append(stu_timetable.sun)
        subjectlists = []
        for i in subjects:
            subjectlist = []
            subjectlist.append(i.id)
            subjectlist.append(i.sub)
            subjectlist.append(i.time)
            subjectlist.append(i.selected)
            if i.sub in stu_timelist:
                subjectlist.append('是')
            else:
                subjectlist.append('否')
            subjectlists.append(subjectlist)

        return render_template('signin-ok.html', username=username, subjects=subjectlists)

    except Exception as e:
        print(e)


@app.route('/select/<username>/<id>/',methods=['GET','POST'])
def select(username,id):
    try:
        sub = session.query(subject).filter_by(id=id).one()
        stu_timetable = session.query(timetable).filter_by(id=username).one()
        if sub.time == 'mon':
            stu_time = stu_timetable.mon
        elif sub.time == 'tue':
            stu_time = stu_timetable.tue
        elif sub.time == 'wed':
            stu_time = stu_timetable.wed
        elif sub.time == 'thu':
            stu_time = stu_timetable.thu
        elif sub.time == 'fri':
            stu_time = stu_timetable.fri
        elif sub.time == 'sat':
            stu_time = stu_timetable.sat
        else:
            stu_time = stu_timetable.sun

        if not stu_time:
            session.query(timetable).filter_by(id=username).update({sub.time : sub.sub})
            session.commit()
            session.query(subject).filter_by(id=id).update({'selected': sub.selected+1})
            session.commit()
        return redirect(url_for('choose', username=username))

    except Exception as e:
        print(e)
@app.route('/notselect/<username>/<id>/',methods=['GET','POST'])
def notselect(username,id):
    try:
        sub = session.query(subject).filter_by(id=id).one()
        print(sub.time)
        stu_timetable = session.query(timetable).filter_by(id=username).one()
        if sub.time == 'mon':
            stu_time = stu_timetable.mon
        elif sub.time == 'tue':
            stu_time = stu_timetable.tue
        elif sub.time == 'wed':
            stu_time = stu_timetable.wed
        elif sub.time == 'thu':
            stu_time = stu_timetable.thu
        elif sub.time == 'fri':
            stu_time = stu_timetable.fri
        elif sub.time == 'sat':
            stu_time = stu_timetable.sat
        else:
            stu_time = stu_timetable.sun
        if stu_time == sub.sub:
            session.query(timetable).filter_by(id=username).update({sub.time: None})
            session.commit()
            session.query(subject).filter_by(id=id).update({'selected': sub.selected - 1})
            session.commit()
        return redirect(url_for('choose', username=username))
    except Exception as e:
        print(e)

if __name__ == '__main__':
    app.run()
    session.close()