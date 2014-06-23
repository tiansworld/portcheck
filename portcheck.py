#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


## 
## Note: This script is used for checking opened ports for an address(domain name or ip address).
## It's convenient for you to check whether a port is opened on your computer, server
## or something else. It's a simple tool aims to improve security.
## Don't use it to do evil things.

## About: This is my second python script. You know I am just a python newbie. Any
## suggestion, improvement on this script is welcome.
##

## 
import socket
import argparse
import sys

def check_open_port(address='localhost', *ports):
    port_lst = []
    for i in ports:
        print('Attempting to connect to port {0} on {1}'.format(i, address))

        try:
            socket.create_connection((address,i))
            print("Connected to port {0} on {1}".format(i, address))
            port_lst.append(i)
        except socket.error as e:
            print("Connection to port {0} on {2} failed {1}".format(i, e, address))
            print("Port {0} seems not open on {1}".format(i,address))
    if len(port_lst) == 0:
        print("The port(s) {0} is/are not opened".format(str(ports)[1:-1]))
    else:
        print("Opened Ports on {0} are: {1}".format(address,port_lst))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check open ports for ADDRESS')
    parser.add_argument('-a',default='localhost', dest='address',
                        metavar='ADDRESS', type=str,
                        help='Address to be checked, either domain name or ip address, default is "localhost".')
    parser.add_argument('-p', '--port',nargs='*',type=int,
                        dest='ports',default=(22,80),
                        metavar='PORTS', help='PORTS  to be checked')
    args = parser.parse_args()
    check_open_port(args.address,*args.ports)
