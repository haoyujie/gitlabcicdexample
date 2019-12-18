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

#from python2db.mysrc.ccm_component_oper import get_component_id_by_category_name

current_case_component_id = -1
current_case_component_row = None

def HitCache_case_component(component_name,report_id):
    global current_case_component_row
    if current_case_component_row is None:
        return -1
    if component_name == current_case_component_row[2] and report_id == current_case_component_row[3]:
        return current_case_component_row[0]
    return -1

# return recordset of one test case
def getone_case_component_by_name_inner(component_name,report_id):
    global current_case_component_row
    global current_case_component_id


    sql_find = "SELECT * FROM case_component WHERE (component_name = '%s' && report_id =%d)" \
               % (
                   component_name,report_id)
    print(sql_find)

    try:
        conn = get_ccmdb()
        cursor = conn.cursor()
        cursor.execute(sql_find)

        # results是个元组对象
        results = cursor.fetchone()
        # 先判断是否为空
        if results is None:
            debugstr = "[ERROR]查询为空:component_name=%d,report_id=%d" \
                    % (component_name,report_id )

            print(debugstr)
            return None
        # else:
        #     print(results)
        # x = len(results)

        case_id = results[0]
        current_case_component_row = results
        current_case_component_id = case_id
        print("case_id=%d" % (case_id))
        return results
    except Exception as ex:
        print('<ERROR>getone_case_component_by_name failed')
        print(ex)
        return None

# return recordset of one test case
def getone_case_component_by_name(component_name,report_id):
    global current_case_component_row
    global current_case_component_id
    if HitCache_case_component(component_name,report_id)>0:
        return current_case_component_row
    return getone_case_component_by_name_inner(component_name,report_id)


# 用例启动时调用，这里的设计是这样的：板卡侧分为管理者和执行者两个任务，
# insert动作由管理者发起。表述的含义是，本板卡下一个将要启动的测试是这里发来的信息
# 注意：当前category_name实际是component name

def ccmdb_insert_case_component(component_info_id,component_name,report_id,total_case,execute_case,pass_case,
                                blocked_case,fail_case):

    sql_insert=''
    try:
        conn=get_ccmdb()

        #componentid = get_component_id_by_category_name(conn,category_name)

        sql_insert = "INSERT INTO case_component(component_id,component_name,report_id,total_case,execute_case,pass_case,blocked_case,fail_case) VALUES \
                 (%d, '%s' , %d,  %d, %d, %d, %d, %d )" % (
            component_info_id,component_name,report_id,total_case,execute_case,pass_case,blocked_case,fail_case)


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
        return caseid

    except Exception as ex:
        print('<ERROR>ccmdb_insert_case_component failed')
        print("<ERROR> %s" % (sql_insert))
        print(ex)

        return -1


# 这里的设计是这样的：板卡侧分为管理者和执行者两个任务，
# 板卡侧的用例执行结束时调用，由执行者调用。这样设计暗未管理者在启动用例后，用例可能会中止
# 修改全部元素
# 注意：当前category_name实际是component name
def ccmdb_update_case_component(havetestrecord,oldstatus,component_info_id,component_name,report_id,teststatus):
    sql_update=''
    try:
        conn=get_ccmdb()

        case_component_id=0

        total_case=0
        execute_case=0
        pass_case=0
        blocked_case=0
        fail_case=0

        target_case_component_row = getone_case_component_by_name(component_name, report_id)
        #1  ===========================================
        if target_case_component_row is None:
            # debugstr = "[ERROR]查询为空:component_name=%d,report_id=%d"      % (component_name,report_id )
            # print(debugstr)
            case_component_id=    ccmdb_insert_case_component(component_info_id,component_name,report_id,total_case,execute_case,pass_case,blocked_case,
                                fail_case)
        #2  ============================================
        if not target_case_component_row is None:
            case_component_id = target_case_component_row[0] # component_id
            component_id = target_case_component_row[2] # component_id

            total_case = target_case_component_row[4]
            execute_case = target_case_component_row[5]
            pass_case = target_case_component_row[6]
            blocked_case = target_case_component_row[7]
            fail_case = target_case_component_row[8]

        # 3  ============================================
        if(110==teststatus or 0==havetestrecord):
            total_case += 1
            execute_case += 1
            if (110==teststatus): # 第一次insert
                blocked_case += 1

        if (1==havetestrecord):  # testcase result 已存在
            if(oldstatus==110):  # if last oper is insert
                blocked_case -= 1

        if (0==teststatus):
            fail_case += 1
        elif (1==teststatus):
            pass_case += 1
        elif (2 == teststatus):
            blocked_case+=1

        sql_update = "UPDATE case_component SET " \
                "component_name = '%s',report_id = %d, total_case = %d, " \
                "execute_case =%d, pass_case = %d, blocked_case = %d, fail_case = %d " \
                "WHERE (case_component_id = %d) " \
                     % (
                          component_name, report_id, total_case, execute_case, pass_case, blocked_case, fail_case,case_component_id)

        print(sql_update)

        # strsql = ('62', '7', '3', 'test1', 'zeqomq', '1', null, 'No note')
        # create a cursor
        cursor = conn.cursor()
        cursor.execute(sql_update)
        conn.commit()

        getone_case_component_by_name_inner(component_name, report_id)
        # target_case_component_row[4] = total_case
        # target_case_component_row[5] = execute_case
        # target_case_component_row[6] = pass_case
        # target_case_component_row[7] = blocked_case
        # target_case_component_row[8] = fail_case

        return case_component_id

    except Exception as ex:
        print('<ERROR>ccmdb_update_case_component failed')
        print("sql_update: %s" % (sql_update))
        print(ex)

        return -1
