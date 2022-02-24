#Задача 1
class DriveBot:
    #Задача 4
    all_disabled = False
    latitude = -999999
    longitude = -999999
    #Задача 5
    robot_count = 0
    #Задача 3
    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
        DriveBot.robot_count +=1
        self.id = DriveBot.robot_count
    #Задача 2
    def control_bot(self, speed, new_direction):
        self.motor_speed = speed
        self.direction = new_direction
    def adjust_sensor(self, sensor):
        self.sensor_range = sensor
    
    
bot = DriveBot()
bot1 = DriveBot()
bot.all_disabled = True
bot.longitude = 50.0
bot.latitude = -50.0
print(bot.id) #1
print(bot1.id) #2