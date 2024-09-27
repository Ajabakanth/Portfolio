from flask import Flask,render_template

app=Flask(__name__)

# @app.route('/')
# def homes():
#     return "<h1>Hi</h1>"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/education')
def education():
    return render_template('edu.html')

@app.route('/skills')
def skills():
    return render_template('intern.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/contact')
def contact():
    return render_template('cont.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')


if __name__=='__main__':
    app.run(debug=True)

