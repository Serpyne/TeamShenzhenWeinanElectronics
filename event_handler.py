from time import perf_counter

SETSPEED = 0x5e
STOP = 0x00

class EventHandler:
    def __init__(self, robot):
        self.max_motor_speed = 90_000_000

        self.command_interval = 100 # ms
        self.prev_time = perf_counter()
        self.delta_time = 0

        self.commands = {0: None, 1: None, 2: None, 3: None, 4: None}
        self.robot = robot

    def stop(self, motor_number: int):
        """Stops the motor numbered from 1 to 5"""
        self.commands[motor_number - 1] = STOP

    def set_speed(self, motor_number: int, speed: float):
        adjusted_speed = self.max_motor_speed * min(max(speed, -1.0), 1.0)
        self.commands[motor_number - 1] = (SETSPEED, int(adjusted_speed))

    def update(self):
        current_time = perf_counter()
        self.delta_time = current_time - self.prev_time

        if self.delta_time < self.command_interval:
            return
        
        self.prev_time = current_time

        for motor_number in self.commands:
            if self.commands[motor_number] is None:
                continue

            if self.commands[motor_number] == STOP:
                self.robot.motors[motor_number].set_speed(0)
                self.commands[motor_number] = None
                continue

            if self.commands[motor_number] == SETSPEED:
                speed = self.commands[motor_number][1]
                self.robot.motors[motor_number].set_speed(speed)
                self.commands[motor_number] = None
        