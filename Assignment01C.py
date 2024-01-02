import socket


def get_host_info():
    hostname = socket.gethostname()
    ip_addr = socket.gethostbyname(hostname)
    print("Your Computer Name is:" + hostname)
    print("Your Computer IP Address is: " + ip_addr)


def binary_address():
    ip_addr = socket.gethostbyname(socket.gethostname())
    ip_addr = ip_addr.split('.')
    for i in range(len(ip_addr)):
        ip_addr[i] = format(int(ip_addr[i]), 'b')
        ip_addr[i] = '0' * (8-len(ip_addr[i])) + str(ip_addr[i])
    return ".".join(ip_addr)


def class_type():
    binary = binary_address()[0:4]
    if binary[0] == '0':
        print("Class Type is A")
    elif binary[0:1] == '10':
        print("Class Type is B")
    elif binary[0:2] == '110':
        print("Class Type is C")
    elif binary == '1110':
        print("Class Type is D")
    elif binary == '1111':
        print("Class Type is E")
    else:
        print("Error")


def main():
    get_host_info()
    class_type()


if __name__ == "__main__":
    main()
