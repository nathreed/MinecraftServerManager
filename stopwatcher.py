#!/usr/bin/python

import subprocess
import time

#Config options
#Path to the server folder
serverFolderPath = "/home/nathan/Desktop/TestScreenServer"
#Path to the log
serverLogPath = serverFolderPath + "/logs/latest.log"

serverLog = open(serverLogPath)

serverLog.seek(0,2)
while True:
        line = serverLog.readline()
        if not line:
                time.sleep(1)
        else:
                if "Stopping server" in line:
                        time.sleep(5) #give the server time to shut down
                        subprocess.Popen(["bash", "cleanup.sh"])
