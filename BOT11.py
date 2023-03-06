import requests
import json
import sys
import os
import time
from requests import session
import datetime
from random import SystemRandom
import random
from datetime import datetime

user = input("Key: ")
import getpass
algoritma = getpass.getpass()
if algoritma == 'op000000' and user == 'ardhy':
    os.system("clear")
else:
    sys.exit(" HUBUNGI DEV BOT")



kolom = os.get_terminal_size().columns

R = "\033[0;31;40m" #RED
G = "\033[0;32;40m" # GREEN
Y = "\033[0;33;40m" # Yellow
B = "\033[0;34;40m" # Blue
N = "\033[0m" # Reset
os.system('clear')
print(Y+"""
       ███████╗███████╗░░░███████╗██╗██╗░░░██╗███████╗
       ██╔════╝██╔════╝░░░██╔════╝██║██║░░░██║██╔════╝
       ██████╗░██████╗░░░░█████╗░░██║╚██░░██╔╝█████╗░░
       ╚════██╗╚════██╗░░░██╔══╝░░██║░╚████╔╝░██╔══╝░░
       ██████╔╝██████╔╝██╗██║░░░░░██║░░╚██╔╝░░███████╗
       ╚═════╝░╚═════╝░╚═╝╚═╝░░░░░╚═╝░░░╚═╝░░░╚══════╝
""")
print("")
print(f"{R}[1] . {G}Win Go")
print(f"{R}[2] . {G}TRX - MAINTENANCE")
pilih = input("Masukkan Pilihan : ")
if pilih == '1':
	os.system("clear")
elif pilih == '2':
	sys.exit("                                                                                                                                    Maintenance goblok, wkkwkwwk")

    
P = '\033[95m'
CYAN = '\033[96m'
DARK = '\033[36m'
B = '\033[94m'
G = '\033[92m'
Y = '\033[93m'
R = '\033[91m'
BO = '\033[1m'
UNDER = '\033[4m'
N = '\033[0m'
			
			
def countdownTimer ():
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'        {G}============ {DARK}Sisa Waktu : {Y}{BO}{mins:02d}:{secs:02d} {G}============', end='\r')
        time.sleep(1)
        total_second -= 1
        
def resetTimeSlow ():
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 5)
        print(f'          {DARK}Mencoba Menyesuaikan Pola..!!  {Y}{BO}{secs:02d}', end='\r')
        time.sleep(1)
        total_second -= 1
        
def resetTimes ():
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'             {DARK}Pantau Trend dulu..{Y}[Tunggu{Y}]  {Y}{BO}{secs:02d}', end='\r')
        time.sleep(1)
        total_second -= 1        
        
def gameissue ():
			
			data = {
			'typeid' : '1',
			'language' : '1'
			}
			session = requests.Session()
			a = session.post('https://www.55lottertttapi.com/api/webapi/GetGameIssue', data = data)
			b = json.loads(a.text)
			c = b.get('data')
			d = c.get('IssueNumber')
			with open('issuenumber.txt', 'w') as f:
				f.write(str(d))
				f.close()
				
def taruhanbesarikut ():
			data = {
			'typeid' : '1',
			'pageno' : '1',
			'language' : 'id'
			}
			session = requests.Session()
			a = session.post('https://www.55lottertttapi.com/api/webapi/GetNoaverageEmerdList', data = data)
			b = json.loads(a.text)
			c = b.get('data')
			d = c.get('gameslist')
			e = d[0].get('IssueNumber')
			ff = d[0].get('Number')
			with open("Num.txt", 'w') as g:
			 g.write(ff)
			 g.close()
			ee = open("Num.txt", 'r')
			f = ee.read()
			if f > '4':
			 print(f"{DARK}HASIL : {G}[{e}] {BO}WINNNN //{R}[{G}BESAR{R}] {Y}{f} ✅✅✅✅✅✅")
			 with open("winlose.txt",'a') as g:
			  g.write("BESAR WIN\n")
			  g.close()
			 rumusikut()
			elif f < '5':
			 print(f"{DARK}HASIL : {R}[{e}] {BO}LOSEEE //{Y}[{G}KECIL{Y}] {R}{f} ⛔⛔⛔⛔⛔⛔")
			 with open("winlose.txt",'a') as g:
			  g.write("BESAR LOSE\n")
			  g.close()
			  rumusikut()
			 

			
