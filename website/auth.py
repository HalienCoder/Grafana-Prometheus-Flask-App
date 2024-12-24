from flask import Blueprint,render_template,request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    
    #when we use the request variable inside the route, it will have information about the request that was sent to access the route, like the URL, the method, all the info that was sent
    # the form attirubte of the request has all of the data that was sent as a part of a form.
    # LINE OF CODE => data=request.form

    if request.method =='POST':
        email = request.form.get('email')
        password = request.form.get('password')

    
    return render_template("login.html", text="sample text", user="tim")

@auth.route('/logout')
def logout():
    return "<p>Hellooo</p>"

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method =='POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) <4 :
            flash('Email must be greater than 4 characters.', category='error')
        elif len(firstName) < 4 :
            flash('First name must be greater than 4 characters', category='error')
        elif password1 != password2:
            flash("Passwords do not match", category='error')
        elif len(password1) < 7 :
            flash('Password must be greater than 7 charcaters.', category='error')
        else:
            #add user to db
            flash ('Account created!', category='success')
    return render_template("signup.html")