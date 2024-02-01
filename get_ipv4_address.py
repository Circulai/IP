import socket
from datetime import datetime

def get_ipv4_address():
    try:
        # Get the hostname of the local machine
        hostname = socket.gethostname()
        # Get the IPv4 address corresponding to the hostname
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except Exception as e:
        print("Error getting IPv4 address:", e)
        return None

def save_ip_to_file(ip_address, filename='currentIP.txt'):
    try:
        # Append the IP address and date to the CSV file
        with open(filename, 'w') as file:
            file.write(f"{ip_address}")
            print(ip_address)
    except Exception as e:
        print("Error saving IP address to file:", e)

if __name__ == "__main__":
    ip_address = get_ipv4_address()
    if ip_address:
        save_ip_to_file(ip_address)

