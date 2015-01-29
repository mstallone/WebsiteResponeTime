import requests
import datetime
import sys
import subprocess

subprocess.call("sudo discoveryutil udnsflushcaches", shell=True)

totalTime = datetime.timedelta(0,0)

for i in range(int(sys.argv[2])):
    totalTime += requests.request('GET', str(sys.argv[1])).elapsed
    
print(str(totalTime/int(sys.argv[2])))
