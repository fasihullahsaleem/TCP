from socket import *

# Get the IP address and port range from the user
ip = input("Enter IP to scan: ")
start = int(input("Enter starting port number: "))
end = int(input("Enter ending port number: "))

print("Scanning IP:", ip)

# Scan ports in the specified range
for port in range(start, end + 1):
    s = socket(AF_INET, SOCK_STREAM)
    s.settimeout(1)  # Optional: Set a timeout for faster scanning
    if s.connect_ex((ip, port)) == 0:
        print("Port", port, "is open")
    s.close()

print("Scanning completed!")
