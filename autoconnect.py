from pywinauto import application
import time
import os

os.system('taskkill /IM ncStarter* /F /T')
os.system('taskkill /IM CpStart* /F /T') 
os.system('taskkill /IM DibServer* /F /T') 
os.system('wmic process where "name like \'%ncStarter%\'" call terminate') 
os.system('wmic process where "name like \'%CpStart%\'" call terminate') 
os.system('wmic process where "name like \'%DibServer%\'" call terminate')

time.sleep(5)        

app = application.Application()
app.start('C:\DAISHIN\STARTER\\ncStarter.exe /prj:cp /id:hw7120 /pwd:calpjr35 /pwdcert:* /autostart')
time.sleep(60)
