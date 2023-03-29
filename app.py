from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Amy Chen! I am adding my first code change.'

@app.route('/hello')
def hello():  # put application's code here
    return render_template('hello.html')

@app.route('/about')
def about():  # put application's code here
    return render_template('about.html')

@app.route('/favorite-course', methods=['GET', 'POST'])
def favorite_course():
    if request.method == 'POST':
        return render_template('favorite-course.html', form_submitted=True)
    else:
        return render_template('favorite-course.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        print('First name entered: ' + request.form.get('first_name'))
        print('Last name entered: ' + request.form.get('last_name'))
        print('Email entered: ' + request.form.get('email'))
        print('Phone number entered: ' + request.form.get('phone'))
        return render_template('contact.html', form_submitted=True)
    else:
        return render_template('contact.html')



if __name__ == '__main__':
    app.run()