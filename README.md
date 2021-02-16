# Linbips.py
     
## Description:
This python script can be used to discover a list of employees and their role in a given organisation.
The script can also be used to scrape a list of potential usernames in different formats given a target Company name (-u option).

Why?
------------------------
Retrieving a list of employees and their role in an organistation might be useful for Red Team engagements and mostly phishing attacks.
Alternatively a list of potential usernames is mostly useful for Password Spray attacks.
For example, in an Active Directory environment the generated list can be fired against a Domain Controller using the smb_login module in metasploit, using a weak password like "Pasword1".

How to install:
-------------------------
Download the files using git:
`git clone https://github.com/weissec/linbips.git`

Use Pip to install the required packages:
`pip install -r requirements.txt`

How to use / Modes:
------------------------
Company Mode: `./linbips.py -c COMPANY [-o OUTPUT.csv] [-n NUMBER]`  
Email Mode: `./linbips.py -e EMAILS.txt [-o OUTPUT.csv]`  
Usernames Mode: `./linbips.py -u -c COMPANY [-o OUTPUT.csv]`

Username Output Format Types: 
* 1 = NameSurname
* 2 = Name.Surname
* 3 = NSurname
* 4 = NameS
* 5 = N.Surname

Required arguments (one of the two):
 * -c COMPANY  The target company name
 * -e EMAILS.TXT  The file containing a list of emails

Optional arguments:
 *  -h, --help  show this help message and exit
 *  -p PAGES    Number of pages, default=1
 *  -o OUTFILE  Output file name (CSV). Default: linbips-output.csv
 *  -u          Also generate a list of potential usernames

Output Format:
------------------------
Name Surname | Role | Linkedin URL | Email | NameSurname | Name.Surname | NSurname | NameS | N.Surname  
