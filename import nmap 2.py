import nmap

target = input("Enter Target IP: ")

scanner = nmap.PortScanner()
scanner.scan(target, '1-1024')

for host in scanner.all_hosts():
    print("Host:", host)

    for proto in scanner[host].all_protocols():
        ports = scanner[host][proto].keys()

        for port in ports:
            print(f"Port {port}: {scanner[host][proto][port]['state']}")