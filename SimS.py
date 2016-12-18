'''
"SimS" just simple python code
to automatically use shodan search engine.
I wait your suggestions to improve this code ^_^
coded by SimiPrambos
contact > simi.prambos@gmail.com
'''


import sys
import time
import os, os.path
import commands
import subprocess

#color list
red = '\033[0;31;0m'
green = '\033[0;32;0m'
blue = '\033[0;34;0m'


def banner():
	print
	print ("			 ____  _            ____  ")
	time.sleep(0.1)
	print ("			/ ___|(_)_ __ ___  / ___| ")
	time.sleep(0.1)
	print ("			\___ \| | '_ ` _ \ \___ \ ")
	time.sleep(0.1)
	print ("			 ___) | | | | | | | ___) |")
	time.sleep(0.1)
	print ("			|____/|_|_| |_| |_||____/ ")
	time.sleep(0.1)
	print
	print ("		Automatically Shodan Scanners v0.5 Beta")
	print ("		  Contact : simi.prambos@gmail.com")
	print

def install():
	print "checking installations required .."
	time.sleep(1)
	path = '/usr/local/bin/shodan'
	if os.path.exists(path):
		time.sleep(1)
		print
		os.system('clear')
	else:
		print "shodan not installed"
		print "[+] Installing shodan .."
		os.system('easy_install shodan')
		time.sleep(2)
		print "[+] Updating shodan .."
		os.system('easy_install -U shodan')
		time.sleep(2)
		print "[+] Initializing shodan API .."
		os.system('shodan init vjXgfcSKJmEnRSAsMXjyXyazWrLqw4ed')
		time.sleep(2)
		print "[+] Installation Succes"
		time.sleep(1)
		print
		os.system('clear')
install()

def menu():
	print
	print ("1.What's my Ip")
	print ("2.Scanning Host")
	print ("3.Shodan search, sorter: ip, port, hostname")
	print ("0.Exit")

def pilih():
	print
	time.sleep(0.1)
	pilih = input("SimS> ")
	os.system('clear')
	if pilih == 1:
		myip()
	elif pilih == 2:
		host()
	elif pilih == 3:
		search()
	elif pilih == 0:
		print
		print "[+] Closing the program .."
		time.sleep(1)
		print
		os.system('clear')
		exit()
	elif pilih == ' ':
		os.system('clear')
		menu()
		pilih()
	else:
		print "Nothing in menu"
		time.sleep(1)
		os.system('clear')
		menu()
		pilih()


def myip():
	print
	print "Your Ip Address :"
	print
	get = os.system('shodan myip')
	


def search():
	print
	query = raw_input("Input your have query to searching : ")
	print ("Please type q to end")
	get = os.system('shodan search --fields ip_str,port,org,hostnames %s' %query)
	print get
	

def host():
	print
	hostname = raw_input("Input Host ip address : ")
	print ("Please type q to end")
	get = os.system('shodan host %s' %hostname)
	print get
 


while True:
	try:
		banner()
		menu()
		pilih()

	except KeyboardInterrupt:
		print "\nExiting..."
		time.sleep(1)
		os.system('clear')
		break
