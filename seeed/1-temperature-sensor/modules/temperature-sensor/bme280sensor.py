import smbus2
import bme280

class BME280Sensor():
    def __init__(self):
        self.port = 1
        self.address = 0x76
        self.bus = smbus2.SMBus(self.port)
        self.json_temperature_data = None
        self.raw_sensor_data = None

        try:
            bme280.load_calibration_params(self.bus, self.address)
        except Exception as e:
            print(e)

    def get_sample(self):
        sample = bme280.sample(self.bus, self.address)

        machine = Machine(sample.temperature, sample.pressure)
        ambient = Ambient(sample.temperature, sample.humidity)

        return MessageBody(machine, ambient, str(sample.timestamp), sample.id)


class MessageBody():
    def __init__(self, machine, ambient, timeCreated, id):
        self.machine = machine
        self.ambient = ambient
        self.timeCreated = timeCreated
        self.id = id


class Machine():
    def __init__(self, temperature, pressure):
        self.temperature = temperature
        self.pressure = pressure


class Ambient():
    def __init__(self, temperature, humidity):
        self.temperature = temperature
        self.humidity = humidity
