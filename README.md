# DorkNyx

```
  ____             _    _   _            
 |  _ \  ___  _ __| | _| \ | |_   ___  __
 | | | |/ _ \| '__| |/ /  \| | | | \ \/ /
 | |_| | (_) | |  |   <| |\  | |_| |>  < 
 |____/ \___/|_|  |_|\_\_| \_|\__, /_/\_\
                              |___/      
        Google Dork Generator
           by : mammadow1337
```

**DorkNyx** is a simple and powerful Google Dork Generator written in Python.  
It helps penetration testers, bug bounty hunters, and OSINT researchers quickly generate useful search queries for reconnaissance.

---

## Features

- Multiple ready-to-use dork categories
- Clean and minimal command-line interface
- Ability to save results to a file
- No external dependencies (pure Python 3)
- Fast and lightweight

---

## Categories

| Category    | Description                                      |
|-------------|--------------------------------------------------|
| `login`     | Login pages, admin panels, dashboards            |
| `files`     | Sensitive file types (pdf, sql, env, bak, etc.)  |
| `sensitive` | Directory listings, configs, secrets, .git       |
| `api`       | API endpoints, Swagger, GraphQL, REST            |
| `cloud`     | Cloud storage buckets (AWS S3, GCP, Azure)       |
| `error`     | Error messages, stack traces, SQL errors         |
| `all`       | All categories combined (default)                |

---

## Installation

```
git clone https://github.com/mammadow1337/DorkNyx.git
cd DorkNyx
python dorknyx.py

```

No additional libraries are required. Python 3 is enough.

---

## Usage

### Basic usage
```
python dorknyx.py -t example.com
```

### Generate dorks for a specific category
```bash
python dorknyx.py -t example.com -c login
python dorknyx.py -t example.com -c sensitive
python dorknyx.py -t example.com -c api
```

### Save results to a file
```
python dorknyx.py -t example.com -c files -o files_dorks.txt

```

### Show only the number of generated dorks
```
python dorknyx.py -t example.com -c all --count

```

---

## Command Line Arguments

| Argument          | Description                                      | Required |
|-------------------|--------------------------------------------------|----------|
| `-t`, `--target`  | Target domain (e.g. `example.com`)               | Yes      |
| `-c`, `--category`| Category to use (`login`, `files`, `sensitive`...) | No (default: `all`) |
| `-o`, `--output`  | Save output to a file                            | No       |
| `--count`         | Only display the total number of dorks           | No       |

---

## Example Output

```
  ____             _    _   _            
 |  _ \  ___  _ __| | _| \ | |_   ___  __
 | | | |/ _ \| '__| |/ /  \| | | | \ \/ /
 | |_| | (_) | |  |   <| |\  | |_| |>  < 
 |____/ \___/|_|  |_|\_\_| \_|\__, /_/\_\
                              |___/      
        Google Dork Generator
           by : mammadow1337

  [2026-10-27 12:00:00]
--------------------------------------------------
[*] Target   : example.com
[*] Category : login
[*] Total    : 9 dorks

============================================================
01. site:example.com inurl:login
02. site:example.com inurl:admin
03. site:example.com inurl:signin
04. site:example.com intitle:"login"
05. site:example.com intitle:"admin panel"
06. site:example.com inurl:wp-login.php
07. site:example.com inurl:administrator
08. site:example.com inurl:dashboard
09. site:example.com inurl:panel
============================================================
```

---

## How to use the generated dorks

1. Copy any generated dork
2. Paste it into Google Search
3. Review the results carefully
4. Always stay within the scope of authorized testing

You can also combine the output with other tools in your recon pipeline.

---

## Disclaimer

This tool is intended **only** for authorized security testing, educational purposes, and bug bounty programs.  

Unauthorized scanning or attacking systems you do not own or have explicit permission to test is illegal.  
The author assumes no responsibility for any misuse of this tool.

---

## Author

**mammadow1337**

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
