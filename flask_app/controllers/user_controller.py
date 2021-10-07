from flask_app import app
from flask import redirect, render_template, session, request, url_for
from flask_app.models.user import User


@app.route('/')
def index():
    headerText = session['header'] = "Welcome to User's List"
    isHome = session['isHome'] = "true"
    return render_template('index.html', headerText=headerText, isHome=isHome)


@app.route('/users')
def all_users():
    all_users = User.get_all()
    print(f" this is variable {all_users}")
    isGetUser = session['isGetUser'] = 'true'
    return render_template('index.html', isGetUser=isGetUser, all_users=all_users)


@app.route('/user/new')
def will_add_user():
    isGetUser = session['isGetUser'] = 'false'
    isAddUser = session['isAddUser'] = 'true'
    headerText = session['header'] = "Add User"
    isHome = session['isHome'] = "false"
    return render_template('index.html', isGetUser=isGetUser, isAddUser=isAddUser, headerText=headerText, isHome=isHome)


@app.route('/user/add', methods=['POST'])
def add_user():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.add_user(data)
    return redirect('/users')


@app.route('/show_user/<int:user_id>')
def show_user(user_id):
    data = {
        'id': user_id
    }
    one_user = User.get_user(data)
    return render_template('user.html', one_user=one_user)


@app.route('/edit/<int:user_id>')
def edit(user_id):
    data = {
        "id": user_id
    }
    one_user = User.get_user(data)
    return render_template('edit.html', one_user=one_user)


@app.route('/edit/update/<int:user_id>', methods=['POST'])
def edit_user(user_id):

    data = {
        'id': user_id,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.edit_user(data)
    return redirect('/users')

@app.route('/delete/<int:user_id>')
def delete(user_id):
    data = {
        "id": user_id
    }
    User.delete_user(data)
    return redirect('/users')