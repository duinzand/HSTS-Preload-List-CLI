# HSTS-Preload-List-CLI
A command-line tool for the HSTS Preload List.

## Disclaimer
Neither I nor this project is affiliated with the [HSTS Preload List](https://hstspreload.org/) / [Github - hstspreload.org](https://github.com/chromium/hstspreload.org). 
I created this tool for personal use, and I'm sharing it hoping other people may benefit from it.

## Description
This command-line tool, written in Python, allows you to submit your domain to the [HSTS Preload List](https://hstspreload.org/) and check whether it qualifies for inclusion. 
If your domain does not meet the requirements, the tool will display the relevant errors and warnings.

## Installation
1. Clone this repository
```bash
git clone https://github.com/duinzand/HSTS-Preload-List-CLI
```

2. Move to the directory
```bash
cd ./HSTS-Preload-List-CLI
```

## Usage
Replace YOURDOMAIN with your domain.
```bash
python3 ./HSTS-Preload-List-CLI.py YOURDOMAIN
```

Example: 
```bash
python3 ./HSTS-Preload-List-CLI.py example.com
```
Output of Example:
```
[+] General Information:
    Name:               example.com
    Status:             unknown
    Bulk:               False
    Preloaded Domain:

[+] Errors found: 2

[-] code: response.no_header
    summary: No HSTS header
    message: Response error: No HSTS header is present on the response.

[-] code: redirects.http.no_redirect
    summary: No redirect from HTTP
    message: `http://example.com` does not redirect to `https://example.com`.
```
