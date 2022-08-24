import requests,os
from time import sleep
import hashlib
from tkinter import messagebox
import time
import random
from datetime import datetime
def logo():
    os.system('cls')
    log="""
\033[1;32m   _  _ ___                    _____    _____   ______   ___________  ______        ___       __ 
\033[1;33m  | |/ || |                   |  _  \  |  ___| |  __  | |____  ____| |  __  \      / _ \     |__|
\033[1;34m  | ' / | |__   ____   ___ _  | | |  | | |___  | |__| |     |  |     | |__)  |    / /_\ \     __ 
\033[1;36m  |  <  | '_ \|/  _ \ /  _ `| | | |  | |  ___| |  ____|     |  |     |      /    /  ___  \   |  | 
\033[1;31m  | . \ | | | |  (_)    (_) | | |_/  | | |___  | |          |  |     |  __  \   /  /   \  \  |  |
\033[1;36m  |_|\_||_| |_|\____/ \___,_| |_____/  |_____| |_|          |__|     |_|  \__\ /__/     \__\ |__|
 \033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
 \033[1;97m[\033[1;91m✓\033[1;97m] => \033[1;31mCopyright By: \033[1;32mVũ Đình Khoa
 \033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
 \033[1;97m[\033[1;91m✓\033[1;97m] => \033[1;33mTool Làm Hắc Cơ 2022 
 \033[1;97m[\033[1;91m✓\033[1;97m]\033[1;97m => \033[1;91mZalo : \033[1;94m0354008375
 \033[1;97m[\033[1;91m✓\033[1;97m]\033[1;97m => \033[1;91mFacebook : \033[1;94mhttps://www.facebook.com/KhoaLaHacker.No1
 \033[1;97m[\033[1;91m✓\033[1;97m]\033[1;97m => \033[1;91mDonate cho admin momo : \033[1;94m0354008375
 \033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - -"""
    print(log)

def cre_mã():
    số_kí_tự_in_chuỗi = 8
    kí_tự_số = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  
    kí_tự_chữ = ['A', 'B', 'Y',
                        'Z']
    set_chuỗi = kí_tự_số + kí_tự_chữ
    random_số = random.choice(kí_tự_số)
    random_chữ = random.choice(kí_tự_chữ)
    ghép = random_số + random_chữ
    for x in range(số_kí_tự_in_chuỗi):
        ghép = ghép + random.choice(set_chuỗi)
        import array
        ghép_list = array.array('u', ghép)
        random.shuffle(ghép_list)
    password = "Team-Py-"
    for x in ghép_list:
            password = password + x
    return password
logo()


fol_mã=r"C:\System\AppData\Win32\FINN\Program\Auto-TDS-TTC-YTB"
if os.path.exists(fol_mã) == False:
    os.makedirs(fol_mã, mode=0o777, exist_ok=True)
elif os.path.exists(fol_mã) == True:
    pass
if os.path.exists(f'{fol_mã}\device.txt')==False:
    mã_máy=cre_mã()
    filea=open(f'{fol_mã}\device.txt', "w+")
    filea.write(mã_máy)
    filea.close()
dev=open(f'{fol_mã}\device.txt', "r")
device=dev.read()
dev.close()
dev=open(f'{fol_mã}\device.txt', "r")
device=dev.read()
dev.close()
if os.path.exists(fol_mã) == False:
    os.makedirs(fol_mã, mode=0o777, exist_ok=True)
elif os.path.exists(fol_mã) == True:
    pass
he=hashlib.md5(bytes('FINN-'+str(device), 'utf-8-sig')).hexdigest()
device='FINN-'+str(he[0:14])
try:
    check_key=requests.get('https://pastebin.com/raw/VzPEJ9qA').text
except:
    check_key=requests.get('https://pastebin.com/raw/VzPEJ9qA').text
if device in check_key:
    pass
else:
    print(f'\033[1;31m[\033[1;32m●\033[1;31m]\033[1;32m Mã Máy: \033[1;36m{device}')
    messagebox.showwarning('Thông báo', 'Thiết bị chưa được kích hoạt\nLiên hệ admin để mua key\nZalo admin: 0393203943')
    time.sleep(100)
    quit()

logo()

cookiefb=input("\033[0;32mNhập Cookie Facebook:\033[1;95m ")
cookie=input("\033[0;32mNhập Cookie Web:\033[1;95m ")
link=input("\033[0;32mNhập ID Post:\033[1;95m ")
typelike=input("\033[0;32mNhập Type Reactions\033[1;32m(like,love,haha,angry,wow,sad):\033[1;95m ")
def rundelay(k):
  while (k>0):
    
    k=k-1
    print(f'\033[0;31m[ | ]\033[0;33m Vui Lòng Đợi '+str(k), end='\r')
    sleep(0.25)
    print(f'\033[0;31m[ / ]\033[0;33m Vui Lòng Đợi '+str(k), end='\r')
    sleep(0.25)
    print(f'\033[0;31m[ - ]\033[0;33m Vui Lòng Đợi '+str(k), end='\r')
    sleep(0.25)
    print(f'\033[0;31m[ \ ]\033[0;33m Vui Lòng Đợi '+str(k), end='\r')
    sleep(0.25)
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
headers={
  "Host":"rpwliker.com",
  "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
  "x-requested-with": "mark.via.gq",
  "content-type":"application/x-www-form-urlencoded",
  "cookie":cookie
}
t33=requests.get("https://rpwliker.com/feed",headers=headers).text
t4=t33.split(' <meta name="csrf-token" content="')[1].split('">')[0]
hd={
  "x-csrf-token":t4,
  "Host":"rpwliker.com",
  "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
  "x-requested-with": "mark.via.gq",
  "content-type":"application/x-www-form-urlencoded",
  "cookie":cookie
}
data={
  "send_to": link,
  "quantity": "40",
  "reaction_type[]": typelike,
  "local_only": "0",
  "relevant_accounts_only": "0"
}
stt=0
while True:
  stt=stt+1
  t3=requests.post("https://rpwliker.com/autoreaction",headers=hd,data=data).text
  sleep(65)
  check_dv = requests.get(f'https://mbasic.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier={link}&hash=AeTkxnH8LFuk5Gk10G0&refid=13', headers = {
                        'Host': 'mbasic.facebook.com',
                        'cache-control': 'max-age=0',
                        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
                        'sec-ch-ua-mobile': '?1',
                        'save-data': 'on',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.115 Mobile Safari/537.36',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'sec-fetch-site': 'none',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-user': '?1',
                        'sec-fetch-dest': 'document',
                        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                        'cookie': cookiefb
                        }).text
  t=check_dv.split('role="button" aria-pressed="true" href="')[1].split('">Tất cả ')[0]
  t2=t.split('total_count=')[1].split('"')[0]
  time=datetime.now().strftime("%H:%M:%S")
  print(f"\033[1;33mTQT\033[1;37m [\033[1;32m{time}\033[1;37m] \033[1;37m=> \033[1;95mSuccessful \033[1;37m=> \033[1;95m+40 Reactions \033[1;37m=> \033[1;33m{t2} \033[1;32mReactions")
  k=1150
  rundelay(k)
