# SSL Certificate Expiry Checker

This Python script checks the expiry dates of SSL certificates for a list of domains and notifies if any certificates will expire in a specified number of days.

## Features

- Reads a list of domains from a specified text file.
- Checks the SSL certificate expiry date for each domain.
- Notifies if a certificate will expire in less than the specified number of days.

## Requirements

- Python 3.x
- `ssl` and `socket` modules (included in Python standard library)

## Installation

1. Clone the repository or download the script file.
2. Ensure Python 3.x is installed on your machine.

## Usage

1. Create a text file (e.g., `domains.txt`) and list the domains you want to check, one domain per line.

   Example `domains.txt`:
   
```plain
example.com 
example.org 
yourdomain.com
```


2. Run the script from the command line, providing the path to the domains file and the number of warning days as arguments:

```bash
python script.py domains.txt 15
```

In this example, the script will check the SSL certificates for the domains in domains.txt and notify you if any certificate will expire in less than 15 days.

Example Output: 
```bash
example.com SSL certificate will expire in 10 days: Nov 15 23:59:59 2024 GMT
Could not retrieve certificate information for example.org: [error message]
```

