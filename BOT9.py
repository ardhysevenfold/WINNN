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
refresh = "refresh"
while(refresh == "refresh"):
    print("                 PANTAU BOT SEBELUM BERMAIN YA")
    refresh = input("LANJUTKAN: Y")
    
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

def auto_besarikut ():
			gameissue()
			e = open("issuenumber.txt", 'r')
			f = e.read()
			g = ['7','9','6','8','5']
			m = ['9','8','6','5','7']
			v = ['HATI-HATI','GASS','GASS','TURUNKAN BET','GASS']
			p = ['44%','47%','53%','58%','56%','67%','69%','74%','79%','82%','87%','85%','96%','92%']
			h = random.SystemRandom()
			i = h.choice(g)
			l = h.choice(m)
			z = h.choice(v)
			u = h.choice(p)
			print("▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️")
			print(f"{G}•P{R}[{Y}{f}{R}]{G}•{DARK}Prediksi{R}({Y}{UNDER}BESAR({i}/{l}){N}{BO}{R}){Y}•⚕️ :{DARK}{u} {G}•{Y}{z}")
			countdownTimer()
			time.sleep(0.5)
			taruhanbesarikut()
			
			
			
def auto_kecilikut ():
			gameissue()
			e = open("issuenumber.txt", 'r')
			f = e.read()
			g = ['3','1','2','0','4']
			m = ['1','4','3','2','0']
			v = ['TURUNKAN BET','HATI-HATI','GASS','BOMB','GASS']
			p = ['40%','46%','51%','50%','54%','61%','63%','65%','78%','75%','89%','97%']
			h = random.SystemRandom()
			i = h.choice(g)
			l = h.choice(m)
			z = h.choice(v)
			u = h.choice(p)
			print("▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️")
			print(f"{G}•P{R}[{Y}{f}{R}]{G}•{DARK}Prediksi{R}({Y}{UNDER}KECIL({i}/{l}){N}{BO}{R}){Y}•⚕️ :{DARK}{u} {G}•{Y}{z}")
			countdownTimer()
			time.sleep(0.5)
			taruhankecilikut()
			
			
def countdownTimer ():
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'        {G}============ {DARK}Sisa Waktu : {Y}{BO}{mins:02d}:{secs:02d} {G}============', end='\r')
        time.sleep(1)
        total_second -= 1
        
def resetTime ():
    aaa = datetime.now()
    bbb = aaa.strftime("%S")
    total_second = 60-int(bbb)
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'          {DARK}Mencocokkan rumus [mohon menunggu] : {Y}{BO}{mins:02d}:{secs:02d}', end='\r')
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
			  
			  print ("")
			  print (CYAN+"             SITUASI TIDAK BAGUS..!! ")
			  resetTime()
			  time.sleep(0.5)
			  rumus33()
			 
def auto_besarlawan ():
			gameissue()
			e = open("issuenumber.txt", 'r')
			f = e.read()
			g = ['8','6','7','5','9']
			m = ['8','5','7','9','6']
			v = ['GASS','GASS','TURUNKAN BET','HATI-HATI','GASS']
			p = ['48%','53%','58%','66%','79%','83%','85%','92%','95%']
			h = random.SystemRandom()
			i = h.choice(g)
			l = h.choice(m)
			z = h.choice(v)
			u = h.choice(p)
			print("▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️")
			print(f"{G}•P{R}[{Y}{f}{R}]{G}•{DARK}Prediksi{R}({Y}{UNDER}BESAR({i}/{l}){N}{BO}{R}){Y}•⚕️ :{DARK}{u} {G}•{Y}{z}")
			countdownTimer()
			time.sleep(0.5)
			taruhanbesarlawan()		

			
