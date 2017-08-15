
import rospy, sys 
import moveit_commander 
from moveit_commander import MoveGroupCommander 
from geometry_msgs.msg import Pose 
from copy import deepcopy 


def getPose():
        moveit_commander.roscpp_initialize("hello") 

#        # Initialize the ROS node 
        rospy.init_node('moveit_demo', anonymous=True) 
#        cartesian = rospy.get_param('~cartesian', True) 

#        # Connect to the right_arm move group 
        right_arm = MoveGroupCommander('braccio_arm') 
        print("pose=",right_arm.get_current_pose())

getPose()