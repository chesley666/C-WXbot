from datetime import datetime
import subprocess
import time,os
from config.mediaconfig import ANDROID_QRCODE_PATH,PC_JIANYING_PATH

def killadb():
    try:# 检查是否有adb进程
        subprocess.call("taskkill /IM adb.exe /F", shell=True)
        print("所有adb进程已被杀死。")
        time.sleep(1)
    except subprocess.CalledProcessError as e:
        print("发生错误：", e)

def pushqrcode(qrname):
    adb_command = ['adb', 'push', os.path.join(PC_JIANYING_PATH,qrname), f'{ANDROID_QRCODE_PATH}/{qrname}']
    adb_output = subprocess.check_output(adb_command).decode('utf-8')
    return f'{ANDROID_QRCODE_PATH}/{qrname}'

def freshgallery(qrpath):
    adb_cmd = ['adb','shell','am','broadcast','-a android.intent.action.MEDIA_SCANNER_SCAN_FILE',f'-d file://{qrpath}']
    adb_output = subprocess.check_output(adb_cmd).decode('utf-8')

def rmqrcode(qrpath):
    adb_command = ['adb', 'shell',f'rm {qrpath}']
    subprocess.check_output(adb_command).decode('utf-8')