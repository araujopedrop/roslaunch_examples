#!/usr/bin/python3


import rclpy

import launch  
import launch_ros
import launch.events
import launch.actions
import launch.substitutions

from rclpy.node                        import Node

from launch                            import LaunchService
from launch.actions                    import IncludeLaunchDescription
from launch_ros.substitutions          import FindPackageShare
from launch.launch_description_sources import PythonLaunchDescriptionSource

class testNode(Node):

    def __init__(self):
        super().__init__("test_node")

        ld = launch.LaunchDescription()
        
        # Action LogInfo
        action_print = launch.actions.LogInfo(msg='Hello World!')

        # Action Node
        action_node = launch_ros.actions.Node(
            package="roslaunch_examples",
            executable="test_node2.py",
            name='test_node_test'
        )
 
        #Action "Launch"
        launch_to_import = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([
                    FindPackageShare("roslaunch_examples"), '/launch', '/test_launch.launch.py'])
            )

        ld.add_action(action_print)
        ld.add_action(action_node)
        ld.add_action(launch_to_import)
        

        ls = LaunchService()
        ls.include_launch_description(ld)
        ls.run()

        self.get_logger().info("test_node is up!")




def main(args=None):
    rclpy.init(args=args)
    node = testNode() 
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()
