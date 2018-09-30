#!/usr/bin/env python
import rospy
import random
import time
import os
from catch_the_star.msg import Num

ch = 0
score = 0
level = 1
global life
def callback(msg):
    global ch
    ch = msg.num
    
def start(x):
    global score
    global level
    global life
    global ch
    os.system('cls' if os.name == 'nt' else 'clear')  
    if x == 1:
        print '1. * \n2.\n3.\n4.\n5.'
        rate.sleep()
        
    if x == 2:
        print '1.\n2. * \n3.\n4.\n5.'
        rate.sleep()
        
    if x == 3:
        print '1.\n2.\n3. * \n4.\n5.'
        rate.sleep()
        
    if x == 4:
        print '1.\n2.\n3.\n4. * \n5.'
        rate.sleep()
        
    if x == 5:
        print '1.\n2.\n3.\n4.\n5. * '
        rate.sleep()
        
    print "Score: ",score
    print 'Level: ',level
    print 'Life: ',life
        
    time.sleep(5.0 / level)
    if ch == x:
        score += level*10
        level += 1
        
    elif ch != x and ch != 0:
        life -= 1
    
    if life == 0:
        os.system('cls' if os.name == 'nt' else 'clear')  
        print "*********"
        print "GAME OVER"
        print "Score: ",score
        print 'Level: ',level
        print "*********"
    ch = 0
    rate.sleep()
    
if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    rospy.init_node('subscriber')
    rospy.Subscriber('/keystroke',Num,callback)
    rate = rospy.Rate(10)
    global life
    life = 3
    while True:
        if life == 0:
            break
        x = random.randint(1,5)
        start(x)

        rate.sleep()
        
    rospy.spin()
