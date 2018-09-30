#!/usr/bin/env python
import rospy
import random
import time
import os
from catch_the_star.msg import Num

os.system('cls' if os.name == 'nt' else 'clear')

def getchar():
   #Returns a single character from standard input
   import tty, termios, sys
   fd = sys.stdin.fileno()
   old_settings = termios.tcgetattr(fd)
   try:
      tty.setraw(sys.stdin.fileno())
      ch = sys.stdin.read(1)
   finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
   return ch

rospy.init_node('keystroke_publisher')
keyPub = rospy.Publisher('/keystroke',Num,queue_size = 0)

keyStroke = Num()

while True:
    keyStroke.num = int(getchar())
    keyPub.publish(keyStroke)
    keyStroke.num = 0
