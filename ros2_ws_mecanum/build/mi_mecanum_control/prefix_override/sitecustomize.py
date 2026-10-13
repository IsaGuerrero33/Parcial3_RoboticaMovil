import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/isa-guerrero/ros2_ws_mecanum_estudiantes/ros2_ws_mecanum/install/mi_mecanum_control'
