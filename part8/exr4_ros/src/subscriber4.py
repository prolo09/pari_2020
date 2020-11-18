#!/usr/bin/env python

import rospy
from exr4_ros import mesaguemCao

import argparse

def callback(data):
    rospy.loginfo(str(mesageuemCao))

def escolhamodo():
    # funcao para escolher os modos
    esc_modo = argparse.ArgumentParser(description="escolhe dos nos")
    esc_modo.add_argument('-tn', help="topic name", default='chat')
    arg_list=vars(esc_modo.parse_args())
    return arg_list

def subscriber():

    lista_tn=escolhamodo()
    rospy.init_node( 'no_recive', anonymous=True)         # cria o no
    rospy.Subscriber(lista_tn['tn'], mesageuemCao, callback)    # recebe o topico
    rospy.spin()                                          # evita que o no saio sem ser desligado

if __name__ == '__main__':
    subscriber()