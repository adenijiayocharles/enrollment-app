from application import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', login=True)

@app.route('/courses')
def courses():
    courseData = [
        {
            "courseID": "CS101",
            "title": "Introduction to Computer Science",
            "credits": 3,
            "term": "Fall 2024",
            "description": "An introductory course covering the basics of computer science, including algorithms, data structures, and programming languages."
        },
        {
            "courseID": "MATH201",
            "title": "Calculus I",
            "credits": 4,
            "term": "Spring 2024",
            "description": "A first course in calculus, covering limits, derivatives, integrals, and applications of calculus in various fields."
        },
        {
            "courseID": "ENG102",
            "title": "English Composition",
            "credits": 3,
            "term": "Fall 2024",
            "description": "A course designed to improve students' writing skills, focusing on composition, grammar, and critical thinking."
        },
        {
            "courseID": "PHY150",
            "title": "Physics I: Mechanics",
            "credits": 4,
            "term": "Fall 2024",
            "description": "An introduction to classical mechanics, covering topics such as Newton's laws, work, energy, and momentum."
        },
        {
            "courseID": "HIST101",
            "title": "World History",
            "credits": 3,
            "term": "Spring 2024",
            "description": "A survey course exploring major events, figures, and themes in world history from ancient times to the modern era."
        },
        {
            "courseID": "CHEM105",
            "title": "General Chemistry",
            "credits": 4,
            "term": "Fall 2024",
            "description": "A comprehensive introduction to the principles of chemistry, including atomic structure, chemical bonding, and reactions."
        },
        {
            "courseID": "BIO110",
            "title": "Introduction to Biology",
            "credits": 3,
            "term": "Spring 2024",
            "description": "An introductory course in biology, covering cellular biology, genetics, evolution, and the diversity of life."
        }
    ]
    return render_template('courses.html', login=False, coursesData=courseData)

@app.route('/login')
def login():
    return render_template('login.html', login=False)

@app.route('/register')
def register():
    return render_template('register.html', login=False)