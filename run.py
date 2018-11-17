#! /usr/bin/python3

global recordCount
import trademe
import datetime
import backup
import time
# import sendnotification

logFile = open('/home/trademebot/tmdata_log.csv', 'a+')
logFile.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ': Initiated run \n')

trademe.trademescraper()

iteration = 0

while trademe.recordCount < 2077 and iteration < 3:
    print('Only ' + str(trademe.recordCount) + ' records identified! Will auto retry in 20 minutes...')
    logFile.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ': Only ' + str(trademe.recordCount) + ' records identified! Will auto retry in 10 minutes...' + '\n')
    for i in range(1200):
        time.sleep(1)
    trademe.trademescraper()
    iteration = iteration + 1

finalRecordCount = 0

if trademe.recordCount >= 2077:
    finalRecordCount = 0
    finalOutFile = open('/home/trademebot/tmdata.csv', 'a')
    outFile = open('/home/trademebot/tmdata_temp.csv', 'r')
    for line in outFile:
        finalOutFile.write(line)
        finalRecordCount = finalRecordCount + 1
    finalOutFile.close()
    outFile.close()
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ': Wrote ' + str(finalRecordCount) +  ' records to tmdata.csv \n')
    logFile.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ': Wrote ' + str(finalRecordCount) +  ' records to tmdata.csv \n')

backup.backup()
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ': Backup suceeded... \n')
logFile.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ': Backup suceeded... \n')

# sendnotification.sendmail('TM bot update','Completed successfully! ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n With ' + str(finalRecordCount) + ' records written.' )

logFile.close()
