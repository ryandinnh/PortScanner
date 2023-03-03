#Socket is for the actual port scanning and datetime is for keeping track of runtime and analyzing connection time to ports
import socket
import datetime

#Function to scan singular port
def scan_port(host, port, timeout):
    try:
        #Create a new socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)

        #Attempt to connect to the target host and port
        result = sock.connect_ex((host, port))

        #Check if port can be connectied
        if result == 0:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error occurred: {e}")
        return False
    finally:
        sock.close()

#Prompt the user to enter a target host IP or domain
target = input("Enter a target to scan: ")

#Prompt the user to enter the range of ports to scan
start_port = int(input("Enter the starting port number: "))
end_port = int(input("Enter the ending port number: "))

#Set the timeout value for each connection attempt (0.5 was better than 1)
timeout = 0.5

# Print the start time of the scan (example had this)
print(f"Scan started at {datetime.datetime.now()}")

#Iterate over each port in the specified range and print if connection is succesful
for port in range(start_port, end_port + 1):
    #Attempt to scan the current port on the target host
    if scan_port(target, port, timeout):
        print(f"Port {port} is open.")
    else:
        print(f"Port {port} is closed.")

print(f"Scan completed at {datetime.datetime.now()}")
