#!/usr/bin/python3
# encoding: utf8
#
import datetime

from spyne import Application, rpc, ServiceBase, Iterable, Integer, Unicode

from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

# import requests
import re
import pymysql
import sys

import os


localdir=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,localdir)

from ccmdboper import *
from TstService import *

def my_init():
    print("ccm automatic test webservice starting...")


application = Application([CCMTstService], 'spyne.examples.hello.soap',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    import logging

    from wsgiref.simple_server import make_server


    my_init()
    ccm_conn = open_ccmtcdb()
    if ccm_conn is None :
        print("open db error")
        exit(-1)

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

    logging.info("listening to http://pek-lpd-ccm1:9005")
    logging.info("wsdl is at: http://pek-lpd-ccm1:9005/?wsdl")

    server = make_server('128.224.179.178', 9005, wsgi_application)
    server.serve_forever()
    print('error')
    ccm_conn.close()
