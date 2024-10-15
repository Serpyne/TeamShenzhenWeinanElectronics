from smbus2 import SMBus, i2c_msg

class bno08x_IMU:
    def __init__(self):
        self.CS = 10
        self.INT = 9
        self.RESET = -1

        self.address = 0x4a
        self.SDA = 18
        self.SCL = 19

    # DO SERIAL
