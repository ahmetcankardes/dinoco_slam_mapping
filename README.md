# DINOCO-SLAM Mapping Test Codes

This repo will be used to test mapping algorithms in real life.

# Setup

-Make sure that catkin is installed, if it is not type the following command
sudo apt-get install ros-noetic-catkin

-First, open a terminal and type the following commands.

mkdir -p ~/dinoco_mapping_ws/src
cd ..
catkin_make

-This will create the catkin workspace that will be used for mapping algorithms.
-Then go inside the src folder by
cd /src

-Finally get the github repo by
git clone https://github.com/ahmetcankardes/dinoco_slam_mapping.git

# How to Run

-Navigate the directory to the /dinoco_slam_mapping folder.
-There are two different mapping codes written in python as mapping.py and
mapping_v2.py. You can run those codes in terminal by
pyhton3 mapping.py
python3 mapping_v2.py
