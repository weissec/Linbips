#!/usr/bin/env python2

# GMSPUFL v0.1
# Get Me Some Potential Usernames From Linkedin
# W315 (C) 2019

from googlesearch import search
import argparse
import sys
from argparse import RawTextHelpFormatter

banner = """  ___  _  _  ____  ____  _  _  ____  __   
 / __)( \/ )/ ___)(  _ \/ )( \(  __)(  )  
| (_ \/ \/ ||___ \ ) __/) \/ ( ) _) / (___
 \___/\_)(_/(____/(__)  \____/(__)  \____/ v.0.1

Get Me Some Potential Usernames From Linkedin
"""

def getresults():
	print("[*] Scraping first {} google results..\n".format(numres))
	global results_list
	results_list = []
	for i in search(query,
			tld = 'com',   # The top level domain
		        lang = 'en',   # The language
		        num = 10,      # Number of results per page
		        start = 0,     # First result to retrieve
		        stop = numres, # Number of results to retrieve
		        pause = 2.0,   # Lapse between HTTP requests
		       ):

		if args.s == False:
			print(i)

		results_list.append(i)

	print("\n[*] All profiles retrieved")
		

# NameSurname
def output_type_one():
	print("[*] Saving usernames as: NameSurname\n")
	f = open(filename, 'w')
	ftwo = open("Others.txt", 'w')
	for line in results_list:
		name = str(line).split("/")
		if "-" in line:
			user = name[4].split("-")
			if args.s == False:
				print(user[0] + user[1])
			f.write(user[0] + user[1] + "\n")
		else:
			user = name[4]
			if args.s == False:
				print(user)
			ftwo.write(user + "\n")
	ftwo.close()
	f.close()

# Name.Surname
def output_type_two():
	print("[*] Saving usernames as: Name.Surname\n")
	f = open(filename, 'w')
	ftwo = open("Others.txt", 'w')
	for line in results_list:
		name = str(line).split("/")
		if "-" in line:
			user = name[4].split("-")
			if args.s == False:
				print(user[0] + "." + user[1])
			f.write(user[0] + "." + user[1] + "\n")
		else:
			user = name[4]
			if args.s == False:
				print(user)
			ftwo.write(user + "\n")
	ftwo.close()
	f.close()

# NSurname
def output_type_three():
	print("[*] Saving usernames as: NSurname\n")
	f = open(filename, 'w')
	ftwo = open("Others.txt", 'w')
	for line in results_list:
		name = str(line).split("/")
		if "-" in line:
			user = name[4].split("-")
			letters = user[0]
			if args.s == False:
				print(letters[0] + user[1])
			f.write(letters[0] + user[1] + "\n")
		else:
			user = name[4]
			if args.s == False:
				print(user)
			ftwo.write(user + "\n")
	ftwo.close()
	f.close()

# NameS
def output_type_four():
	print("[*] Saving usernames as: NameS\n")
	f = open(filename, 'w')
	ftwo = open("Others.txt", 'w')
	for line in results_list:
		name = str(line).split("/")
		if "-" in line:
			user = name[4].split("-")
			letters = user[1]
			if args.s == False:
				print(user[0] + letters[0])
			f.write(user[0] + letters[0] + "\n")
		else:
			user = name[4]
			if args.s == False:
				print(user)
			ftwo.write(user + "\n")
	ftwo.close()
	f.close()

# N.Surname
def output_type_five():
	print("[*] Saving usernames as: NameS\n")
	f = open(filename, 'w')
	ftwo = open("Others.txt", 'w')
	for line in results_list:
		name = str(line).split("/")
		if "-" in line:
			user = name[4].split("-")
			letters = user[0]
			if args.s == False:
				print(letters[0] + "." + user[1])
			f.write(letters[0] + "." + user[1] + "\n")
		else:
			user = name[4]
			if args.s == False:
				print(user)
			ftwo.write(user + "\n")
	ftwo.close()
	f.close()

# Menu

test = '''
Given a target company name, retrieve a list of potential
usernames from Linkedin using a google dork.

Output Format Types: 
1 = NameSurname
2 = Name.Surname
3 = NSurname
4 = NameS
5 = N.Surname

Example: gmspufl.py -c Ecorp -t 2 -o Usernames.txt -n 100
'''

if __name__ == "__main__":

	print banner.decode('UTF-8')

	parser = argparse.ArgumentParser(description=test, formatter_class=RawTextHelpFormatter)
	parser.add_argument('-c', dest='company', required=True, help='The target company name')
	parser.add_argument('-t', dest='type', default='1', help='Type of output format')
	parser.add_argument('-o', dest='filen', default='Usernames.txt', help='Output file name')
	parser.add_argument('-n', dest='number', default=50, help='Number of results (default: 50)')
	parser.add_argument('-s', action='store_true', help='Silent mode - do not print results in terminal')

	try:
    		args = parser.parse_args()
	except:
    		sys.exit(0)

	query = "site:linkedin.com/in '%s'" % (str(args.company))
	numres = int(args.number)
	filename = args.filen

	getresults()

	if args.type == "1":
		output_type_one()
	elif args.type == "2":
		output_type_two()
	elif args.type == "3":
		output_type_three()
	elif args.type == "4":
		output_type_four()
	elif args.type == "5":
		output_type_five()
	
	print("\n[*] List of potential usernames saved in file: {}".format(filename))
	print("[*] A list of usernames that do not follow the required pattern has been saved in: Others.txt")

