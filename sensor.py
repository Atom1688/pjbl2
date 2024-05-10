from flask import render_template, request, Blueprint

sensor = Blueprint("sensor", __name__)

sensors = {}


@sensor.route('/register_sensor')
def register_sensor():
    return render_template("sensors/register_sensor.html")

@sensor.route('/add_sensor', methods=['GET','POST'])
def add_sensor():
    global sensors
    if request.method == 'POST':
        sensor = request.form['sensor']
    else:
        sensor = request.args.get('sensor', None)
    sensors[sensor] = None
    return render_template("sensors/sensors.html", sensors=sensors)

@sensor.route('/list_sensors')
def list_sensors():
    global sensors
    return render_template("sensors/sensors.html", sensors=sensors)

@sensor.route('/remove_sensor')
def remove_sensor():
    return render_template("sensors/remove_sensor.html", sensors=sensors)

@sensor.route('/del_sensor', methods=['GET','POST'])
def del_sensor():
    global sensors
    if request.method == 'POST':
        sensor = request.form['sensor']
    else:
        sensor = request.args.get('sensor', None)
    sensors.pop(sensor)
    return render_template("sensors/sensors.html", sensors=sensors)

@sensor.route('/edit_sensor')
def edit_sensor():
    return render_template("sensors/edit_sensor.html", sensors=sensors)

@sensor.route('/update_sensor', methods=['POST'])
def update_sensor():
    global sensors
    sensor_name = request.form['sensor']
    new_sensor_name = request.form['new_sensor_name']

    if sensor_name in sensors:
        sensors.pop(sensor_name)
        sensors[new_sensor_name] = None
    return render_template("sensors/sensors.html", sensors=sensors)