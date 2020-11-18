#!/usr/bin/env python

import rospy
from std_msgs.msg import String         # impoto so a string pois neste caso e so string que estou a enviar mas da para enviar mais um variadade de coisas com imaguens e assim
import argparse

def escolhamodo():
    # funcao para escolher os modos
    esc_modo = argparse.ArgumentParser(description="escolhe topic e mesaguens")
    esc_modo.add_argument('-tn', help="topic name",default="chat")
    esc_modo.add_argument('-m', help="mesaguem para enviar atraves do publiseher", default="esta ja e a mesaguem")
    esc_modo.add_argument('-f', help="frequcia de envaio", default=5)
    arg_list=vars(esc_modo.parse_args())

    return arg_list

def publisher():

    lista_tmf=escolhamodo()

    pub=rospy.Publisher(lista_tmf['tn'], String , queue_size=10 ) # cria os meus topicos para comunicar com os nos
    rospy.init_node('publisher',anonymous=True)             # cria o meu node em anonimo

    rate = rospy.Rate(float(lista_tmf['f']))  # 10hz  # frequencia de envio com 10 mesaguens por segundo


    while not rospy.is_shutdown():
       # hello_str="hello word %s" % rospy.get_time()
        hello_str = lista_tmf['m']
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass

