from users_clases import Users
from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)


# home page
@app.route("/")
@app.route("/users")
def display_all_usesr():
    all_users = Users.get_all_users()
    return render_template("all_users.html", all_users=all_users)


# to add a new user
@app.route("/new/user")
def display_new_user():
    return render_template('add_new_user.html')


@app.route("/new/user", methods=["POST"])
def new_user():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
# you need to put the name of the class and the @classmethod that you are calling
    Users.add_new_user(data)
    return redirect("/users")

@app.route('/show/<int:user_id>')
# the parameter that you have here  has to mach on the url and inside of the dictionary
def show_one_user(user_id):
    data={
        'id': user_id
    }
    curent_user = Users.get_one_user(data)
#here we are just renaming the variable that we made before
    return render_template("show.html", user = curent_user)


@app.route("/edit/<int:num>")
def edit_one_user(num):
    data = {
        'id': num
    }
    user = Users.get_one_user(data)
    return render_template("edit.html" ,user = user)

@app.route("/edit/one_user/<int:num>",methods = ['post'])
def update_one_user_form(num):
    data = {
    'id': num,
    'first_name':request.form['first_name'],
    'last_name':request.form['last_name'],
    'email':request.form['email']
    }
    Users.update_one_user(data)
    return redirect("/users")

@app.route("/user/delete/<int:num>")
def delete_user(num):
    data = {
        "id": num
    }
    Users.delete_user(data)
    return redirect("/users")