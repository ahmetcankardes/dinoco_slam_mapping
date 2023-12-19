import rospy
from std_msgs.msg import Float64
from sensor_msgs.msg import LaserScan
from math import radians
from time import sleep

class map_class:
    def __init__(self):

        rospy.init_node('Dinoco_Mapping')

        # Subscribe to your servo angle topic
        rospy.Subscriber("/servo_angle", Float64, self.servo_callback)

        # Subscribe to laser scan topic
        rospy.Subscriber("/scan", LaserScan, self.lidar_callback)
        sleep(5)

        self.tilt_angle = 0
        self.lidar_data

    def servo_callback(self, angle_msg):
        self.tilt_angle = angle_msg.data  # Get the tilt angle from your servo message
        #print("Tilt:",self.tilt_angle)
        self.tilt_angle = radians(self.tilt_angle)

    def lidar_callback(self, scan_msg):
        self.lidar_data = scan_msg.ranges
        #print("Lidar:", self.lidar_data)
