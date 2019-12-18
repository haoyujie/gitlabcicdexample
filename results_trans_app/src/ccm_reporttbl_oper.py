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

from ccmdboper import *
from ccm_utils import *

# return recordset of one test case
def getone_report_by_reportid(report_id):

    sql_find = "SELECT * FROM test_report WHERE (report_id =%d)" \
               % (report_id)
    print(sql_find)

    try:
        conn = get_ccmdb()
        cursor = conn.cursor()
        cursor.execute(sql_find)

        # results是个元组对象
        results = cursor.fetchone()
        # 先判断是否为空
        if results is None:
            debugstr = "[ERROR]查询为空:casename=%d,report_id=%d" \
                    % (casename,report_id )

            print(debugstr)
            return None
        # else:
        #     print(results)
        # x = len(results)

        case_id = results[0]
        print("case_id=%d" % (case_id))
        return results
    except Exception as ex:
        print('<ERROR>getone_testcase_by_name failed')
        print(ex)
        return None



def write2ccmdb_test_report(report_id, report_name, rcpl, report_date, project_id):
    try:
        conn=get_ccmdb()

        execute_case =0;
        total_case=0;
        pass_case=0;

        fail_case=0;
        blocked_case=0;

        sql_insert = "INSERT INTO test_report(report_id, report_name, rcpl, report_date, project_id, execute_case, total_case, pass_case, fail_case, blocked_case) VALUES  \
        (%d, '%s', %d, '%s', %d, %d, %d, %d, %d, %d )" % (
        report_id, report_name, rcpl, report_date, project_id, execute_case, total_case, pass_case, fail_case,
        blocked_case)

        print(sql_insert)

        # strsql = ('62', '7', '3', 'test1', 'zeqomq', '1', null, 'No note')
        # create a cursor
        cursor = conn.cursor()
        # execute SQL statement
        cursor.execute(sql_insert)
        # caseid = int(cursor.lastrowid)
        # get ID of last inserted record
        print("ID of last record is ", int(report_id))  # 最后插入行的主键ID
        # print("ID of inserted record is ", int(conn.insert_id()))  # 最新插入行的主键ID，conn.insert_id()一定要在conn.commit()之前，否则会返回0
        conn.commit()
        return 1



    except Exception as ex:
        print(ex)
        # (Exception, e):
        print('write2ccmdb_test_report failed')
        # print ('repr(e):\t', repr(e))

        return -1



def update2ccmdb_test_report(report_id, report_name, rcpl, report_date, project_id, execute_case, total_case, pass_case,
                            fail_case, blocked_case,report_end_time):
    try:


        conn=get_ccmdb()

        sql_update =    "UPDATE test_report SET report_name='%s' , rcpl=%d, report_date='%s', project_id=%d,  \
                        execute_case=%d, total_case=%d, pass_case=%d, fail_case=%d, blocked_case=%d,end_time='%s',state=%d, isstasticed=%d " \
                        "WHERE (report_id=%d) " \
                        % (
                            report_name, rcpl, report_date, project_id, execute_case, total_case, pass_case, fail_case,
                            blocked_case,report_end_time,int(1),int(0),report_id )

        print(sql_update)

        # strsql = ('62', '7', '3', 'test1', 'zeqomq', '1', null, 'No note')
        # create a cursor
        cursor = conn.cursor()
        # execute SQL statement
        cursor.execute(sql_update)
        conn.commit()
        return 1

    except Exception as ex:
        print(ex)
        print('update2ccmdb_test_report failed')

        return -1