def auto_kecilikut ():
			gameissue()
			e = open("issuenumber.txt", 'r')
			f = e.read()
			g = ['0','2','1','3','4']
			m = ['4','0','3','2','0']
			j = ['🟢','🔴']
			v = ['TURUNKAN BET','HATI-HATI','GASS']
			p = ['40%','46%','51%','50%','54%','61%','63%','65%','78%','75%','89%','97%']
			h = random.SystemRandom()
			i = h.choice(g)
			l = h.choice(m)
			z = h.choice(v)
			u = h.choice(p)
			k = h.choice(j)
			print("▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️")
			print(f"{G}•P{R}[{Y}{f}{R}]{G}•{DARK}Prediksi{R}({Y}KECIL({i}/{l}/{k}){N}{BO}{R}){Y}•{DARK}{u} {G}•{Y}{z}")
			countdownTimer()
			time.sleep(0.5)
			taruhankecilikut()
			
			
def taruhankecilikut ():
			data = {
			'typeid' : '1',
			'pageno' : '1',
			'language' : 'id'
			}
			session = requests.Session()
			a = session.post('https://www.55lottertttapi.com/api/webapi/GetNoaverageEmerdList', data = data)
			b = json.loads(a.text)
			c = b.get('data')
			d = c.get('gameslist')
			e = d[0].get('IssueNumber')
			ff = d[0].get('Number')
			with open("Num.txt", 'w') as g:
			 g.write(ff)
			 g.close()
			ee = open("Num.txt", 'r')
			f = ee.read()
			if f < '5':
			 print(f"{DARK}HASIL : {G}[{e}] {BO}WINNNN //{R}[{G}KECIL{R}] {Y}{f} ✅✅✅✅✅✅")
			 with open("winlose.txt",'a') as g:
			  g.write("KECIL WIN\n")
			  g.close()
			 rumusikut()
			elif f > '4':
			 print(f"{DARK}HASIL : {R}[{e}] {BO}LOSEEE //{Y}[{G}BESAR{Y}] {R}{f} ⛔⛔⛔⛔⛔⛔")
			 with open("winlose.txt",'a') as g:
			  g.write("KECIL LOSE\n")
			  g.close()
			  
			  print ("")
			  print (DARK+"                CILAKA,,, MENDUGA ZIGZAG...!! ")
			  resetTimes()
			  time.sleep(0.5)
			  rumuslawan()
			 
			 
def halaman1 ():
      data = {
      'typeid' : '1',
      'pageno' : '1',
      'language' : 'id'
      }
      session = requests.Session()
      a = session.post('https://www.55lottertttapi.com/api/webapi/GetNoaverageEmerdList', data = data)
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('gameslist')
      e1 = d[0].get('Number')
      e5 = d[0].get('Number')
      e6 = d[0].get('IssueNumber')
      e10 = d[0].get('Number')
      with open("halaman1.txt", 'w') as f:
       f.write(str(e1))
       f.close()
			
def rumusikut ():
      halaman1()
      data = {
      'typeid' : '1',
      'pageno' : '144',
      'language' : 'id'
      }
      session = requests.Session()
      a = session.post('https://www.55lottertttapi.com/api/webapi/GetNoaverageEmerdList', data = data)
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('gameslist')
      e1 = d[0].get('Number')
      e5 = d[0].get('Number')
      e6 = d[0].get('IssueNumber')
      e10 = d[0].get('Number')
      with open("halaman144.txt", 'w') as f:
       f.write(str(e10))
       f.close()
      j = open("halaman144.txt").read()
      j1 = open("halaman1.txt").read()
      result = int(j1)+int(j)
      with open("result.txt",'w') as f:
       f.write(str(result))
       f.close()
      res = open("halaman1.txt").read()
      if res == '0':
       auto_kecilikut()
      elif res == '1':
       auto_kecilikut()
      elif res == '2':
       auto_kecilikut()
      elif res == '3':
       auto_kecilikut()
      elif res == '4':
       auto_kecilikut()
      elif res == '5':
       auto_besarikut()
      elif res == '6':
       auto_besarikut()
      elif res == '7':
       auto_besarikut()
      elif res == '8':
       auto_besarikut()
      elif res == '9':
       auto_besarikut()
      else:
       auto_kecilskip()
					  
 
