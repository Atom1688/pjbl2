from flask import render_template, request, Blueprint

actuators = {}

actuator = Blueprint("actuator", __name__)

@actuator.route('/register_actuator')
def register_actuator():
    return render_template("actuators/register_actuator.html")

@actuator.route('/add_actuator', methods=['GET','POST'])
def add_actuator():
    global actuators
    if request.method == 'POST':
        actuator = request.form['actuator']
    else:
        actuator = request.args.get('actuator', None)
    actuators[actuator] = None
    return render_template("actuators/actuators.html", actuators=actuators)

@actuator.route('/list_actuators')
def list_actuators():
    global actuators
    return render_template("actuators/actuators.html", actuators=actuators)

@actuator.route('/remove_actuator')
def remove_actuator():
    return render_template("actuators/remove_actuator.html", actuators=actuators)

@actuator.route('/del_actuator', methods=['GET','POST'])
def del_actuator():
    global actuators
    if request.method == 'POST':
        actuator = request.form['actuator']
    else:
        actuator = request.args.get('actuator', None)
    actuators.pop(actuator)
    return render_template("actuators/actuators.html", actuators=actuators)

@actuator.route('/edit_actuator')
def edit_actuator():
    return render_template("actuators/edit_actuator.html", actuators=actuators)

@actuator.route('/update_actuator', methods=['POST'])
def update_actuator():
    global actuators
    actuator_name = request.form['actuator']
    new_actuator_name = request.form['new_actuator_name']

    if actuator_name in actuators:
        actuators.pop(actuator_name)
        actuators[new_actuator_name] = None
    return render_template("actuators/actuators.html", actuators=actuators)