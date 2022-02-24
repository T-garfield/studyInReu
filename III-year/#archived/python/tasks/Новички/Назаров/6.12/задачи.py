class DriveBot:

    all_disabled = False
    latitude = -999999
    longitude= -999999 
    robot_count=0

    def __init__(self, motor_speed=0, direction=180, sensor_range=10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range 
        self.robot_count +=1
        self.id=DriveBot.robot_count

    def control_bot(self, motor_speed, direction):
        self.motor_speed = motor_speed
        self.direction = direction

    def adjust_sensor(self, sensor_range):
        self.sensor_range = sensor_range 

microbot= DriveBot()

microbot.longitude = 50.0
microbot.latitude = -50.0  

print(microbot.longitude)
print(microbot.latitude)
