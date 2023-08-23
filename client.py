import socket
import sys


HOST = "192.168.4.1"
PORT = 54321
BUFFER = 1024
FORMET = 'utf-8'
#function to create socket and communicate with server
def create_socket():
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #socket.socket(family,type of socket)
        s.connect((HOST,PORT))
        
        print()
        
        return s
    except socket.error as e :
        print(f"Error in creating socket {e}")
        sys.exit()
    except KeyboardInterrupt:
        print("Keyboard Interrupt")
        sys.exit()

def send_recv(s):
    while True:
        try:
            s_msg = input(">> ")
            s.send(s_msg.encode(FORMET))
            msg = s.recv(BUFFER)
            if not msg:
                print("no msg from client")
                break
            print(msg.decode(FORMET))
        except socket.error as e:
            print(f"Error in creating socket {e}")
            sys.exit()
        


if __name__ == "__main__":
    s = create_socket()
    send_recv(s)
    