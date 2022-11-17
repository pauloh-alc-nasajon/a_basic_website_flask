from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


# Defining the home page of our site
@app.route('/')  # this sets the route to this page
def home():
    return render_template('index.html')


@app.route('/<usr>')
def user(usr):
    return f'<h1>{usr}</h1>'


@app.route('/admin')
def admin():
    return redirect(url_for('user', usr='Admin!'))  # Now we when we go to /admin we will redirect to user with the argument "Admin!"


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('user', usr=user))
    else:
        return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
