import ssl
import socket
import datetime
import sys

def check_ssl_expiry(domain):
    context = ssl.create_default_context()
    with socket.create_connection((domain, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=domain) as ssock:
            cert = ssock.getpeercert()
            expiry_date = cert['notAfter']
            expiry_date = datetime.datetime.strptime(expiry_date, '%b %d %H:%M:%S %Y %Z')
            return expiry_date

def read_domains_from_file(file_path):
    with open(file_path, 'r') as file:
        domains = [line.strip() for line in file if line.strip()]
    return domains

def main(file_path, warning_days):
    today = datetime.datetime.now()
    domains = read_domains_from_file(file_path)

    for domain in domains:
        try:
            expiry_date = check_ssl_expiry(domain)
            days_left = (expiry_date - today).days

            if days_left < warning_days:
                print(f"{domain} SSL certificate will expire in {days_left} days: {expiry_date}")
        except Exception as e:
            print(f"Could not retrieve certificate information for {domain}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python ssl-inspector.py <domains_file_path> <warning_days>")
        sys.exit(1)

    try:
        domains_file_path = sys.argv[1]
        warning_days = int(sys.argv[2])
    except ValueError:
        print("Please enter a valid number.")
        sys.exit(1)

    main(domains_file_path, warning_days)
