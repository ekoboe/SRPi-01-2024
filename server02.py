from flask import Flask, render_template, jsonify
from bme_module import BME280Module
import random
import socket

bme280_module = BME280Module()

app = Flask(__name__)
app.secret_key = 'BOE'

s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s1.bind(('0.0.0.0', 6002))
print('listening on 0.0.0.0:5005')

@app.route('/')
def home():
    return render_template('monitoring.html')

@app.route('/sensorData')
def get_sensor_readings():
    temperature, pressure, humidity, altitude = bme280_module.get_sensor_readings()
    #temperature= random.randint(0,100)
    #humidity = random.randint(0, 100)
    data={
        "temperature": temperature,
        "humidity": humidity,
    }
    return jsonify(data)

@app.route('/updateClient')
def get_sensor_data_1():
    data, _ = s1.recvfrom(2048)
    data_1, data_2, data_3, data_4 = map(str, data.decode().split(','))

    response = {
        #"reading_data_1": random.randint(0,5),
        #"reading_data_2": random.randint(220,250),
        #"reading_data_3": random.randint(0,100),
        #"reading_data_4": random.randint(0,10),
        "reading_data_1": float(data_1),
        "reading_data_2": float(data_2),
        "reading_data_3": float(data_3),
        "reading_data_4": float(data_4),
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
