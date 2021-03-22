from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():

    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up',  methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater then 3 characters', category='error')
        elif len(firstName) < 2:
            flash('Please enter your real name',  category='error')
        elif len(password1) < 6:
            flash('The password must be at least 5 characters',  category='error')
        elif password1 != password2:
            flash('The passwords do not match',  category='error')
        else:
            flash('Account created',  category='success')
    return render_template("signup.html")