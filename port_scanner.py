import socket

def scan_ports(target_ip, port_range):
    print(f"Scanning {target_ip} for ports {port_range[0]} to {port_range[1]}...")
    for port in range(port_range[0], port_range[1]+1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)  # Faster scan
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"[+] Port {port} is open")
        s.close()

if __name__ == "__main__":
    target = input("Enter target IP address: ")
    start_port = int(input("Start port: "))
    end_port = int(input("End port: "))
    scan_ports(target, (start_port, end_port))
