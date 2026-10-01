# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       kelvin                                                       #
# 	Created:      9/1/2026, 3:43:50 PM                                         #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import(Brain, wait, MSEC, Competition, Controller, PRIMARY, Inertial, Motor, Ports, FORWARD, REVERSE, PERCENT)

brain = Brain()
controller1 = Controller(PRIMARY)
inertial = Inertial(Ports.PORT5)
motorrearleft = Motor(Ports.PORT12, GearSetting.RATIO_18_1, True)
motorrearright = Motor(Ports.PORT9, GearSetting.RATIO_18_1, False)
motorfrontleft = Motor(Ports.PORT3, GearSetting.RATIO_18_1, True)
motorfrontright = Motor(Ports.PORT4, GearSetting.RATIO_18_1, False)
motorgroupleft = MotorGroup(motorrearleft, motorfrontleft)
motorgroupright = MotorGroup(motorrearright, motorfrontright)
drivetrain = SmartDrive(motorgroupleft, motorgroupright, inertial, 320, 350, 350)
auton = 0

def autonomous_switcher():
    global auton
    auton = auton + 1
    if auton > 3:
        auton = 0
    if auton == 0:
        controller1.screen.clear_screen()
        wait(50, MSEC)
        controller1.screen.print("Short Auton")
        wait(50, MSEC)
        controller1.screen.set_cursor(3, 1)
        controller1.rumble(".")

def pre_auton():
    global auton
    brain.screen.clear_screen()
    brain.screen.print("Pre-Autonomous")
    inertial.calibrate()

def autonomous():
    global auton
    brain.screen.clear_screen()
    brain.screen.print("autonomous code")
    # place automonous code here
    if auton == 0:
        drivetrain.drive_for(FORWARD, 100, MM)
def user_control():
    brain.screen.clear_screen()
    brain.screen.print("driver control")
    # place driver control in this while loop
    while True:
        wait(20, MSEC)
        motorgroupleft.spin(REVERSE)
        motorgroupright.spin(FORWARD)
        driveSpeed = controller1.axis3.position()
        turn = controller1.axis1.position()
        motorgroupleft.set_velocity(0.2*driveSpeed + 0.2*turn, PERCENT)
        motorgroupright.set_velocity(0.2*driveSpeed - 0.2*turn, PERCENT)
 
# create competition instance
comp = Competition(user_control, autonomous)

# actions to do when the program starts
brain.screen.clear_screen()
pre_auton()
controller1.rumble(".")
