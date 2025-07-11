## Computer Vision Sorting Robotic Arm: Mechanical CAMden

### Project Overview: 
The goal of this project is to mimic the behavior of our close friend, Camden James Droz. Not only is he an inspiration to us all, but more importantly, he is excellent at sorting objects by color. For our final project, we used computer vision and inverse kinematics to sort cubes of various colors into different locations. This is done by using an ArUco board to translate image coordinates to camera coordinates to world coordinates, and then transfrom from the board frame, to the camera frame, to the robotic frame. Lastly, use our IK algorithm to move our robotic arm to the desired end effector position and pick up the object. Mechanical CAMden is shown in action below: 

<img src="media/gif_video.gif" height="450">  <img src="media/gif_video2.gif" height="450">

### Repository Information: 
This repository provides the python libraries for interfacing with the Hiwonder 5-DOF mobile manipulator. We have modified the original reporsitory to add additional functionality to the Hiwonder 5-DOF mobile manipulator; we have added a sorter.py function as the final project of our Fundamentals of Robotics final. Our final report for the project can be found in this repo here: [Final Project Report.](https://github.com/swisnoski/hiwonder-armpi-pro/blob/v2025/Mechanical_CAMden_Technical_Report.pdf)

### Robot Information:
The robot platform has an onboard **Raspberry Pi 4B** which serves as the main compute unit of the system. The 5-DOF arm are driven by serial bus servos controlled over serial while the mobile base is driven by DC motors controlled by a custom driver board with communication over I2C. Our project development was completed onboard the Raspberry Pi over **SSH protocol**.


## How to setup and run Mechanical CAMden

#### Step 0: Connect to Raspberry Pi over SSH
- Run `ssh pi@robot.ip` in terminal, replacing `robot.ip` with the IP adress of your robot.
  **The password is `fun`** 
- SSH troubleshooting:
  - Make sure you are connected to the Olin Robotics network (It should work on Olin, but Olin Robotics may be faster/more stable).
  - Make sure OpenSSH Client and OpenSSH Server are installed (should be installed by default on Mac/Linux, may need to be installed under `Settings > System > Optional Features` in Windows).
  - Make sure the OpenSSH folder is added to your path. Should be `C:\Windows\System32\OpenSSH` in Windows.
  - Check the SD card to make sure the number physically written on it matches what you expect.

#### Step 1: Create a virtual environment
- We strongly recommend that you create a new python virtual environment for all your work on the platform.
- Follow this [tutorial here](https://docs.python.org/3/tutorial/venv.html).


#### Step 2: Get this repository from Github
- Fork this repository from github and clone it onto your Hiwonder Armpi Pro robot. Ensure you have the updated v2025 repository, DO NOT USE the v2024 or v2024-new versions. 


#### Step 3: Install all required Python packages
First: make sure you have created and activated the virtual environment (see step 1).
```bash
# cd to the project folder
$ cd hiwonder-armpi-pro

# install all required packages from requirements.txt
$ pip install -r requirements.txt
```
The requirements has already been updated for our Mechanical CAMden scripts. 


#### Step 4: How to Run Mechanical CAMden

- Before you run any script, please initialize the **pigpiod module**
``` bash
$ sudo pigpiod
```

- If setup worked well, you should be able to run the main script (sorter.py) by navigating to the scripts folder and running:
``` bash
$ cd scripts
$ python sorter.py
# this should activate the function. The robot will move to home position. 
```

#### Step 5: Sorting Cubes
In order for Mechanical CAMden to work, you need to have a ArUco board with specified dimensions in camera_cv.py. We used a 5x7 grid with 6x6 april tags. If the ArUco board is in frame, place a red or green cube on the board within range of the arm, and the arm will begin scanning coordinates and pick up the cube. Red cubes will be sorted to the left side of the robot, while green cubes will be sorted to the left. 


