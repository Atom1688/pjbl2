from flask import Flask, render_template, request

app = Flask(__name__)

users = {
    'admin': 'admin',
    'rafael': '12345',
    'matheus': '54321'
}

sensors = {}
actuators = {}

# --------------- LOGIN --------------- # 

@app.route('/')
def index():
    return render_template("login/login.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/validated_user', methods=['POST'])
def validated_user():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        print(user, password)
        if user in users and users[user] == password:
            return render_template('home.html')
        else:
            return render_template('login/invalid_credentials.html')
    else:
        return render_template('login/login.html')

# --------------- CRUD SENSOR --------------- # 

@app.route('/register_sensor')
def register_sensor():
    return render_template("sensors/register_sensor.html")

@app.route('/add_sensor', methods=['GET','POST'])
def add_sensor():
    global sensors
    if request.method == 'POST':
        sensor = request.form['sensor']
    else:
        sensor = request.args.get('sensor', None)
    sensors[sensor] = None
    return render_template("sensors/sensors.html", sensors=sensors)

@app.route('/list_sensors')
def list_sensors():
    global sensors
    return render_template("sensors/sensors.html", sensors=sensors)

@app.route('/remove_sensor')
def remove_sensor():
    return render_template("sensors/remove_sensor.html", sensors=sensors)

@app.route('/del_sensor', methods=['GET','POST'])
def del_sensor():
    global sensors
    if request.method == 'POST':
        sensor = request.form['sensor']
    else:
        sensor = request.args.get('sensor', None)
    sensors.pop(sensor)
    return render_template("sensors/sensors.html", sensors=sensors)

@app.route('/edit_sensor')
def edit_sensor():
    return render_template("sensors/edit_sensor.html", sensors=sensors)

@app.route('/update_sensor', methods=['POST'])
def update_sensor():
    global sensors
    sensor_name = request.form['sensor']
    new_sensor_name = request.form['new_sensor_name']

    if sensor_name in sensors:
        sensors.pop(sensor_name)
        sensors[new_sensor_name] = None
    return render_template("sensors/sensors.html", sensors=sensors)

# --------------- CRUD ACTUATOR --------------- # 

@app.route('/register_actuator')
def register_actuator():
    return render_template("actuators/register_actuator.html")

@app.route('/add_actuator', methods=['GET','POST'])
def add_actuator():
    global actuators
    if request.method == 'POST':
        actuator = request.form['actuator']
    else:
        actuator = request.args.get('actuator', None)
    actuators[actuator] = None
    return render_template("actuators/actuators.html", actuators=actuators)

@app.route('/list_actuators')
def list_actuators():
    global actuators
    return render_template("actuators/actuators.html", actuators=actuators)

@app.route('/remove_actuator')
def remove_actuator():
    return render_template("actuators/remove_actuator.html", actuators=actuators)

@app.route('/del_actuator', methods=['GET','POST'])
def del_actuator():
    global actuators
    if request.method == 'POST':
        actuator = request.form['actuator']
    else:
        actuator = request.args.get('actuator', None)
    actuators.pop(actuator)
    return render_template("actuators/actuators.html", actuators=actuators)

@app.route('/edit_actuator')
def edit_actuator():
    return render_template("actuators/edit_actuator.html", actuators=actuators)

@app.route('/update_actuator', methods=['POST'])
def update_actuator():
    global actuators
    actuator_name = request.form['actuator']
    new_actuator_name = request.form['new_actuator_name']

    if actuator_name in actuators:
        actuators.pop(actuator_name)
        actuators[new_actuator_name] = None
    return render_template("actuators/actuators.html", actuators=actuators)

# --------------- CRUD USER --------------- # 

@app.route('/register_user')
def register_user():
    return render_template("users/register_user.html")

@app.route('/add_user', methods=['GET','POST'])
def add_user():
    global users
    if request.method == 'POST':
        user = request.form['user']
    else:
        user = request.args.get('user', None)
    users[user] = '0000'
    return render_template("users/users.html", users=users)

@app.route('/list_users')
def list_users():
    global users
    return render_template("users/users.html", users=users)

@app.route('/remove_user')
def remove_user():
    removable_users = {key: value for key, value in users.items() if key != "admin"}
    return render_template("users/remove_user.html", users=removable_users)

@app.route('/del_user', methods=['GET','POST'])
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

@app.route('/edit_user')
def edit_user():
    removable_users = {key: value for key, value in users.items() if key != "admin"}
    return render_template("users/edit_user.html", users=removable_users)

@app.route('/update_user', methods=['POST'])
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

# --------------- MAIN --------------- # 

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
