#! /usr/bin/python3

import os
import shutil
import datetime

def backup():
    shutil.copy('/home/trademebot/tmdata.csv','/home/trademebot/backups/tmdata' + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.csv')