def auto_besarikut ():
			gameissue()
			e = open("issuenumber.txt", 'r')
			f = e.read()
			g = ['5','8','7','9','6']
			m = ['9','5','8','6','7']
			j = ['🔴','🟢']
			v = ['HATI-HATI','GASS','TURUNKAN BET']
			p = ['44%','47%','53%','58%','56%','62%','65%','67%','69%','70%','72%','74%','76%','79%','82%','86%','87%','85%','96%','95%','98%','92%']
			h = random.SystemRandom()
			i = h.choice(g)
			l = h.choice(m)
			z = h.choice(v)
			u = h.choice(p)
			k = h.choice(j)
			print("▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️")
			print(f"{G}•P{R}[{Y}{f}{R}]{G}•{DARK}Prediksi{R}({Y}BESAR({i}/{l}/{k}){N}{BO}{R}){Y}•{DARK}{u} {G}•{Y}{z}")
			countdownTimer()
			time.sleep(0.5)
			taruhanbesarikut()
			
			
			
def auto_kecilikut ():
			gameissue()
			e = open("issuenumber.txt", 'r')
			f = e.read()
			g = ['0','1','3','2','4']
			m = ['1','0','3','4','2']
			j = ['🟢','🔴']
			v = ['TURUNKAN BET','HATI-HATI','GASS']
			p = ['40%','46%','51%','50%','54%','61%','63%','65%','78%','75%','89%','97%']
			h = random.SystemRandom()
			i = h.choice(g)
			l = h.choice(m)
			z = h.choice(v)
			u = h.choice(p)
			k = h.choice(j)
			print("▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️")
			print(f"{G}•P{R}[{Y}{f}{R}]{G}•{DARK}Prediksi{R}({Y}KECIL({i}/{l}/{k}){N}{BO}{R}){Y}•{DARK}{u} {G}•{Y}{z}")
			countdownTimer()
			time.sleep(0.5)
			taruhankecilikut()
        
def gameissue ():
			
			data = {
			'typeid' : '1',
			'language' : '1'
			}
			session = requests.Session()
			a = session.post('https://www.55lottertttapi.com/api/webapi/GetGameIssue', data = data)
			b = json.loads(a.text)
			c = b.get('data')
			d = c.get('IssueNumber')
			with open('issuenumber.txt', 'w') as f:
				f.write(str(d))
				f.close()
				
def taruhanbesarskip ():
			data = {
			'typeid' : '1',
			'pageno' : '1',
			'language' : 'id'
			}
			session = requests.Session()
			a = session.post('https://www.55lottertttapi.com/api/webapi/GetNoaverageEmerdList', data = data)
			b = json.loads(a.text)
			c = b.get('data')
			d = c.get('gameslist')
			e = d[0].get('IssueNumber')
			ff = d[0].get('Number')
			with open("Num.txt", 'w') as g:
			 g.write(ff)
			 g.close()
			ee = open("Num.txt", 'r')
			f = ee.read()
			if f > '4':
			 print(f"{DARK}HASIL : {DARK}[{e}] {BO}SKIPP //{R}[{G}SKIPP{R}] {Y}{f} ⚫⚫⚫⚫⚫⚫")
			 with open("winlose.txt",'a') as g:
			  g.write("BESAR WIN\n")
			  g.close()
			 rumusikut()
			elif f < '5':
			 print(f"{DARK}HASIL : {DARK}[{e}] {BO}SKIPP //{Y}[{G}SKIPPP{Y}] {R}{f} ⚫⚫⚫⚫⚫⚫")
			 with open("winlose.txt",'a') as g:
			  g.write("BESAR LOSE\n")
			  g.close()
			  rumusIkut()
				
				
			
def auto_kecilskip ():
			gameissue()
			e = open("issuenumber.txt", 'r')
			f = e.read()
			g = ['2','1','0','3','4']
			m = ['1','4','3','2','0']
			j = ['🔴','🟢']
			d = ['JANGAN BET','JANGAN BET']
			v = ['HATI-HATI','TURUNKAN BET','GASS']
			p = ['40%','46%','51%','53','50%','54%','61%','63%','65%','74%','78%','75%','89%''81%','82%','84%','87%','90%','93%','95%','97%']
			h = random.SystemRandom()
			i = h.choice(g)
			l = h.choice(m)
			z = h.choice(v)
			u = h.choice(p)
			k = h.choice(j)
			b = h.choice(d)
			print("▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️")
			print(f"{G}•P{R}[{Y}{f}{R}]{G}•{DARK}Prediksi{R}({Y}SKIP(---){N}{BO}{R}){Y}•{DARK}{u} {G}•{Y}{b}")
			countdownTimer()
			time.sleep(0.5)
			taruhankecilskip()			
			
