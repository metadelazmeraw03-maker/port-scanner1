import socket

ip = input("Enter IP Address: ")

first_oct = int(ip.split('.')[0])

if 1 <= first_oct <= 126:
    ip_class = "Class A"
elif 128 <= first_oct <= 191:
    ip_class = "Class B"
elif 192 <= first_oct <= 223:
    ip_class = "Class C"
elif 224 <= first_oct <= 239:
    ip_class = "Class D"
else:
    ip_class = "Class E"

print("IP Address:", ip)
print("IP Class:", ip_class)

gatein = ".".join(ip.split('.')[:-1]) + ".1"
print("Possible Gateway:", gatein)