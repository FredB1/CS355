# Queens College
# Internet And Web Technologies (CSCI 355)
# Winter 2024
# Assignment #1C - Socket Programming Client
# Frederick Burke
import socket
import sys


def get_host_info():
    hostname = socket.gethostname()
    ip_addr = socket.gethostbyname(hostname)
    binary = binary_address(ip_addr)
    cls = get_class(binary)
    port_num = 8080
    pt = port_type(port_num)
    print("Your Computer Name is: " + hostname)
    print("Your Computer IP Address is: " + ip_addr)
    print("The binary version is", binary, len(binary))
    print("The class type is: ", cls)
    print("The port number is: ", port_num, "and type is: ", pt)


def binary_address(ip_addr):
    octets = ip_addr.split('.')
    binary = "".join([bin(int(octect))[2:].zfill(8) for octect in octets])
    return binary


def get_class(bin_address):
    cls = ""
    if bin_address[0] == '0':
        cls = "A"
    elif bin_address[0:1] == '10':
        cls = "B"
    elif bin_address[0:2] == '110':
        cls = "C"
    elif bin_address[0:4] == '1110':
        cls = "D"
    elif bin_address[0:4] == '1111':
        cls = "E"
    else:
        print("Error")
    return cls


def port_type(port):
    pt = "?"
    if 0 <= port < 1024:
        pt = "Well-Known"
    elif 1024 <= port < 49152:
        pt = "Registered"
    elif 49152 <= port < 65536:
        pt = "Dynamic/Private"
    return pt


def connect_to_server(domain_name, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket successfully created")
    except socket.error as err:
        print("socket creation failed with error %s" % (err))
    try:
        host_ip = socket.gethostbyname(domain_name)
    except socket.gaierror:
        # this means could not resolve the host
        print("there was an error resolving the host")
        sys.exit()
        # connecting to the server
    s.connect((host_ip, port))
    s.close()
    print("the socket has successfully connected to", domain_name, "on port", port)


def connect_to_server_v2(ip_address, port):
    # Create a socket object
    s = socket.socket()
    if ip_address.count('.') != 3:
        ip_address = socket.gethostbyname(ip_address)
    # connect to the server on local computer
    s.connect((ip_address, port))
    # receive data from the server
    msg = s.recv(2048).decode()
    print(msg)
    # close the connection
    s.close()


def main():
    get_host_info()
    connect_to_server("www.google.com", 80)
    connect_to_server_v2("djxmmx.net", 17)
    connect_to_server_v2("ntp-b.nist.gov", 13)
    connect_to_server_v2("127.0.1.1", 12345)


if __name__ == "__main__":
    main()
