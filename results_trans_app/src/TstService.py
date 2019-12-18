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

from ccm_utils import *
from ccmdboper import *
from ccm_project_oper import *
from ccm_reporttbl_oper import *
from ccm_testcase_oper import *




class CCMTstService(ServiceBase):
    # ================================================================
    #   test case
    # ===============================================================
    @rpc(Unicode, Integer, Unicode, Unicode, _returns=Unicode)
    def test_case_start(ctx, casename, reportid, category, packagename):
        """Docstrings for service methods appear as documentation in the wsdl.
        <b>What fun!</b>

        @param casename is test machinename
        @param reportid is lava job id
        @param category is cate
        @param status is result of test
        @param log is execute log
        @return the result of push to db
        """

        try:
            print(casename)
            print(reportid)
            print(category)
            conn=get_ccmdb()
            now_time = datetime.datetime.now()
            time1_str = datetime.datetime.strftime(now_time, '%Y-%m-%d %H:%M:%S')
            print(time1_str)

            casename = transferContent(casename)
            category = transferContent(category)

            status=110
            log=''


            if (ccmdb_insert_resultcase(casename, reportid, category, packagename, status, log, '', time1_str) > 0):

                return "SUCCEED"
            else:
                try:
                    conn.close()
                    open_ccmtcdb()
                    return "FIELD:1:dbopenfailed"
                except:
                    return "FIELD:2:dbopenexception"

        except:
            print('push_ccmtesting_result failed')
            return "FIELD:3:pushexception"

    # insert full data to test case table
    @rpc(Unicode, Integer, Unicode, Unicode, Integer, Unicode, _returns=Unicode)
    def push_ccmtesting_result(ctx, casename, reportid, category, package, status, log):
        """Docstrings for service methods appear as documentation in the wsdl.
        <b>What fun!</b>

        @param casename is test machinename
        @param reportid is lava job id
        @param category is cate
        @param status is result of test
        @param log is execute log
        @return the result of push to db
        """

        try:
            print(casename)
            print(reportid)
            print(category)
            conn=get_ccmdb()
            now_time = datetime.datetime.now()
            time1_str = datetime.datetime.strftime(now_time, '%Y-%m-%d %H:%M:%S')
            print(time1_str)

            casename = transferContent(casename)
            category = transferContent(category)
            log = transferContent(log)

            if (ccmdb_insert_resultcase(casename, reportid, category, package, status, log, '', time1_str) > 0):
                return "SUCCEED"
            else:
                try:
                    conn.close()
                    open_ccmtcdb()
                    return "FIELD:1:dbopenfailed"
                except:
                    return "FIELD:2:dbopenexception"

        except:
            print('push_ccmtesting_result failed')
            return "FIELD:3:pushexception"


    # insert or update data to test case table
    @rpc(Unicode, Integer, Unicode, Unicode, Integer, Unicode, _returns=Unicode)
    def push_ccmtesting_result_Ex(ctx, casename, reportid, category, package, status, log):
        """Docstrings for service methods appear as documentation in the wsdl.
        <b>What fun!</b>

        @param casename is test machinename
        @param reportid is lava job id
        @param category is cate
        @param status is result of test
        @param log is execute log
        @return the result of push to db
        """

        try:
            print(casename)
            print(reportid)
            print(category)
            conn=get_ccmdb()
            now_time = datetime.datetime.now()
            time1_str = datetime.datetime.strftime(now_time, '%Y-%m-%d %H:%M:%S')
            print(time1_str)

            casename = transferContent(casename)
            category = transferContent(category)
            log = transferContent(log)


            if (ccmdb_update_testcase(casename, reportid, category, package, status, log, '', time1_str) > 0):
                return "SUCCEED"
            else:
                try:
                    conn.close()
                    open_ccmtcdb()
                    return "FIELD:1:dbopenfailed"
                except:
                    return "FIELD:2:dbopenexception"

        except:
            print('push_ccmtesting_result_Ex failed')
            return "FIELD:3:pushexception"


    @rpc(Unicode, Integer, Integer, Unicode, _returns=Unicode)
    def test_case_end(ctx, casename, report_id, status, log ):
        """Docstrings for service methods appear as documentation in the wsdl.
        <b>What fun!</b>

        @param casename is test machinename
        @param reportid is lava job id
        @param category is cate
        @param status is result of test
        @param log is execute log
        @return the result of push to db
        """

        try:
            print(casename)
            print(report_id)

            conn=get_ccmdb()
            global current_testcase_row
            global current_testcase_id
            # if(current_testcase_id==
            current_testcase_row = None
            # find current recorder

            casename = transferContent(casename)
            target_testcase_row = getone_testcase_by_name(casename, report_id)

            if target_testcase_row is None:
                print("[ERROR] cannot find recordset")
                return 0

            now_time = datetime.datetime.now()
            time1_str = datetime.datetime.strftime(now_time, '%Y-%m-%d %H:%M:%S')
            print(time1_str)

            category = target_testcase_row[4]
            package=target_testcase_row[5]
            log = transferContent(log)

            if (ccmdb_update_testcase(casename, report_id, category, package, status, log, '', time1_str) > 0):
                return "SUCCEED"
            else:
                try:
                    conn.close()
                    open_ccmtcdb()
                    return "FIELD:1:dbopenfailed"
                except:
                    return "FIELD:2:dbopenexception"
        except Exception as ex:
            print(ex)
            print('push_ccmtesting_result failed')
            return "FIELD:3:pushexception"

    #================================================================
    #   test report
    # ===============================================================
    @rpc(Integer, Unicode, Integer, Unicode, _returns=Unicode)
    def init_test_report(ctx, report_id, report_name, rcpl, project_name):
        """Docstrings for service methods appear as documentation in the wsdl.
        <b>What fun!</b>

        @param report_id is lave report id
        @param report_name is jenkins project name
        @param rcpl is source of project rcpl
        @param project_name is proect name
        @return the result of push to test_report table
        """

        try:

            conn=get_ccmdb()
            now_time = datetime.datetime.now()
            report_date = datetime.datetime.strftime(now_time, '%Y-%m-%d %H:%M:%S')
            print("reportdate:", str(report_date))
            print("reportid: ", str(report_id))

            project_id = get_projectid_by_name(conn,project_name)

            if (write2ccmdb_test_report(report_id, report_name, rcpl, report_date, project_id) > 0):
                return "SUCCEED"
            else:
                try:
                    conn.close()
                    open_ccmtcdb()
                    return "FIELD:1:dbopenfailed"
                except:
                    return "FIELD:2:dbopenexception"


        except Exception as ex:
            print(ex)
            print('init_test_report failed')
            return "FIELD:3:pushexception"

    @rpc(Integer, Unicode, Unicode, Unicode, Integer, Integer, Integer, Integer, Integer, _returns=Unicode)
    def init_test_report_v2(ctx, report_id, report_name, rcpl_str, project_name, execute_case, total_case, pass_case,
                         fail_case, blocked_case):
        """Docstrings for service methods appear as documentation in the wsdl.
        <b>What fun!</b>

        @param report_id is lave report id
        @param report_name is jenkins project name
        @param rcpl is source of project rcpl
        @param project_name is proect name
        @return the result of push to test_report table
        """

        try:

            conn=get_ccmdb()
            now_time = datetime.datetime.now()
            report_date = datetime.datetime.strftime(now_time, '%Y-%m-%d %H:%M:%S')
            print("reportdate:", str(report_date))
            print("reportid: ", str(report_id))

            rcpl=0

            if len(rcpl_str) > 0:
                rcpl = int(rcpl_str)

            project_id = get_projectid_by_name(conn,project_name)

            cur_report_row = getone_report_by_reportid(report_id)
            if cur_report_row is None:
                if (write2ccmdb_test_report(report_id, report_name, rcpl, report_date, project_id) > 0):
                    return "SUCCEED"
                else:
                    try:
                        conn.close()
                        open_ccmtcdb()
                        return "FIELD:1:dbopenfailed"
                    except:
                        return "FIELD:2:dbopenexception"

            if (update2ccmdb_test_report(report_id, report_name, rcpl, report_date, project_id, execute_case,
                                         total_case,
                                         pass_case, fail_case, blocked_case,report_date) > 0):
                return "SUCCEED"
            else:
                try:
                    conn.close()
                    open_ccmtcdb()
                    return "FIELD:1:dbopenfailed"
                except:
                    return "FIELD:2:dbopenexception"

        except Exception as ex:
            print(ex)
            print('init_test_report failed')
            return "FIELD:3:pushexception"


    @rpc(Integer, Unicode, Integer, Unicode, Integer, Integer, Integer, Integer, Integer, _returns=Unicode)
    def update_test_report(ctx, report_id, report_name, rcpl, project_name, execute_case, total_case, pass_case,
                         fail_case, blocked_case):
        """Docstrings for service methods appear as documentation in the wsdl.
        <b>What fun!</b>

        @param report_id is lave report id
        @param report_name is jenkins project name
        @param rcpl is source of project rcpl
        @param project_name is proect name
        @param execute_case is actually excuted case count
        @param total_case is count of planed
        @param pass_case is count of passed
        @param fail_case is count of fail
        @param blocked_case is blacked
        @return the result of push to test_report table
        """

        try:

            conn=get_ccmdb()

            end_time = datetime.datetime.now()
            report_end_time = datetime.datetime.strftime(end_time, '%Y-%m-%d %H:%M:%S')
            print("report_end_time:", str(report_end_time))
            print("reportid: ", str(report_id))

            project_id = get_projectid_by_name(conn,project_name)

            cur_report_row = getone_report_by_reportid(report_id)
            if cur_report_row is None:
                return "FAIELD:1:REOCRD_DOES_NOT_EXIST"

            start_time = cur_report_row[3]
            report_start_time = datetime.datetime.strftime(start_time, '%Y-%m-%d %H:%M:%S')


            if (update2ccmdb_test_report(report_id, report_name, rcpl, report_start_time, project_id, execute_case, total_case,
                                        pass_case, fail_case, blocked_case,report_end_time) > 0):
                return "SUCCEED"
            else:
                try:
                    conn.close()
                    open_ccmtcdb()
                    return "FIELD:1:dbopenfailed"
                except:
                    return "FIELD:2:dbopenexception"


        except Exception as ex:
            print(ex)
            print('init_test_report failed')
            return "FIELD:3:pushexception"


    @rpc(Integer, _returns=Unicode)
    def end_test_report(ctx, report_id):
        """Docstrings for service methods appear as documentation in the wsdl.
        <b>What fun!</b>

        @param report_id is lave report id
        @param report_name is jenkins project name
        @param rcpl is source of project rcpl
        @param project_name is proect name
        @param execute_case is actually excuted case count
        @param total_case is count of planed
        @param pass_case is count of passed
        @param fail_case is count of fail
        @param blocked_case is blacked
        @return the result of push to test_report table
        """

        try:

            conn=get_ccmdb()

            end_time = datetime.datetime.now()
            report_end_time = datetime.datetime.strftime(end_time, '%Y-%m-%d %H:%M:%S')
            print("report_end_time:", str(report_end_time))
            print("reportid: ", str(report_id))

            cur_report_row = getone_report_by_reportid(report_id)
            if cur_report_row is None:
                return "FAIELD:1:REOCRD_DOES_NOT_EXIST"

            start_time = cur_report_row[3]

            report_start_time = datetime.datetime.strftime(start_time, '%Y-%m-%d %H:%M:%S')

            report_name=cur_report_row[1]
            rcpl=cur_report_row[2]

            project_id=cur_report_row[4]
            execute_case=cur_report_row[5]
            total_case=cur_report_row[6]
            pass_case=cur_report_row[7]
            fail_case=cur_report_row[8]
            blocked_case=cur_report_row[9]


            if (update2ccmdb_test_report(report_id, report_name, rcpl, report_start_time, project_id, execute_case, total_case,
                                        pass_case, fail_case, blocked_case,report_end_time) > 0):
                return "SUCCEED"
            else:
                try:
                    conn.close()
                    open_ccmtcdb()
                    return "FIELD:1:dbopenfailed"
                except:
                    return "FIELD:2:dbopenexception"


        except Exception as ex:
            print(ex)
            print('init_test_report failed')
            return "FIELD:3:pushexception"