def auto_kecilikut ():
			gameissue()
			e = open("issuenumber.txt", 'r')
			f = e.read()
			g = ['0','2','1','3','4']
			m = ['4','0','3','2','0']
			v = ['TURUNKAN BET','HATI-HATI','GASS','GASS','GASS']
			p = ['40%','46%','51%','50%','54%','61%','63%','65%','78%','75%','89%','97%']
			h = random.SystemRandom()
			i = h.choice(g)
			l = h.choice(m)
			z = h.choice(v)
			u = h.choice(p)
			print("▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️")
			print(f"{G}•P{R}[{Y}{f}{R}]{G}•{DARK}Prediksi{R}({Y}{UNDER}KECIL({i}/{l}){N}{BO}{R}){Y}•⚕️ :{DARK}{u} {G}•{Y}{z}")
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
			if f > '4':
			 print(f"{DARK}HASIL : {R}[{e}] {BO}LOSEEE //{Y}[{G}BESAR{Y}] {R}{f} ⛔⛔⛔⛔⛔⛔")
			 with open("winlose.txt",'a') as g:
			  g.write("KECIL LOSE\n")
			  g.close()
			 rumus33()
			elif f < '5':
			 print(f"{DARK}HASIL : {G}[{e}] {BO}WINNNN //{R}[{G}KECIL{R}] {Y}{f} ✅✅✅✅✅✅")
			 with open("winlose.txt",'a') as g:
			  g.write("KECIL WIN\n")
			  g.close()
			 rumusikut()
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
      e5 = d[4].get('Number')
      e6 = d[9].get('IssueNumber')
      e10 = d[9].get('Number')
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
      res = open("result.txt").read()
      if res == '0':
       auto_kecilikut()
      elif res == '1':
       auto_kecillawan()
      elif res == '2':
       auto_besarlawan()
      elif res == '3':
       auto_kecilikut()
      elif res == '4':
       auto_kecillawan()
      elif res == '5':
       auto_besarlawan()
      elif res == '6':
       auto_kecilikut()
      elif res == '7':
       auto_kecillawan()
      elif res == '8':
       auto_besarlawan()
      elif res == '9':
       auto_kecilikut()
      elif res == '10':
       auto_kecillawan()
      elif res == '11':
       auto_besarlawan()
      elif res == '12':
       auto_kecilikut()
      elif res == '13':
       auto_kecillawan()
      elif res == '14':
       auto_besarlawan()
      elif res == '15':
       auto_kecilikut()
      elif res == '16':
       auto_kecillawan()
      elif res == '17':
       auto_besarlawan()
      elif res == '18':
       auto_kecilikut()
      elif res == '19':
       auto_kecillawan()
      elif res == '20':
       auto_besarlawan()
      elif res == '21':
       auto_kecilikut()
      elif res == '22':
       auto_kecillawan()
      elif res == '23':
       auto_besarlawan()
      elif res == '24':
       auto_kecilikut()
      elif res == '25':
       auto_kecillawan()
      elif res == '26':
       auto_besarlawan()
      else:
       auto_kecillawan()
       
def auto_besarlawan ():
			gameissue()
			e = open("issuenumber.txt", 'r')
			f = e.read()
			g = ['5','9','7','8','6']
			m = ['8','6','5','9','7']
			v = ['GASS','GASS','HATI-HATI','TURUNKAN BET','GASS']
			p = ['48%','53%','58%','66%','79%','83%','85%','92%','95%']
			h = random.SystemRandom()
			i = h.choice(g)
			l = h.choice(m)
			z = h.choice(v)
			u = h.choice(p)
			print("▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️")
			print(f"{G}•P{R}[{Y}{f}{R}]{G}•{DARK}Prediksi{R}({Y}{UNDER}BESAR({i}/{l}){N}{BO}{R}){Y}•⚕️ :{DARK}{u} {G}•{Y}{z}")
			countdownTimer()
			time.sleep(0.5)
			taruhanbesarlawan()
			
			
