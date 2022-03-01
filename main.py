import sipfullproxy

import SocketServer
import re
import string
import socket
#import threading
import sys
import time
import logging
def main():
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',filename='proxy.log',level=logging.INFO,datefmt='%H:%M:%S')
    logging.info(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime()))
    hostname = socket.gethostname()
    logging.info(hostname)
    ipaddress = socket.gethostbyname(hostname)
    if (sipfullproxy.ip != ""):
        ipaddress = sipfullproxy.ip
    # logging.info("prev IP")
    # logging.info(ipaddress)
    # ipaddress = "192.168.0.101" # LOCAL IP ADDRESS
    # if ipaddress == "127.0.0.1":
    #     ipaddress = sys.argv[1]
    logging.info(ipaddress)
    sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress,sipfullproxy.PORT)
    sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress,sipfullproxy.PORT)
    server = SocketServer.UDPServer((sipfullproxy.HOST, sipfullproxy.PORT), sipfullproxy.UDPHandler)
    server.serve_forever()


if __name__ == "__main__":
    args = sys.argv[1:]
    print(args)
    if (len(args) > 0):
        sipfullproxy.ip = args[0]
    main()
