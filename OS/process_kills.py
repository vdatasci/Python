import psutil

x = 'HPFS.exe SynTPHelper.exe sttray64.exe SmartMenu.exe GWX.exe HPClientServices.exe HPSA_Service.exe HPWA_Main.exe HPWA_Service.exe QBCFMonitorService.exe LightScribeControlPanel.exe hpservice.exe iPodService.exe iTunesHelper.exe mysqld.exe'.split(' ')

l = []
for proc in psutil.process_iter():
    if proc.name() in x:
        try:
            proc.terminate()
            break
        except:
            print proc.name() + str(' termination was denied...')
    else:
        l.append(proc.name())


l.sort()


import os
for i in x:
    os.system('taskkill /f /im ' + str(i) + '')


os.system('taskkill /f /im SynTPEnh.exe')
os.system('taskkill /f /im YCMMirage.exe')
os.system('taskkill /f /im HPFS.exe')
os.system('taskkill /f /im SynTPHelper.exe')
