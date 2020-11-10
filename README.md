# USERSEARCHEDIN.py
     
*** Update Oct 2020 - upgraded to Python3


## Description:
Python script that uses Google dork to get a list of potential usernames given a target Company name.

Why?
------------------------
A list of usernames generated using OSINT is mostly useful for Password Spray attacks.
For example, in an Active Directory environment the generated list can be fired against a Domain Controller using the smb_login module in metasploit, using a weak password like "Pasword1".

How to install:
-------------------------
Downoad the files using git:
`git clone https://github.com/weissec/usersearchedin.git`

Use Pip to install the required packages:
`pip install -r requirements.txt`

How to use:
------------------------
usage: `./usersearchedin.py [-h] -c COMPANY [-t TYPE] [-o FILEN] [-n NUMBER] [-s]`

Output Format Types: 
* 1 = NameSurname
* 2 = Name.Surname
* 3 = NSurname
* 4 = NameS
* 5 = N.Surname

Example: `./usersearchedin.py -c Ecorp -t 2 -o Usernames.txt -n 100`

Required arguments:
 * -c COMPANY  The target company name

Optional arguments:
 * -h, --help  show this help message and exit
 * -t TYPE     Type of output format
 * -o FILEN    Output file name
 * -n NUMBER   Number of results (default: 50)
 * -s          Silent mode - do not print results in terminal

