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


current_component_info_id = -1
current_component_info_name = ""

def HitCache_case_component(component_name):
    global current_component_info_row
    global current_component_info_id

    if component_name == current_component_info_name:
        return current_component_info_id
    return -1

def get_component_id_by_category_name(ccm_conn,category_name):
    if ccm_conn is None:
        print("查询为空")
        return 0

    global current_component_info_name
    global current_case_component_id

    if HitCache_case_component(category_name)>0:
        return current_component_info_id

    sql_find = "SELECT * FROM component_info WHERE category_name='%s'" % (category_name)

    print(sql_find)

    try:
        cursor = ccm_conn.cursor()
        cursor.execute(sql_find)

        # results是个元组对象
        results = cursor.fetchone()
        # 先判断是否为空
        if results is None:
            print("查询为空")
            return 0
        # else:
        #     print(results)

        # x = len(results)


        component_id = results[0]

        print("component_id=%d\n" % (component_id))

        current_component_info_id = component_id
        current_component_info_name = results[1]

        return component_id

    except Exception as ex:
        print("get_component_id_by_package_name: %s failed\n" % (package_name))
        print(ex)
        return 0

