from flask import Flask, render_template, request

app = Flask(__name__)

users = {
    'admin': 'admin',
    'rafael': '12345',
    'matheus': '54321'
}

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/validated_user', methods=['POST'])
def validated_user():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        print(user, password)
        if user in users and users[user] == password:
            return render_template('home.html')
        else:
            return '<h1>invalid credentials!</h1>'
    else:
        return render_template('login.html')

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/atuadores')
def quarto():
    atuadores = {'Atuador 1': 0, 'Atuador 2': 1, 'Atuador 3': 1}
    return render_template("actuators.html", atuadores=atuadores)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
