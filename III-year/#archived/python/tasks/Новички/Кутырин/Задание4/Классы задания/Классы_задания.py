
class DriveBot:
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0

    def __init__(self,motor_speed=0,direction=180,sensor_range=10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range  
        self.robot_count += 1
        self.robot_count = id
    def control_bot(motor_speed,direction):  
        self.motor_speed = motor_speed
        self.direction = direction
        return self.motor_speed,self.direction
    def adjust_sensor(sensor_range):
        self.sensor_range = sensor_range  
        return self.sensor_range
    
robot1 = DriveBot()
print(robot1.adjust_sensor)