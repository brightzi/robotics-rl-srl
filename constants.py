from __future__ import print_function, absolute_import, division

# Socket port
SERVER_PORT = 7777
REF_POINT = [0.6, 0.30, 0.20]
IK_SEED_POSITIONS = [-1.535, 1.491, -0.038, 0.194, 1.546, 1.497, -0.520]
HOSTNAME = 'localhost'
DELTA_POS = 0.05

# ROS Topics
IMAGE_TOPIC = "/cameras/head_camera_2/image"
ACTION_TOPIC = "/robot/limb/left/endpoint_action"
BUTTON_POS_TOPIC = "/button1/position"


# Arrow keys for teleoperation
UP_KEY = 82
DOWN_KEY = 84
RIGHT_KEY = 83
LEFT_KEY = 81
ENTER_KEY = 10
SPACE_KEY = 32
EXIT_KEYS = [113, 27]  # Escape and q
D_KEY = 100
U_KEY = 117
R_KEY = 114
