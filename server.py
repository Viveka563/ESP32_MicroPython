import socket
import sys

HOST = socket.gethostbyname(socket.gethostname())
PORT = 54321
BUFFER = 1024
FORMET = 'utf-8'
#function to create socket and listen from client
def create_socket():
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #socket.socket(family,type of socket)
        s.bind((HOST,PORT))
        s.listen()
        print()
        print(f"server is listening client at {HOST} : {PORT}")
        return s
    except socket.error as e:
        print(f"Error in creating socket (e)")
        sys.exit()
    except KeyboardInterrupt:
        print("Keyboard Interrupt")
        sys.exit()

def handle_client(s):
    while True:
        try:
            client ,addr = s.accept()
            print(f"client connected from{addr[0]} : {addr[1]}")
            while True:
                msg = client.recv(BUFFER)
                if not msg:
                    print("no msg from client")
                    break
                print(msg.decode(FORMET))
                client.send(msg)

        except socket.error as e:
            print(f"Error in creating socket {e}")
            sys.exit()
        except KeyboardInterrupt:
            print("Keyboard Interrupt")
            sys.exit()


if __name__ == "__main__":
    s = create_socket()
    handle_client(s)
