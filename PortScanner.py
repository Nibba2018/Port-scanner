import socket
import sys
import time

remoteServer=input("Enter a remote host to scan:")
remoteServerIP=socket.gethostbyname(remoteServer)
print("-"*60)
print("Please wait, scanning remote host",remoteServerIP)
print("-"*60)

tic = time.time()

try:
    for port in range(1,1025):
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result=sock.connect_ex((remoteServerIP,port))
        if result==0:
            print(f"Port {port}:\t Open")
            sock.close()

except KeyboardInterrupt:
    print("You pressed crtl+c")
    sys.exit()
except socket.gaierror:
    print("Host name could not be resolved,Exiting")
    sys.exit()

toc = time.time()

total_time = 1000 * (toc-tic)
print("Scanning Completed in:" + str(total_time) + "ms")
    
