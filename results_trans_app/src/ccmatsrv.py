#!/usr/bin/env python
# encoding: utf8
#
import datetime

from spyne import Application, rpc, ServiceBase, Iterable, Integer, Unicode

from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication



class CCMTstService(ServiceBase):
    @rpc( Unicode,Integer, Unicode, Integer, Unicode, _returns=Unicode)
    def push_ccmtesting_result(ctx,  casename, reportid, category, status, log):
        """Docstrings for service methods appear as documentation in the wsdl.
        <b>What fun!</b>

        @param casename is test machinename
        @param reportid is lava job id
        @param category is cate
        @param status is result of test
        @param log is execute log
        @return the result of push to db
        """
        print(casename)
        print(reportid)
        print(category)


        now_time = datetime.datetime.now()
        time1_str = datetime.datetime.strftime(now_time, '%Y-%m-%d %H:%M:%S')
        print(time1_str)

        #yield u'Hello, %s' % name
        return "SUCCEED0"
        #for i in range(3):
        #    yield u'Hello, %s' % name

application = Application([CCMTstService], 'spyne.examples.hello.soap',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)


if __name__ == '__main__':
    import logging

    from wsgiref.simple_server import make_server

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

    logging.info("listening to http://pek-lpd-ccm1:9005")
    logging.info("wsdl is at: http://pek-lpd-ccm1:9005/?wsdl")

    server = make_server('128.224.179.178', 9005, wsgi_application)
    server.serve_forever()
    print('error')

