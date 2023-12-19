import rospy
import tf
from std_msgs.msg import Float64
from math import radians


def servo_callback(angle_msg):
    # Update the transform based on the servo angle
    tilt_angle = angle_msg.data  # Get the tilt angle from your servo message
    tilt_angle = radians(tilt_angle)

    # Create a TF broadcaster
    tf_broadcaster = tf.TransformBroadcaster()

    # Publish the transform
    tf_broadcaster.sendTransform(
        (0.0, 0.0, 0.0),  # translation (x, y, z)
        tf.transformations.quaternion_from_euler(tilt_angle, 0.0, 0.0),  # rotation (roll, pitch, yaw)
        rospy.Time.now(),
        "base_footprint",
        "laser_frame"
    )

if __name__ == "__main__":
    rospy.init_node("lidar_tf_broadcaster")

    # Create a TF broadcaster
    #tf_broadcaster = tf.TransformBroadcaster()

    # Subscribe to your servo angle topic
    rospy.Subscriber("/servo_angle", Float64, servo_callback)

    while True:
        continue

    # Spin to keep the node running
    #rospy.spin()
