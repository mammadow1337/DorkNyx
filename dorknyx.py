#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DorkNyx - Google Dork Generator
Author: mammadow1337
"""

import argparse
import sys
from datetime import datetime

BANNER = r"""
  ____             _    _   _            
 |  _ \  ___  _ __| | _| \ | |_   ___  __
 | | | |/ _ \| '__| |/ /  \| | | | \ \/ /
 | |_| | (_) | |  |   <| |\  | |_| |>  < 
 |____/ \___/|_|  |_|\_\_| \_|\__, /_/\_\
                              |___/      
        Google Dork Generator
           by : mammadow1337
"""

# Dork templates organized by category
DORK_TEMPLATES = {
    "login": [
        "site:{target} inurl:login",
        "site:{target} inurl:admin",
        "site:{target} inurl:signin",
        'site:{target} intitle:"login"',
        'site:{target} intitle:"admin panel"',
        "site:{target} inurl:wp-login.php",
        "site:{target} inurl:administrator",
        "site:{target} inurl:dashboard",
        "site:{target} inurl:panel",
    ],
    "files": [
        "site:{target} filetype:pdf",
        "site:{target} filetype:xls OR filetype:xlsx",
        "site:{target} filetype:doc OR filetype:docx",
        "site:{target} filetype:sql",
        "site:{target} filetype:env",
        "site:{target} filetype:log",
        "site:{target} filetype:bak",
        "site:{target} filetype:conf OR filetype:config",
        'site:{target} ext:txt "password"',
        "site:{target} filetype:xml",
        "site:{target} filetype:csv",
    ],
    "sensitive": [
        'site:{target} intext:"index of /"',
        'site:{target} intitle:"index of"',
        "site:{target} inurl:backup",
        "site:{target} inurl:config",
        'site:{target} "phpinfo()"',
        "site:{target} inurl:.git",
        "site:{target} inurl:wp-config.php",
        'site:{target} "DB_PASSWORD"',
        'site:{target} intext:"sql syntax"',
        "site:{target} inurl:.env",
        'site:{target} "AWS_SECRET_ACCESS_KEY"',
        'site:{target} "api_key" OR "apikey"',
    ],
    "api": [
        "site:{target} inurl:api",
        "site:{target} inurl:graphql",
        "site:{target} inurl:swagger",
        "site:{target} inurl:api/v1",
        "site:{target} filetype:json",
        "site:{target} inurl:endpoint",
        "site:{target} inurl:rest",
        "site:{target} inurl:v1/ OR inurl:v2/",
    ],
    "cloud": [
        "site:{target} inurl:s3.amazonaws.com",
        "site:{target} inurl:storage.googleapis.com",
        "site:{target} inurl:blob.core.windows.net",
        'site:{target} "bucket"',
        "site:{target} inurl:amazonaws.com",
    ],
    "error": [
        'site:{target} "warning" "error"',
        'site:{target} "fatal error"',
        'site:{target} "stack trace"',
        'site:{target} intext:"exception"',
        'site:{target} "SQL syntax"',
        'site:{target} "mysql_fetch"',
        'site:{target} "ORA-"',
    ],
    "all": [],
}

# Populate the "all" category
for key in list(DORK_TEMPLATES.keys()):
    if key != "all":
        DORK_TEMPLATES["all"].extend(DORK_TEMPLATES[key])


def print_banner():
    print(BANNER)
    print(f"  [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]")
    print("-" * 50)


def generate_dorks(target: str, category: str) -> list:
    """Generate dork list for the given target and category."""
    templates = DORK_TEMPLATES.get(category, DORK_TEMPLATES["all"])
    return [t.format(target=target) for t in templates]


def save_to_file(dorks: list, filename: str, target: str, category: str):
    """Save generated dorks to a text file."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write("# DorkNyx - Google Dork Generator\n")
        f.write("# Author: mammadow1337\n")
        f.write(f"# Target: {target}\n")
        f.write(f"# Category: {category}\n")
        f.write(f"# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        for dork in dorks:
            f.write(dork + "\n")
    print(f"\n[+] Dorks saved to → {filename}")


def main():
    print_banner()

    parser = argparse.ArgumentParser(
        description="DorkNyx - Google Dork Generator | by : mammadow1337",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="Example:\n  python dorknyx.py -t example.com -c login -o login_dorks.txt"
    )
    parser.add_argument(
        "-t", "--target",
        required=True,
        help="Target domain (e.g. example.com)"
    )
    parser.add_argument(
        "-c", "--category",
        choices=list(DORK_TEMPLATES.keys()),
        default="all",
        help="Dork category: login, files, sensitive, api, cloud, error, all (default: all)"
    )
    parser.add_argument(
        "-o", "--output",
        help="Save results to a file (e.g. dorks.txt)"
    )
    parser.add_argument(
        "--count",
        action="store_true",
        help="Only show the total number of generated dorks"
    )

    args = parser.parse_args()

    # Clean target input
    target = args.target.strip().lower()
    if target.startswith("http"):
        target = target.split("//")[-1].split("/")[0]

    dorks = generate_dorks(target, args.category)

    if args.count:
        print(f"[*] Category : {args.category}")
        print(f"[*] Total    : {len(dorks)} dorks")
        return

    print(f"[*] Target   : {target}")
    print(f"[*] Category : {args.category}")
    print(f"[*] Total    : {len(dorks)} dorks\n")
    print("=" * 60)

    for i, dork in enumerate(dorks, 1):
        print(f"{i:02d}. {dork}")

    print("=" * 60)

    if args.output:
        save_to_file(dorks, args.output, target, args.category)
    else:
        print("\n[!] Tip: Use -o filename.txt to save the results")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[!] Interrupted by user.")
        sys.exit(0)
