class DriveBot:
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 1
    def __init__(self, motor_speed, directiion, sensor_range):
        self.motor_speed = motor_speed
        self.direction = directiion
        self.sensor_range = sensor_range
        self.id = DriveBot.robot_count
        DriveBot.robot_count += 1
    def display(self):
        print(f"ROBOT {self.id}\nMotor speed: {self.motor_speed}\nDirection: {self.direction}\nSensor range: {self.sensor_range}")
while True:
    motor_speed = input("Motor speed: ")
    direction = input("Direction: ")
    sensor_range = input("Sensor range: ")
    robot = DriveBot(motor_speed, direction, sensor_range)
    robot.display()
    next = input("Next robot? (yes/no): ")
    if next != "yes":
        break