from flask import render_template, request, Blueprint

users = {
    'admin': 'admin',
    'rafael': '12345',
    'mateus': '54321'
}

user = Blueprint("user", __name__)

@user.route('/register_user')
def register_user():
    return render_template("users/register_user.html")

@user.route('/add_user', methods=['GET','POST'])
def add_user():
    global users
    if request.method == 'POST':
        user = request.form['user']
    else:
        user = request.args.get('user', None)
    users[user] = '0000'
    return render_template("users/users.html", users=users)

@user.route('/list_users')
def list_users():
    global users
    return render_template("users/users.html", users=users)

@user.route('/remove_user')
def remove_user():
    removable_users = {key: value for key, value in users.items() if key != "admin"}
    return render_template("users/remove_user.html", users=removable_users)

@user.route('/del_user', methods=['GET','POST'])
def del_user():
    global users
    if request.method == 'POST':
        if request.form['user'] == "admin":
            return "O usuário 'admin' não pode ser deletado!", 403
        else:
            user = request.form['user']
    else:
        user = request.args.get('user', None)
    users.pop(user)
    return render_template("users/users.html", users=users)

@user.route('/edit_user')
def edit_user():
    removable_users = {key: value for key, value in users.items() if key != "admin"}
    return render_template("users/edit_user.html", users=removable_users)

@user.route('/update_user', methods=['POST'])
def update_user():
    global users
    username = request.form['user']
    new_name = request.form['new_name']
    new_password = request.form['new_password']

    if username in users:
        if new_name:
            users.pop(username)
            users[new_name] = None
        elif new_password:
            users.pop(username)
            users[username] = new_password
        elif new_name and new_password:
            users.pop(username)
            users[new_name] = new_password
    return render_template("users/users.html", users=users)