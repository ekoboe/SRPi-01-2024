from flask import Flask, render_template, jsonify
from bme_module import BME280Module
import random


bme280_module = BME280Module()

app = Flask(__name__)
app.secret_key = 'BOE'


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
