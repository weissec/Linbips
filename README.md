# GMSPUFL
## Get Me Some Potential Usernames From Linkedin
Python script that uses Google dork to get a list of potential usernames given a target Company name.

How to install:
-------------------------
Downoad the files using git:
`git clone https://github.com/weissec/GMSPUFL.git`

Use Pip to install the required packages:
`pip install -r requirements.txt`

How to use:
------------------------
usage: `gmspufl.py [-h] -c COMPANY [-t TYPE] [-o FILEN] [-n NUMBER] [-s]`

Given a target company name, retrieve a list of potential
usernames from Linkedin using a google dork.

Output Format Types: 
* 1 = NameSurname
* 2 = Name.Surname
* 3 = NSurname
* 4 = NameS
* 5 = N.Surname

Example: `gmspufl.py -c Ecorp -t 2 -o Usernames.txt -n 100`

Optional arguments:
 * -h, --help  show this help message and exit
 * -c COMPANY  The target company name
 * -t TYPE     Type of output format
 * -o FILEN    Output file name
 * -n NUMBER   Number of results (default: 50)
 * -s          Silent mode - do not print results in terminal

