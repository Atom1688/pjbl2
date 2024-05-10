from flask import Flask, render_template, request
from flask_mqtt import Mqtt
from flask_socketio import SocketIO

from login import login
from sensor import sensor
from actuator import actuator
from user import user

app = Flask(__name__)
app.register_blueprint(login, url_prefix='/')
app.register_blueprint(sensor)
app.register_blueprint(actuator)
app.register_blueprint(user)

# --------------- MQTT --------------- # 

app.config['MQTT_BROKER_URL'] = 'mqtt-dashboard.com'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_KEEPALIVE'] = 60
app.config['MQTT_REFRESH_TIME'] = 1.0

socketio = SocketIO(app)
mqtt = Mqtt(app)

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('umidadeTDE')

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    print(f'Mensagem recebida: {message.payload.decode()}')
    socketio.emit('mqtt_message', {
        'topic': message.topic,
        'payload': message.payload.decode()
    })

@socketio.on('publish_mqtt')
def handle_publish_mqtt_event(json):
    topic = json['topic']
    payload = json['payload']
    mqtt.publish(topic, payload)

@app.route('/mqtt_display')
def mqtt_display():
    return render_template('mqtt/mqtt_display.html')

@app.route('/mqtt_publish')
def mqtt_publish():
    return render_template('mqtt/mqtt_publish.html')

# --------------- MAIN --------------- # 

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=8080, use_reloader=True, debug=True)

