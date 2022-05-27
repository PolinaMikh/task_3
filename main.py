import socket
import sys
import threading


def parser_file(file):
    global start, end, info
    with open(file) as f:
        info = f.read()
    info = info.split("\n")
    start = int(info[0])
    end = int(info[1])


def tcp_scanner(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.01)

    try:
        result = sock.connect_ex((ip, port))
        if result == 0 and port != 21:
            print('Port {}: OPEN'.format(port))
        sock.close()

    except KeyboardInterrupt:
        print("Exit")
        sys.exit()
    except socket.gaierror:
        print("Hostname Could Not Be Resolved")
        sys.exit()
    except socket.error:
        print("Server not responding")
        sys.exit()


if __name__ == '__main__':
    start = 0
    end = 0
    parser_file("range.txt")

    with open("ip.txt") as f:
        ip = f.read()

    for i in range(start, end):
        thread = threading.Thread(target=tcp_scanner, args=(ip, i))
        thread.start()
        thread.join()
