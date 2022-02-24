
class DriveBot:

    robot_count = 0

    def __init__(self,  motor_speed = 0, direction = 180 , sensor_range = 10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range

        self.robot_count = self.robot_count + 1
        self.id = self.robot_count
        

    def control_bot(self, motor_speed, direction):
        self.motor_speed = motor_speed
        self.direction = direction
    
    def adjust_sensor(self, sensor_range):
        self.sensor_range = sensor_range
    
    all_disabled = False
    latitude = -999999
    longitude = -999999

longitude = 50.0
latitude = -50.0
all_disabled = True

