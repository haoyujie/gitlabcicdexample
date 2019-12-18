#!/usr/bin/python
# encoding: utf8
#
import datetime
import re
import pymysql
import sys

conn = None

def get_ccmdb():
    global conn
    if conn is None:
        return open_ccmtcdb
    else:
        return conn

def open_ccmtcdb():
    try:
        print('try to conecting to ccmtcdb database...')
        # Connect to the MySQL database
        # conn = pymysql.connect(host='127.0.0.1', user='yhao', passwd='123456', db='ccmdb', charset='utf8mb4')
        global conn
        ccm_conn = pymysql.connect(host='pek-lpd-ccm1', user='yhao', passwd='3333yhao', db='ccmdb', charset='utf8mb4')

        # Check if connection was successful
        if (ccm_conn):
            # Carry out normal procedure
            print("Connection successful")
            conn=ccm_conn
            return ccm_conn
        else:
            # Terminate
            print("Connection failed")
            return None
        return None
    except:
        print("Connection except")
        return None