def taruhankecilskip ():
			data = {
			'typeid' : '1',
			'pageno' : '1',
			'language' : 'id'
			}
			session = requests.Session()
			a = session.post('https://www.55lottertttapi.com/api/webapi/GetNoaverageEmerdList', data = data)
			b = json.loads(a.text)
			c = b.get('data')
			d = c.get('gameslist')
			e = d[0].get('IssueNumber')
			ff = d[0].get('Number')
			with open("Num.txt", 'w') as g:
			 g.write(ff)
			 g.close()
			ee = open("Num.txt", 'r')
			f = ee.read()
			if f < '5':
			 print(f"{DARK}HASIL : {DARK}[{e}] {BO}SKIPP //{R}[{G}SKIPP{R}] {Y}{f} ⚫⚫⚫⚫⚫⚫")
			 with open("winlose.txt",'a') as g:
			  g.write("KECIL WIN\n")
			  g.close()
			 rumusikut()
			elif f > '4':
			 print(f"{DARK}HASIL : {DARK}[{e}] {BO}SKIPP //{Y}[{G}SKIPP{Y}] {R}{f} ⚫⚫⚫⚫⚫⚫")
			 with open("winlose.txt",'a') as g:
			  g.write("KECIL LOSE\n")
			  g.close()
			  rumusikut()()

			
def rumuslawan ():
      halaman1()
      data = {
      'typeid' : '1',
      'pageno' : '9',
      'language' : 'id'
      }
      session = requests.Session()
      a = session.post('https://www.55lottertttapi.com/api/webapi/GetNoaverageEmerdList', data = data)
      b = json.loads(a.text)
      c = b.get('data')
      d = c.get('gameslist')
      e1 = d[0].get('Number')
      e5 = d[4].get('Number')
      e6 = d[9].get('IssueNumber')
      e10 = d[9].get('Number')
      with open("halaman144.txt", 'w') as f:
       f.write(str(e10))
       f.close()
      j = open("halaman144.txt").read()
      j1 = open("halaman1.txt").read()
      result = int(j1)+int(j)
      with open("result.txt",'w') as f:
       f.write(str(result))
       f.close()
      res = open("halaman1.txt").read()
      if res == '0':
       auto_besarikut()
      elif res == '1':
       auto_besarikut()
      elif res == '2':
       auto_besarikut()
      elif res == '3':
       auto_besarikut()
      elif res == '4':
       auto_besarikut()
      elif res == '5':
       auto_kecilikut()
      elif res == '6':
       auto_kecilikut()
      elif res == '7':
       auto_kecilikut()
      elif res == '8':
       auto_kecilikut()
      elif res == '9':
       auto_kecilikut()
      else:
       auto_kecilskip()


b = datetime.now()
c = b.day
f = b.hour
d = 5
e = 6
f = 7
g = 8
h = 1
if c == b:
	os.system("clear")
	os.system("rm 55fivev2.py")
	time.sleep
	exit(10)
else:
	os.system("clear")
	print(DARK+"▒█▀▀█ ▒█▀▀█ ▒█▀▀▀ ▒█▀▀▄ ▀█▀ ▒█░▄▀ ▒█▀▀▀█ ▀█▀\n▒█▄▄█ ▒█▄▄▀ ▒█▀▀▀ ▒█░▒█ ▒█░ ▒█▀▄░ ░▀▀▀▄▄ ▒█░\n▒█░░░ ▒█░▒█ ▒█▄▄▄ ▒█▄▄▀ ▄█▄ ▒█░▒█ ▒█▄▄▄█ ▄█▄ \n\n█▀▀ █▀▀ 　 ▒█▀▀▀ ▀█▀ ▒█░░▒█ ▒█▀▀▀\n▀▀▄ ▀▀▄ 　 ▒█▀▀▀ ▒█░ ░▒█▒█░ ▒█▀▀▀\n▄▄▀ ▄▄▀ 　 ▒█░░░ ▄█▄ ░░▀▄▀░ ▒█▄▄▄")
	print("")
	print("")
	print("▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️")
	print(G+"                  TIPS & TRICK BERMAIN AMAN")
	print("")
	print(CYAN+" 1. PANTAU DULU JANGAN LANGSUNG BET")
	print("")
	print(" 2. JIKA PREDIKSI BOT LOSE 3X, MAKA TUNDA BET 5 MENIT")
	print("")
	print(" 3. SAAT BERMAIN PERHATIKAN RASIO JUGA")
	print("")
	print(" 4. RELOAD BOT SAAT AWAL PANTAU SERING LOSE")
	print("")
	print("▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️   BOT V11.0▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️")
	print("")
	print("")
	halaman1()
	aa = open("halaman1.txt").read()
	if aa > '4':
	 rumusikut()
	elif aa < '5':
	 rumusikut()
	else:
	 rumusikut()
