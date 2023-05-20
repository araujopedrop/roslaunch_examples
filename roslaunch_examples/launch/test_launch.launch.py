import launch.actions
from launch import LaunchDescription


def generate_launch_description():

    ld = LaunchDescription()

    # Action LogInfo
    action_print = launch.actions.LogInfo(msg='Hello World_2!')

    ld.add_action(action_print)


    return ld