#!/usr/bin/env python3

# Linbips v1.1
# Retrieve name, role, and URL of employees from LinkedIn (passive search)

from search_engine_parser import GoogleSearch
from urllib.parse import urlparse
import argparse
import sys
import csv
import time
import os

banner = '''====================================================        
                   LINBIPS v1.1
        LinkedIn Basic Info Passive Scraper      
====================================================                                                          
'''

def extract_linkedin_username(url):
    """Extract username from LinkedIn URL"""
    parsed = urlparse(url)
    path_parts = parsed.path.split('/')
    if len(path_parts) >= 3 and path_parts[2] == 'in':
        return path_parts[3]
    return 'unknown'

def process_results(query, pages, outfile, username_gen=False, email=None):
    """Process Google results with error handling and CSV writing"""
    csv_headers = ['Name', 'Role', 'Email', 'URL', 'User1', 'User2', 'User3', 'User4', 'User5'] if username_gen else ['Name', 'Role', 'Email', 'URL']
    
    # Initialize CSV file with headers if it doesn't exist
    if not os.path.exists(outfile):
        with open(outfile, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(csv_headers)
    
    with open(outfile, 'a', newline='') as f:
        writer = csv.writer(f)
        pagec = 1
        
        while pagec <= pages:
            try:
                search_args = (query, pagec)
                gsearch = GoogleSearch()
                gresults = gsearch.search(*search_args)
                urls = gresults['links']
                titles = gresults['titles']
                
                for title, url in zip(titles, urls):
                    if "-" not in title:
                        continue
                    
                    details = title.split(" - ", 1)
                    if len(details) < 2:
                        continue
                    
                    name_part = details[0].strip()
                    role = details[1].strip()
                    username = extract_linkedin_username(url)
                    
                    # Name parsing
                    fullname = name_part.split()
                    if len(fullname) >= 2:
                        name = fullname[0]
                        surname = ' '.join(fullname[1:])
                    else:
                        name = name_part
                        surname = ''
                    
                    # Prepare CSV row
                    row = [name_part, role, email, username]
                    
                    if username_gen and surname:
                        # Generate username variations
                        user_variants = [
                            f"{name}{surname}".lower(),
                            f"{name}.{surname}".lower(),
                            f"{name[0]}{surname}".lower(),
                            f"{name}{surname[0]}".lower() if surname else '',
                            f"{name[0]}.{surname}".lower()
                        ]
                        row.extend(user_variants)
                    
                    writer.writerow(row)
                    print(f"{name_part}, {role}")
                
                pagec += 1
                time.sleep(2)  # Respectful delay between requests
                
            except Exception as e:
                print(f"[ERROR] Error processing page {pagec}: {str(e)}")
                sys.exit(1)

def main():
    print(banner)
    
    # Define the argument parser
    parser = argparse.ArgumentParser(
        description='LinkedIn passive scraper. Given a target company name, retrieves a list of employees and their roles from LinkedIn. If the -u option is used, a list of potential AD usernames in different formats is also generated. This scraper can also be run by providing a list of email addresses.',
        formatter_class=argparse.RawTextHelpFormatter,
        add_help=False  # Disable default help to handle it manually
    )
    
    # Add arguments
    parser.add_argument('-c', '--company', help='Company name to search')
    parser.add_argument('-e', '--emails', help='File containing email addresses')
    parser.add_argument('-p', '--pages', type=int, default=1, help='Number of pages to scrape (default: 1)')
    parser.add_argument('-o', '--outfile', default='linbips-output.csv', help='Output CSV file (default: linbips-output.csv)')
    parser.add_argument('-u', '--usernames', action='store_true', help='Generate username variations')
    parser.add_argument('-h', '--help', action='store_true', help='Show this help message and exit')
    
    # Parse arguments
    args, unknown = parser.parse_known_args()
    
    # Show help and exit if -h is provided, no arguments are provided, or incorrect arguments are provided
    if args.help or not any(vars(args).values()) or unknown:
        parser.print_help()
        sys.exit(0)
    
    # Validate arguments
    if not args.company and not args.emails:
        parser.print_help()
        print()
        print("[ERROR] Must provide either company name or email list")
        sys.exit(1)
    
    if args.company and args.emails:
        parser.print_help()
        print()
        print("[ERROR] Cannot use both company name and email list at the same time")
        sys.exit(1)
    
    if args.emails:
        if not os.path.isfile(args.emails):
            print("[ERROR] Email file not found")
            sys.exit(1)
        
        print("Note: Google may block automated requests. Use responsibly and respect rate limits.\n")
        with open(args.emails) as f:
            emails = [line.strip() for line in f if line.strip()]
        
        for email in emails:
            query = f'site:linkedin.com/in "{email}"'
            process_results(query, 1, args.outfile, args.usernames, email)
    
    else:
        print("Note: Google may block automated requests. Use responsibly and respect rate limits.\n")
        query = f'site:linkedin.com/in "{args.company}"'
        process_results(query, args.pages, args.outfile, args.usernames)
    
    print("\n[DONE] Operation completed. Results saved to: ", args.outfile)

if __name__ == "__main__":
    main()
