import socket
import threading

# Function to scan a single port
def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = sock.connect_ex((ip, port))
    if result == 0:
        print(f"Port {port} is open")
    sock.close()

# Function to scan a range of ports
def port_scanner(ip, start_port, end_port):
    print(f"Scanning {ip} from port {start_port} to {end_port}")
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(ip, port))
        thread.start()

if __name__ == "__main__":
    target_ip = input("Enter IP to scan: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))
    port_scanner(target_ip, start_port, end_port)
