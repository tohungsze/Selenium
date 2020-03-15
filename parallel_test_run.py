from subprocess import Popen
import time

startt = time.time()
processes = []

for counter in range(10):
    firefox_cmd = 'export BROWSER=firefox && python testGlocal.py'
    firefox_cmd1 = 'export BROWSER=firefox && python testGlocal.py'
    processes.append(Popen(firefox_cmd, shell=True))
    processes.append(Popen(firefox_cmd1, shell=True))

for counter in range(10):
    processes[counter].wait()

endt = time.time()
time_taken = endt - startt

print("time to finish:", time_taken)