def auto_kecillawan ():
			gameissue()
			e = open("issuenumber.txt", 'r')
			f = e.read()
			g = ['3','1','2','0','4']
			m = ['1','2','4','0','3']
			v = ['GASS','HATI-HATI','GASS','GASS','TURUNKAN BET']
			p = ['46%','53%','59%','66%','75%','77%','83%','86%','93%','95%']
			h = random.SystemRandom()
			i = h.choice(g)
			l = h.choice(m)
			z = h.choice(v)
			u = h.choice(p)
			print("▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️")
			print(f"{G}•P{R}[{Y}{f}{R}]{G}•{DARK}Prediksi{R}({Y}{UNDER}KECIL({i}/{l}){N}{BO}{R}){Y}•⚕️ :{DARK}{u} {G}•{Y}{z}")
			countdownTimer()
			time.sleep(0.5)
			taruhankecillawan()
				
def taruhanbesarlawan ():
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
			 rumuslawan()
			elif f < '5':
			 print(f"{DARK}HASIL : {R}[{e}] {BO}LOSEEE //{Y}[{G}KECIL{Y}] {R}{f} ⛔⛔⛔⛔⛔⛔")
			 with open("winlose.txt",'a') as g:
			  g.write("BESAR LOSE\n")
			  g.close()
			 
			  print ("")
			  print (CYAN+"             SITUASI TIDAK BAGUS..!! ")
			  resetTime()
			  time.sleep(0.5)
			  rumus33()
			 
			  
def auto_kecillawan ():
			gameissue()
			e = open("issuenumber.txt", 'r')
			f = e.read()
			g = ['2','1','0','3','4']
			m = ['1','3','4','0','1']
			v = ['GASS','TURUNKAN BET','GASS','HATI-HATI','HATI-HATI']
			p = ['46%','53%','59%','66%','75%','77%','83%','86%','93%','95%']
			h = random.SystemRandom()
			i = h.choice(g)
			l = h.choice(m)
			z = h.choice(v)
			u = h.choice(p)
			print("▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️")
			print(f"{G}•P{R}[{Y}{f}{R}]{G}•{DARK}Prediksi{R}({Y}{UNDER}KECIL({i}/{l}){N}{BO}{R}){Y}•⚕️ :{DARK}{u} {G}•{Y}{z}")
			countdownTimer()
			time.sleep(0.5)
			taruhankecillawan()
					  
			  
def auto_besarikut ():
			gameissue()
			e = open("issuenumber.txt", 'r')
			f = e.read()
			g = ['5','8','7','6','9']
			m = ['9','8','6','5','7']
			v = ['TURUNKAN BET','GAS','GASS','HATI-HATI','GASS']
			p = ['44%','47%','53%','58%','56%','67%','69%','74%','79%','82%','87%','85%','96%','92%']
			h = random.SystemRandom()
			i = h.choice(g)
			l = h.choice(m)
			z = h.choice(v)
			u = h.choice(p)
			print("▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️")
			print(f"{G}•P{R}[{Y}{f}{R}]{G}•{DARK}Prediksi{R}({Y}{UNDER}BESAR({i}/{l}){N}{BO}{R}){Y}•⚕️ :{DARK}{u} {G}•{Y}{z}")
			countdownTimer()
			time.sleep(0.5)
			taruhanbesarikut()
			
			
