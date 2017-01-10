#!/usr/bin/python2.7
# coding=utf-8
# -*- coding: utf-8 -*-
#One instance script
#Muchina


import logging
import os
import sys


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] (%(threadName)-10s) %(message)s', filename='/opt/scripts/one_instance/one_instance.log')
log = logging.getLogger("reminder")


def main():
    #Will ensure only one instance will run at any given time through storing the pid
    pid = str(os.getpid())
    pidfile = "/tmp/one_instance.pid"

    if os.path.isfile(pidfile):
        print "%s already exists, exiting" % pidfile
        log.info("Instance of script already running")
        sys.exit()
    file(pidfile, 'w').write(pid)
    try:
        #your functions go here
        function()
    except Exception, e:
        print e.message
        log.error("Error :" + format(e.message))
    finally:
        os.unlink(pidfile)


#Run the main function
main()
