#!/usr/bin/env python3

# Linbips v1.0
# Retrieve name, role and URL of employees from linkedin (passive search)
# W315 (C) 2021

from search_engine_parser import GoogleSearch
import argparse
import sys
from argparse import RawTextHelpFormatter
import os.path


banner = '''\033[92m
   __   _____  _____  _______  ____
  / /  /  _/ |/ / _ )/  _/ _ \/ __/
 / /___/ //    / _ < / // ___/\ \  
/____/___/_/|_/____/___/_/  /___/                                
Linkedin Basic Info Passive Scraper  \033[0m                                                                
'''

# Functions
def compmode(query):

	pagec = 1
	
	while pagec<= numr:

		search_args = (query, pagec)
		gsearch = GoogleSearch()
		gresults = gsearch.search(*search_args)
		urls = gresults['links']
		titles = gresults['titles']

		i=0
		for line in titles:
			if "-" in line:
					
				details = str(line).split(" - ")
				link = urls[i]
				dinurl = link.split("=")
				
				print(details[0] + ", " + details[1])
				
				f = open(outfile, 'a')
				f.write("\n" + details[0] + "," + details[1] + "," + dinurl[1])
				f.close()
				
				i+=1

		pagec += 1
		
def compmodeusernames(query):

	pagec = 1
	
	while pagec<= numr:

		search_args = (query, pagec)
		gsearch = GoogleSearch()
		gresults = gsearch.search(*search_args)
		urls = gresults['links']
		titles = gresults['titles']

		i=0
		for line in titles:
			if "-" in line:
					
				details = str(line).split(" - ")
				link = urls[i]
				dinurl = link.split("=")
				
				# usernames
				fullname = str(details[0]).split()
				name = fullname[0]
				surname = fullname[1]
				# 1 = NameSurname
				userone = name + surname
				# 2 = Name.Surname
				usertwo = name + "." + surname
				# 3 = NSurname
				userthree = name[0] + surname
				# 4 = NameS
				userfour = name + surname[0]
				# 5 = N.Surname
				userfive = name[0] + "." + surname
				
				print(details[0] + ", " + details[1])
				
				f = open(outfile, 'a')
				f.write("\n" + details[0] + "," + details[1] + "," + dinurl[1] + "," + userone + "," + usertwo + "," + userthree + "," + userfour + "," + userfive)
				f.close()
				
				i+=1

		pagec += 1


def mailmode(mailfile):

	with open(mailfile) as f:
	
		lines = f.readlines()
		for line in lines:
		
			query = "site:linkedin.com/in '%s'" % (str(line))
			search_args = (query, 1)
			gsearch = GoogleSearch()
			gresults = gsearch.search(*search_args)
			urls = gresults['links']
			titles = gresults['titles']
			
			i=0
			for title in titles:
				if "-" in title:
						
					details = str(title).split(" - ")
					link = urls[i]
					dinurl = link.split("=")
					
					print(details[0] + ", " + details[1])
					
					f = open(outfile, 'a')
					f.write("\n" + details[0] + "," + details[1] + "," + line.rstrip() + "," + dinurl[1])
					f.close()
					
					i+=1
					
def mailmodeusernames(mailfile):

	with open(mailfile) as f:
	
		lines = f.readlines()
		for line in lines:
		
			query = "site:linkedin.com/in '%s'" % (str(line))
			search_args = (query, 1)
			gsearch = GoogleSearch()
			gresults = gsearch.search(*search_args)
			urls = gresults['links']
			titles = gresults['titles']
			
			i=0
			for title in titles:
				if "-" in title:
						
					details = str(title).split(" - ")
					link = urls[i]
					dinurl = link.split("=")
					
					# usernames
					fullname = str(details[0]).split()
					name = fullname[0]
					surname = fullname[1]
					# 1 = NameSurname
					userone = name + surname
					# 2 = Name.Surname
					usertwo = name + "." + surname
					# 3 = NSurname
					userthree = name[0] + surname
					# 4 = NameS
					userfour = name + surname[0]
					# 5 = N.Surname
					userfive = name[0] + "." + surname
					
					print(details[0] + ", " + details[1])
					
					f = open(outfile, 'a')
					f.write("\n" + details[0] + "," + details[1] + "," + line.rstrip() + "," + dinurl[1] + "," + userone + "," + usertwo + "," + userthree + "," + userfour + "," + userfive)
					f.close()
					
					i+=1

# Menu

test = '''
Given a target company name, retrieves a list of employees and their role from Linkedin.
If the -u option is used, a list of potential AD usernames in different formats is also generated.
This scraper can also be run by providing a list of email addresses.

Note: this tool is completely passive and does not require a Linkedin account.
'''

if __name__ == "__main__":

	print(banner)

	parser = argparse.ArgumentParser(description=test, formatter_class=RawTextHelpFormatter)
	parser.add_argument('-c', dest='company', default='', help='The company name')
	parser.add_argument('-e', dest='emails', default='', help='File including a list of emails')
	parser.add_argument('-p', dest='pages', default=1, help='Number of pages, default=1')
	parser.add_argument('-o', dest='outfile', default='linbips-output.csv', help='Output file name (CSV). Default: linbips-output.csv')
	parser.add_argument('-u', action='store_true', help='Also generate a list of potential usernames')

	try:
		args = parser.parse_args()
	except:
		sys.exit(0)
		
	outfile = args.outfile

	# Check if the company name has been provided 
	if args.company == "":
	
		# if no company name is provided check if a list of email has been provided
		if args.emails == "":
			print("Error: you need to provide a list of email addresses or the name of the organistation!")
			sys.exit(0)
		
		mailfile = str(args.emails)
		
		if os.path.isfile(mailfile):
			mailnum = sum(1 for entry in open(mailfile))
			print("Emails found: %s" % mailnum)
		else:
			print ("Error: input file not found.")
			sys.exit(0)
		
		print("\033[92mEmail Mode:\033[0m looking for results related to the emails listed in: %s \n" % mailfile)
		# Call function
		
		if args.u == True:
			mailmode(mailfile)
		else:
			mailmodeusernames(mailfile)
			
	else:
	
		# check if a list of email has been provided as well
		if args.emails != "":
			print("Error: you can't search using the company name and a list of email at the same time!")
			sys.exit(0)
		
		print("\033[92mCompany Mode:\033[0m looking for results related to the following organisation: %s \n" % str(args.company))
		query = "site:linkedin.com/in '%s'" % str(args.company)
		numr = int(args.pages)
		
		if args.u == True:
			compmodeusernames(query)
		else:
			compmode(query)
			

	print("\n\033[92mDONE:\033[0m Finished scraping results.")
	employees = sum(1 for line in open(outfile))
	print("Number of employees discovered: %s" % str(employees))
	print("Results saved as CSV in: %s" % outfile)
	
	sys.exit(0)