def taruhankecillawan ():
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
			 print(f"{DARK}HASIL : {R}[{e}] {BO}LOSEEE //{Y}[{G}BESAR{Y}] {R}{f} ⛔⛔⛔⛔⛔⛔")
			 with open("winlose.txt",'a') as g:
			  g.write("KECIL LOSE\n")
			  g.close()
			 rumusikut()
			elif f < '5':
			 print(f"{DARK}HASIL : {G}[{e}] {BO}WINNNN //{R}[{G}KECIL{R}] {Y}{f} ✅✅✅✅✅✅")
			 with open("winlose.txt",'a') as g:
			  g.write("KECIL WIN\n")
			  g.close()
			 rumuslawan()
			
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
      res = open("result.txt").read()
      if res == '0':
       auto_besarlawan()
      elif res == '1':
       auto_besarikut()
      elif res == '2':
       auto_kecillawan()
      elif res == '3':
       auto_besarlawan()
      elif res == '4':
       auto_besarikut()
      elif res == '5':
       auto_kecillawan()
      elif res == '6':
       auto_besarlawan()
      elif res == '7':
       auto_besarikut()
      elif res == '8':
       auto_kecillawan()
      elif res == '9':
       auto_besarlawan()
      elif res == '10':
       auto_kecillawan()
      elif res == '11':
       auto_kecillawan()
      elif res == '12':
       auto_besarlawan()
      elif res == '13':
       auto_besarikut()
      elif res == '14':
       auto_kecillawan()
      elif res == '15':
       auto_besarlawan()
      elif res == '16':
       auto_besarikut()
      elif res == '17':
       auto_besarlawan()
      elif res == '18':
       auto_besarlawan()
      elif res == '19':
       auto_besarikut()
      elif res == '20':
       auto_kecillawan()
      elif res == '21':
       auto_kecillawan()
      elif res == '22':
       auto_kecillawan()
      elif res == '23':
       auto_kecillawan()
      elif res == '24':
       auto_kecillawan()
      elif res == '25':
       auto_besarikut()
      elif res == '26':
       auto_besarikut()
      else:
       auto_kecillawan()
 
def auto_besarikut ():
			gameissue()
			e = open("issuenumber.txt", 'r')
			f = e.read()
			g = ['5','8','7','9','6']
			m = ['9','5','8','6','7']
			v = ['HATI-HATI','GASS','GASS','TURUNKAN BET','GASS']
			p = ['44%','47%','53%','58%','56%','67%','69%','74%','79%','82%','87%','85%','96%','92%']
			h = random.SystemRandom()
			i = h.choice(g)
			l = h.choice(m)
			z = h.choice(v)
			u = h.choice(p)
			print("▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️")
			print(f"{G}•P{R}[{Y}{f}{R}]{G}•{DARK}Prediksi{R}({Y}{UNDER}BESAR({i}/{l}){N}{BO}{R}){Y}•⚕️ :{DARK}{u} {G}•{Y}{z}")
			countdownTimer()
			time.sleep(0.5)
			taruhanbesarikut()
			
			
			
def auto_kecilikut ():
			gameissue()
			e = open("issuenumber.txt", 'r')
			f = e.read()
			g = ['0','1','3','2','4']
			m = ['1','0','3','4','2']
			v = ['TURUNKAN BET','HATI-HATI','GASS','GASS','GASS']
			p = ['40%','46%','51%','50%','54%','61%','63%','65%','78%','75%','89%','97%']
			h = random.SystemRandom()
			i = h.choice(g)
			l = h.choice(m)
			z = h.choice(v)
			u = h.choice(p)
			print("▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️")
			print(f"{G}•P{R}[{Y}{f}{R}]{G}•{DARK}Prediksi{R}({Y}{UNDER}KECIL({i}/{l}){N}{BO}{R}){Y}•⚕️ :{DARK}{u} {G}•{Y}{z}")
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
			  
			  print ("")
			  print (CYAN+"             SITUASI TIDAK BAGUS..!! ")
			  resetTime()
			  time.sleep(0.5)
			  rumus33()
			  
			 
def auto_besarlawan ():
			gameissue()
			e = open("issuenumber.txt", 'r')
			f = e.read()
			g = ['8','6','7','5','9']
			m = ['8','5','6','7','9']
			v = ['GASS','GASS','HATI-HATI','TURUNKAN BET','GASS']
			p = ['48%','53%','58%','66%','79%','83%','85%','92%','95%']
			h = random.SystemRandom()
			i = h.choice(g)
			l = h.choice(m)
			z = h.choice(v)
			u = h.choice(p)
			print("▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️")
			print(f"{G}•P{R}[{Y}{f}{R}]{G}•{DARK}Prediksi{R}({Y}{UNDER}BESAR({i}/{l}){N}{BO}{R}){Y}•⚕️ :{DARK}{u} {G}•{Y}{z}")
			countdownTimer()
			time.sleep(0.5)
			taruhanbesarlawan()		

			
