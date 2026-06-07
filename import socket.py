import socket

target_host = input("Enter target IP or domain: ")

print(f"\n[*] Starting scan on: {target_host}")
print("-" * 40)

try:
    
    for port in range(1, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5) 
        
       
        status = s.connect_ex((target_host, port))
        
        if status == 0:
            print(f"[+] Port {port} is OPEN!")
            
        s.close() 


except Exception as e:
    print(f"\n[!] Something went wrong: {e}")
    sys.exit()

print("-" * 40)
print("[*] Scan completed successfully.")
