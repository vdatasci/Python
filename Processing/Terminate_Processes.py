import psutil

for p in psutil.process_iter():
    print(p)

psutil.Process(7016).terminate()


##################################

import psutil

PROCNAME = "python.exe"

for proc in psutil.process_iter():
    # check whether the process name matches
    if proc.name() == PROCNAME:
        proc.kill()
