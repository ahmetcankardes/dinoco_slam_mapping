import rospy
from std_msgs.msg import Float64
from sensor_msgs.msg import PointCloud
from geometry_msgs.msg import Point32
from math import radians, cos, sin
from map_class import map_class

map_object = map_class()

sequence_control = 0

pc_msg = PointCloud()
pc_msg.header.stamp = rospy.Time.now()
pc_msg.header.frame_id = "base_footprint"

#Publisher for Point Cloud
pub = rospy.Publisher("lidar/pointcloud", PointCloud, queue_size = 10)

if __name__ == "__main__":

    rate = rospy.Rate(30.0) #30Hz

    theta_match = 360 / len(map_object.lidar_data)

    while not rospy.is_shutdown():
        for i in map_object.lidar_data:
            try:
                if (i < 7):
                    theta = radians(theta_match*map_object.lidar_data.index(i))
                    #i_point = (i*cos(map_object.tilt_angle)*cos(theta), i*cos(map_object.tilt_angle)*sin(theta), i*sin(map_object.tilt_angle))
                    #print("detected point: ", i_point)
                    pc_msg.points.append(Point32(i*cos(map_object.tilt_angle)*cos(theta), i*cos(map_object.tilt_angle)*sin(theta), i*sin(map_object.tilt_angle)-0.13))
                else:
                    sequence_control = 0
            except IndexError:
                print("Error")
            except ValueError:
                print("Error Ocured")

        if sequence_control == 0:
            print("--------------------------------")

        pub.publish(pc_msg)

        rate.sleep()
