# -*- coding: utf-8 -*-
import requests
import json
import binascii
import nfc
import time
from threading import Thread, Timer

prams = json.load('params.json')
token = params['token']
device_id = params['device_id']
idm_list = params['idm_list']

url = 'https://api.candyhouse.co/public/sesame/' + device_id
head = {'Content-type': 'application/json', 'Authorization': token}

# Suica待ち受けの1サイクル秒
TIME_cycle = 1.0
# Suica待ち受けの反応インターバル秒
TIME_interval = 0.2
# タッチされてから次の待ち受けを開始するまで無効化する秒
TIME_wait = 3

# NFC接続リクエストのための準備
# 212F(FeliCa)
target_req_suica = nfc.clf.RemoteTarget('212F')
# 0003(Suica)
target_req_suica.sensf_req = bytearray.fromhex('0000030000')

print('Waiting for SUICA...')
while True:
    # USBに接続されたNFCリーダに接続してインスタンス化
    clf = nfc.ContactlessFrontend('usb')
    # Suica待ち受け開始
    # clf.sense( [リモートターゲット], [検索回数], [検索の間隔] )
    target_res = clf.sense(target_req_suica, iterations=int(TIME_cycle//TIME_interval)+1 , interval=TIME_interval)
    
    if target_res is not None:
        
        tag = nfc.tag.activate_tt3(clf, target_res)
        tag.sys = 3
        
        #idmを取り出す
        idm = binascii.hexlify(tag.idm).decode()
        print('suica detected. idm =', idm)
        
        if idm in idm_list:
            
            locked = requests.get(url, headers=head).json()['locked']
            
            # unlock/lock Sesame with token
            command = {'command':'unlock'} if locked else {'command':'lock'}
            response = requests.post(url, headers=head, data=json.dumps(command))
            print(response.text)
        
        print('sleep ' + str(TIME_wait) + ' seconds')
        time.sleep(TIME_wait)
    clf.close()
