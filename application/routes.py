from application import app
from flask import render_template, request
from courses import courseData

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', login=True)

@app.route('/courses')
@app.route('/courses/<term>')
def courses(term=2019):
    return render_template('courses.html', login=False, coursesData=courseData, term=term)

@app.route('/login')
def login():
    return render_template('login.html', login=False)

@app.route('/register')
def register():
    return render_template('register.html', login=False)

@app.route('/enrollment')
def enrollment():
    new_course = []
    for c in courseData:
        if request.args.get('courseID') == c['courseID']:
            new_course = c
            break
    return render_template('enrollment.html', course=new_course)