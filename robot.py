from event_handler import EventHandler
from motors_i2c import Motor
from smbus2 import SMBus
from imu import bno08x_IMU
from camera import Camera

class Robot:
    def __init__(self):
        self.bus = SMBus(1)
        self.imu = bno08x_IMU()
        self.motors = [
            Motor(25, self.bus),
            Motor(27, self.bus),
            Motor(28, self.bus),
            Motor(26, self.bus),
            Motor(30, self.bus)
        ]
        self.event_handler = EventHandler(self)
        self.camera = Camera()

    def update(self):
        ...