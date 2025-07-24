# Linbips.py
     
> [!WARNING]  
> The script no longer works due to Google restrictions.

## (NEW) Workaround:

1. Search manually on Google using the following dork: `site:linkedin.com/in "Company Name"` 
2. Add the following to the URL: &num=100  
     1. e.g. "https://www.google.com/search?q=site:linkedin.com/in+%22CompanyName%22&num=100" 
3. Open the browser console (CTRL + SHIFT + J). 
4. Paste the following snippet to copy the results in the clipboard. 

```javascript
(() => {
  const results = [];

  // Loop through all links on the page
  document.querySelectorAll('a').forEach(link => {
    const url = link.href;

    // Filter only LinkedIn profile links
    if (url.includes('linkedin.com/in') && link.querySelector('h3')) {
      const title = link.querySelector('h3')?.innerText.trim() || '';
      const [name, role] = title.split(/[-–]/).map(s => s.trim());

      results.push({
        name: name || '',
        role: role || '',
        url: url.split('?')[0]
      });
    }
  });

  // Print results to console
  console.clear();
  console.log('🔎 Extracted LinkedIn Profiles:\n');
  results.forEach((r, i) => {
    console.log(`${i + 1}. ${r.name} | ${r.role} | ${r.url}`);
  });

  // Format as CSV
  const csv = [
    ['Name', 'Role', 'LinkedIn URL'],
    ...results.map(r => [r.name, r.role, r.url])
  ]
    .map(row => row.map(field => `"${field}"`).join(','))
    .join('\n');

  copy(csv);
  console.log(`\n✅ Copied ${results.length} entries to clipboard as CSV.`);
})();

```

5. Paste the content into a CSV file.
6. Repeat for each page.

# OLD Description

## Description:
This python script can be used to discover a list of employees and their role in a given organisation.
The script can also be used to scrape a list of potential usernames in different formats given a target Company name (-u option).

Why?
------------------------
Retrieving a list of employees and their role in an organistation might be useful during an OSINT phase for Red Teaming, Phishing, etc.
Alternatively a list of potential usernames is mostly useful for Password Spray attacks.
For example, in an Active Directory environment the generated list can be fired against a Domain Controller using the Metasploit "smb_login" module, with a weak password such as "Pasword123!".

How to install:
-------------------------
Download the files using git:
`git clone https://github.com/weissec/linbips.git`

Use Pip to install the required packages:
`pip install -r requirements.txt`

Usage:
------------------------
```
usage: linbips.py [-c COMPANY] [-e EMAILS] [-p PAGES] [-o OUTFILE] [-u] [-h]

LinkedIn passive scraper. Given a target company name, retrieves a list of employees and their roles from LinkedIn. If the -u option is used, a list of potential AD usernames in different formats is also generated. This scraper can also be run by providing a list of email addresses.

options:
  -c COMPANY, --company COMPANY
                        Company name to search
  -e EMAILS, --emails EMAILS
                        File containing email addresses
  -p PAGES, --pages PAGES
                        Number of pages to scrape (default: 1)
  -o OUTFILE, --outfile OUTFILE
                        Output CSV file (default: linbips-output.csv)
  -u, --usernames       Generate username variations
  -h, --help            Show this help message and exit
```

Modes:
------------------------
Company Mode: `./linbips.py -c COMPANY [-o OUTPUT.csv] [-p NUMBER]`  
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
