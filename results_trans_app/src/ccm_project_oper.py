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


def get_projectid_by_name(ccm_conn,project_name):
    if ccm_conn is None:
        print("查询为空")
        return 0
    sql_find = "SELECT * FROM project_info WHERE project_name='%s'" % (project_name)

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


        project_id = results[0]

        print("projectid=%d" % (project_id))

        return project_id

    except Exception as ex:
        print('get_projectid_by_name failed')
        print(ex)
        return 0

