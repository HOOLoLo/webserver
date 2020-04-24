from flask_cors import CORS
from selenium import webdriver
from flask import Flask
from selenium.webdriver.chrome.options import Options
import socket
import pyautogui
import time
import pandas as pd
app = Flask(__name__)

chrome_options=Options()
# chrome_options.add_argument("--kiosk")
chrome_options.add_experimental_option('useAutomationExtension',False)
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
chrome_options.add_argument("--allow-file-access-from-files")
driver=webdriver.Chrome('chromedriver.exe',chrome_options=chrome_options)
time.sleep(3)

pyautogui.hotkey('F11')

dic={}
def getList():
    csv_data=pd.read_csv('https://raw.githubusercontent.com/HOOLoLo/webserver/master/content.csv')
    print(csv_data)
    for index,value in enumerate(csv_data['name']):
        dic[value]=csv_data['path'][index]
    print(dic)

@app.route('/url/<pageName>')
def getOrder(pageName):
    print(pageName)
    getList()
    driver.get(dic[pageName])
    if pageName=='音乐' :
        time.sleep(1)
        pyautogui.click(x=0, y=500)
    if pageName == 'NASA':
        time.sleep(1)
        pyautogui.click(x=500, y=500)

    # driver.manage().window().fullscreen
    return 'done'
@app.route('/volume/<order>')
def setVolume(order):
    if order=='up':
        pyautogui.keyDown('volumeup')
    elif order=='down':
        pyautogui.keyDown('volumedown')



@app.route('/favicon.ico')
def favicon():
    return

if __name__=='__main__':
    CORS(app,supports_credential=True)
    hostname = socket.gethostname()
    # 获取本机IP1111
    ip = socket.gethostbyname(hostname)
    print(ip)
    app.run(host=ip,port=7777,debug=False)