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

# localdir=os.path.dirname(os.path.abspath(__file__))
# sys.path.insert(0,localdir)
from ccmdboper import *
from ccm_utils import *

from ccm_component_oper import *
from ccm_project_oper import *
from ccm_case_component_oper import *

#from python2db.mysrc.ccm_component_oper import get_component_id_by_category_name

current_testcase_id = -1
current_testcase_row = None

def HitCache_testcase(casename,report_id):
    global current_testcase_row
    if current_testcase_row is None:
        return -1
    if casename == current_testcase_row[3] and report_id == current_testcase_row[1]:
        return current_testcase_row[0]
    return -1

# return recordset of one test case
def getone_testcase_by_name_inner(casename,report_id):
    global current_testcase_row
    global current_testcase_id


    sql_find = "SELECT * FROM test_case WHERE (case_name = '%s' && report_id =%d)" \
               % (
                   casename,report_id)
    print(sql_find)

    try:
        conn = get_ccmdb()
        cursor = conn.cursor()
        cursor.execute(sql_find)

        # results是个元组对象
        results = cursor.fetchone()
        # 先判断是否为空
        if results is None:
            #debugstr = "[ERROR]查询为空:casename=%d,report_id=%d" \
            #        % (casename,report_id )

            #print(debugstr)
            return None
        # else:
        #     print(results)
        # x = len(results)

        current_testcase_row = results
        case_id = results[0]
        current_testcase_id = case_id
        print("case_id=%d" % (case_id))
        return results
    except Exception as ex:
        print('<ERROR>getone_testcase_by_name failed')
        print(ex)
        return None

# return recordset of one test case
def getone_testcase_by_name(casename,report_id):
    global current_testcase_row
    global current_testcase_id
    if HitCache_testcase(casename,report_id)>0:
        return current_testcase_row
    return getone_testcase_by_name_inner(casename,report_id)


# 用例启动时调用，这里的设计是这样的：板卡侧分为管理者和执行者两个任务，
# insert动作由管理者发起。表述的含义是，本板卡下一个将要启动的测试是这里发来的信息
# 注意：当前category_name实际是component name

def ccmdb_insert_resultcase(casename, reportid, category_name, package_name, teststatus, testlog, testnote, datetime_str):

    sql_insert=''
    try:
        conn=get_ccmdb()

        componentid = get_component_id_by_category_name(conn,category_name)

        sql_insert = "INSERT INTO test_case(report_id,component_id,case_name, category, package_name,status,log,note,execdatetime,starttime) VALUES \
         (%d, %d, '%s', '%s', '%s', %d,'%s','%s','%s','%s')" % (
            reportid, componentid, casename, category_name, package_name, teststatus, testlog, testnote, datetime_str,datetime_str)

        print(sql_insert)

        # strsql = ('62', '7', '3', 'test1', 'zeqomq', '1', null, 'No note')
        # create a cursor
        cursor = conn.cursor()
        # execute SQL statement
        cursor.execute(sql_insert)
        caseid = int(cursor.lastrowid)
        # get ID of last inserted record
        print("ID of last record is ", int(cursor.lastrowid))  # 最后插入行的主键ID
        print("ID of inserted record is ",
              int(conn.insert_id()))  # 最新插入行的主键ID，conn.insert_id()一定要在conn.commit()之前，否则会返回0
        conn.commit()
        # 增加统计信息
        oldstatus=110
        ccmdb_update_case_component(0,oldstatus,componentid,category_name,reportid,teststatus)
        return caseid

    except Exception as ex:
        print('<ERROR>ccmdb_insert_resultcase failed')
        print("<ERROR> %s" % (sql_insert))
        print(ex)

        return -1

# 这里的设计是这样的：板卡侧分为管理者和执行者两个任务，
# 板卡侧的用例执行结束时调用，由执行者调用。这样设计暗未管理者在启动用例后，用例可能会中止
# 修改全部元素
# 注意：当前category_name实际是component name
def ccmdb_update_testcase(casename, report_id, category_name, package_name, teststatus, testlog, testnote,
                           execdatetime_str):
    sql_update=''
    try:
        conn=get_ccmdb()

        target_testcase_row = getone_testcase_by_name(casename, report_id)
        if target_testcase_row is None:
            # debugstr = "[ERROR]查询为空:casename=%d,report_id=%d"      % (casename,report_id )
            # print(debugstr)
            case_id=    ccmdb_insert_resultcase(casename, report_id, category_name, package_name, teststatus, testlog, testnote,
                                    execdatetime_str)
            #update component stastic info
            return case_id

        case_id = target_testcase_row[0] # component_id
        component_id = target_testcase_row[2] # component_id
        starttime = target_testcase_row[10] #'starttime'

        sql_update = "UPDATE test_case SET report_id = %d, component_id = %d, case_name = '%s', " \
                     "category = '%s', package_name = '%s', status = %d, log = '%s', note = '%s', execdatetime = '%s', starttime='%s' " \
                     "WHERE (case_id = %d) " \
                     % (
                         report_id, component_id, casename, category_name, package_name, teststatus, testlog, testnote,
                         execdatetime_str,starttime,case_id)

        print(sql_update)

        # strsql = ('62', '7', '3', 'test1', 'zeqomq', '1', null, 'No note')
        # create a cursor
        cursor = conn.cursor()
        cursor.execute(sql_update)
        conn.commit()
        oldstatus = target_testcase_row[6]  # 'starttime'
        ccmdb_update_case_component(1,oldstatus, component_id, category_name, report_id, teststatus)

        getone_testcase_by_name_inner(casename, report_id)

        return case_id

    except Exception as ex:
        print('<ERROR>ccmdb_update_testcase failed')
        print("sql_update: %s" % (sql_update))
        print(ex)

        return -1

# 用例启动时调用，这里的设计是这样的：板卡侧分为管理者和执行者两个任务，
# 用例执行结束时调用。由管理者调用
#============================具体业务相关的====================
def ccmdb_test_end(casename, report_id, teststatus, testlog, testnote,
                           execdatetime_str):

    try:
        conn=get_ccmdb()

        target_testcase_row = getone_testcase_by_name(casename, report_id)
        if target_testcase_row is None:
            debugstr = "[ERROR]查询为空:casename=%d,report_id=%d" \
                    % (casename,report_id )
            print(debugstr)
            return -1

        component_id = target_testcase_row['component_id']
        category_name = target_testcase_row['category_name']
        package_name = target_testcase_row['package_name']

        sql_update = "UPDATE test_case SET case_id = %d, report_id = %d, component_id = %d, case_name = '%s', " \
                     "category = '%s', package_name = '%s', status = %d, log = '%s', note = '%s', execdatetime` = '%s' " \
                     "WHERE (reportid = %d && casename = '%s') " \
                     % (
                         report_id, component_id, casename, category_name, package_name, teststatus, testlog, testnote,
                         execdatetime_str)

        print(sql_update)

        # strsql = ('62', '7', '3', 'test1', 'zeqomq', '1', null, 'No note')
        # create a cursor
        cursor = conn.cursor()
        # execute SQL statement
        cursor.execute(sql_update)
        caseid = int(cursor.lastrowid)
        # get ID of last inserted record
        print("ID of last record is ", int(cursor.lastrowid))  # 最后插入行的主键ID
        print("ID of inserted record is ",
              int(conn.insert_id()))  # 最新插入行的主键ID，conn.insert_id()一定要在conn.commit()之前，否则会返回0
        conn.commit()
        return caseid

    except Exception as ex:
        print('push_ccmtesting_result failed')
        print(ex)

        return -1