def auto_kecilikut ():
			gameissue()
			e = open("issuenumber.txt", 'r')
			f = e.read()
			g = ['2','1','0','3','4']
			m = ['1','4','3','2','0']
			v = ['HATI-HATI','TURUNKAN BET','GASS','GASS','GASS']
			p = ['40%','46%','51%','50%','54%','61%','63%','65%','78%','75%','89%','97%']
			h = random.SystemRandom()
			i = h.choice(g)
			l = h.choice(m)
			z = h.choice(v)
			u = h.choice(p)
			print("▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️")
			print(f"{G}•P{R}[{Y}{f}{R}]{G}•{DARK}Prediksi{R}({Y}{UNDER}KECIL({i}/{l}){N}{BO}{R}){Y}•⚕️ :{DARK}{u} {G}•{Y}{z}")
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
			if f > '4':
			 print(f"{DARK}HASIL : {R}[{e}] {BO}LOSEEE //{Y}[{G}BESAR{Y}] {R}{f} ⛔⛔⛔⛔⛔⛔")
			 with open("winlose.txt",'a') as g:
			  g.write("KECIL LOSE\n")
			  g.close()
			 rumus33()
			elif f < '5':
			 print(f"{DARK}HASIL : {G}[{e}] {BO}WINNNN //{R}[{G}KECIL{R}] {Y}{f} ✅✅✅✅✅✅")
			 with open("winlose.txt",'a') as g:
			  g.write("KECIL WIN\n")
			  g.close()
			 rumusikut()
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
      e5 = d[4].get('Number')
      e6 = d[9].get('IssueNumber')
      e10 = d[9].get('Number')
      with open("halaman1.txt", 'w') as f:
       f.write(str(e1))
       f.close()
			
def rumus33 ():
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
      res = open("result.txt").read()
      if res == '0':
       auto_besarikut()
      elif res == '1':
       auto_besarikut()
      elif res == '2':
       auto_kecilikut()
      elif res == '3':
       auto_kecilikut()
      elif res == '4':
       auto_besarikut()
      elif res == '5':
       auto_besarikut()
      elif res == '6':
       auto_kecilikut()
      elif res == '7':
       auto_kecilikut()
      elif res == '8':
       auto_besarikut()
      elif res == '9':
       auto_besarikut()
      elif res == '10':
       auto_kecilikut()
      elif res == '11':
       auto_kecilikut()
      elif res == '12':
       auto_besarikut()
      elif res == '13':
       auto_besarikut()
      elif res == '14':
       auto_kecilikut()
      elif res == '15':
       auto_kecilikut()
      elif res == '16':
       auto_besarikut()
      elif res == '17':
       auto_besarikut()
      elif res == '18':
       auto_kecilikut()
      elif res == '19':
       auto_kecilikut()
      elif res == '20':
       auto_besarikut()
      elif res == '21':
       auto_besarikut()
      elif res == '22':
       auto_kecilikut()
      elif res == '23':
       auto_kecilikut()
      elif res == '24':
       auto_besarikut()
      elif res == '25':
       auto_besarikut()
      elif res == '26':
       auto_kecilikut()
      else:
       auto_kecilikut()


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
	print(" 3. SAAT BERMAIN PERHATIKAN RASIO")
	print("")
	print(" 4. RELOAD BOT SAAT SERING LOSE BANYAK")
	print("")
	print("▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️   BOT V9.0 ▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️")
	print("")
	print("")
	halaman1()
	aa = open("halaman1.txt").read()
	if aa > '3':
	 rumusikut()
	elif aa < '4':
	 rumuslawan()
	else:
	 rumus33()
