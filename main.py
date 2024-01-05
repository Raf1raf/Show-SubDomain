#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
------------------------------------------------------------------------------
	CTFR - 04.03.18.02.10.00 - شيلا أ. بيرتا (UnaPibaGeek)
------------------------------------------------------------------------------
"""
# طريقه التشغيل 
 # python3 min.py -d example.com -o output.txt
import re
import requests

version = 1.2


def parse_args():
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('-d', '--domain', type=str, required=True, help="نطاق الهدف.")
	parser.add_argument('-o', '--output', type=str, help="ملف الإخراج.")
	return parser.parse_args()

def banner():
	global version
	b = '''
  _____       ______       ____        _____ _______ ______ _____  
 |  __ \     |  ____|     / /\ \      / ____|__   __|  ____|  __ \ 
 | |__) |__ _| |__       / /  \ \    | |       | |  | |__  | |__) |
 |  _  // _` |  __|     / /    \ \   | |       | |  |  __| |  _  / 
 | | \ \ (_| | |       / /      \ \  | |____   | |  | |    | | \ \ 
 |_|  \_\__,_|_|      /_/        \_\  \_____|  |_|  |_|    |_|  \_\
                                                                   
                                                                   
	
     Release {v} - Hey, don't miss it AXFR! edit by:RaF
     https://github.com/Raf1raf
     Produced by Sheila A. Burt (UnaPibaGeek)
	'''.format(v=version)
	print(b)
	
def clear_url(target):
	return re.sub('.*www\.','',target,1).split('/')[0].strip()

def save_subdomains(subdomain,output_file):
	with open(output_file,"a") as f:
		f.write(subdomain + '\n')
		f.close()

def main():
	banner()
	args = parse_args()

	subdomains = []
	target = clear_url(args.domain)
	output = args.output

	req = requests.get("https://crt.sh/?q=%.{d}&output=json".format(d=target))

	if req.status_code != 200:
		print("[X] Information is not available! (╯︵╰,) ") 
		exit(1)

	for (key,value) in enumerate(req.json()):
		subdomains.append(value['name_value'])

	
	print("\n[!] ---- The target: {d} ---- [!] \n".format(d=target))

	subdomains = sorted(set(subdomains))

	for subdomain in subdomains:
		print("[-]  {s}".format(s=subdomain))
		if output is not None:
			save_subdomains(subdomain,output)

	print("\n\n[!]Done. Happy day! ;) (◉‿◉) . ")


main()
