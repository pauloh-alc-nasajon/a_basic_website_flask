from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


# Defining the home page of our site
@app.route('/')  # this sets the route to this page
def home():
    return render_template('index.html', content='Testing')


@app.route('/<name>')
def user(name):
    return f'Hello {name}!'


@app.route('/admin')
def admin():
    return redirect(url_for('user', name='Admin!'))  # Now we when we go to /admin we will redirect to user with the argument "Admin!"


if __name__ == '__main__':
    app.run()
