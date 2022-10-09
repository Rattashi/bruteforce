R = '\033[31m'
G = '\033[32m' 
C = '\033[36m'
W = '\033[0m' 

import os, sys, time, threading, requests, json, csv, argparse
import subprocess as subp
from shutil import which

print(G + '[+]' + C + 'Paketler kontrol ediliyor...' + W)
pkgs = ['python3', 'php', 'git',]
inst = True
for pkg in pkgs:
	present = which(pkg)
	if present == None:
		print(R + '[-] ' + W + pkg + C + 'Paketler yüklü değil!')
		inst = False
	else:
		pass
if inst == False:
	exit()
else:
	pass

row = []
info = ''
result = ''
version = '1.7.44'

def ver_check():
	print(G + '[+]' + C + 'Brute Force güncellemeleri kontrol ediliyor....', end='')
	ver_url = 'https://raw.githubusercontent.com/Ratew/bruteforce/main/src/Version.txt'
	try:
		ver_rqst = requests.get(ver_url)
		ver_sc = ver_rqst.status_code
		if ver_sc == 200:
			github_ver = ver_rqst.text
			github_ver = github_ver.strip()

			if version == github_ver:
				print(C + '[' + G + 'Güncelleme yok' + C +']' + '\n')
				time.sleep(0.8)
			else:
				print(C + '[' + R + ' Mevcut : {} '.format(github_ver) + C + ']' + '\n')
				time.sleep(1.5)
		else:
			print(C + '[' + R + ' Durum : {} '.format(ver_sc) + C + ']' + '\n')
	except Exception as e:
		print('\n' + R + '[-]' + C + ' İstisna : ' + W + str(e))

try:
	ver_check()

except KeyboardInterrupt:
	print ('\n' + R + '[!]' + C + 'Klavye Kesintisi.' + W)
