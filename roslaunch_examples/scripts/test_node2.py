#!/usr/bin/python3

import os
from typing import Iterator
import rclpy
from example_interfaces.msg import String
from rclpy.node import Node
from rclpy.publisher import Publisher

import launch  # noqa: E402
#from launch_ros.actions import Node 
from launch import LaunchDescription  # noqa: E402
from launch import LaunchIntrospector  # noqa: E402
from launch import LaunchService  # noqa: E402
import launch.actions  # noqa: E402
import launch.events  # noqa: E402
import launch.substitutions  # noqa: E402

class myTestNode2(Node):
    def __init__(self):
        super().__init__("test_node2")
        
        self.get_logger().info("Hola soy el launcheado!")    

def main():
    rclpy.init()
    node = myTestNode2() 
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()
        rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()






