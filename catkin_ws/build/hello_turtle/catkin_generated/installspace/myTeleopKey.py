#!/user/bin/env

# script de python correspondiente a un nodo tipo Teleop_key

import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute, TeleportRelative
import termios, sys, os
import numpy as np
from std_srvs.srv import Empty, EmptyRequest

pi= np.pi

def getkey():
    fd = sys.stdin.fileno()  # Entrada de un descriptor de archivos (archivos o conjunto de datos)
    old = termios.tcgetattr(fd)  # Obtiene los atributos del terminal para el descriptor de archivos
    new = termios.tcgetattr(fd)  # Hace una copia de los atributos del terminal actuales
    new[3] = new[3] & ~termios.ICANON & ~termios.ECHO #~ICANON-Evita cadena de carácterees; ~ECHO evita que se imprima en patnalla lo que se escriba
    new[6][termios.VMIN] = 1 #configura el mínimo de carácteres para leer como 1 queda en pausa
    new[6][termios.VTIME] = 0 #Configura el tiempo de espera para la lectura como 0 (modo no bloqueante).
    termios.tcsetattr(fd, termios.TCSANOW, new) #Establece los nuevos atributos de los terminales TCSANOW, hace los cambios de inmediato
    c = None
    try:
        c = os.read(fd, 1) #Lee un solo caracter del descriptor de archivos
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, old) # Restaura los antigus atributos del terminal despues de sacar los datos del buffer y limpiar la entrada
    return c
    
def moveTurtle(velocity):
    movePub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    move_msg = Twist()
    move_msg.linear.x = velocity
    rate = rospy.Rate(10) # 10hz 
    movePub.publish(move_msg)
    rate.sleep()
    
def turnTurtle(velocity):
    movePub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    move_msg = Twist()
    move_msg.angular.z = velocity
    rate = rospy.Rate(10) # 10hz  
    movePub.publish(move_msg)
    rate.sleep()

def mainPositionTurtle():
    rospy.wait_for_service('/turtle1/teleport_absolute')    
    
    try:
        teleport_mainPosition = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute)
        req = TeleportAbsolute._request_class()
        req.x = 5.5
        req.y = 5.5
        req.theta = 0
        teleport_mainPosition(req) #Se mueve hasta su posición inicial con su orientacion inicial
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s" % e)
    
def turn180Turtle():
    rospy.wait_for_service('/turtle1/teleport_relative')    

    try:
        teleport_180g = rospy.ServiceProxy('/turtle1/teleport_relative', TeleportRelative)
        req = TeleportRelative._request_class()
        req.linear = 0.0
        req.angular = pi  # 180 degrees in radians
        teleport_180g(req) # a partir de su punto se rota 180°
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s" % e)

def main():
    rospy.init_node('robotTurtleJJ',anonymous=True)

    while True:
        movement = getkey().decode('ascii')
        if movement == 'w':
            print('forward')
            moveTurtle(1)
        elif movement == 's':
            print('backward')
            moveTurtle(-1)
        elif movement == 'a':
            print('turn Counterclockwise')
            turnTurtle(1)
        elif movement == 'd':
            print('turn clockwise')
            turnTurtle(-1)
        elif movement == 'r':
            print('turn 180')
            turn180Turtle()
        elif movement == ' ':
            print('main position')
            mainPositionTurtle()
        elif movement == 'p':
            print('shut code')
            rospy.on_shutdown()
        else: 
            print("No esta entre las opciones")

    
if __name__ == '__main__':
    try:
         #Testing our function
         main()
    except rospy.ROSInterruptException: pass
