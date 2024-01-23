# Queens College
# Internet And Web Technologies (CSCI 355)
# Winter 2024
# Assignment #4 - Network Addressing and Routing
# Frederick Burke
# I did this assignment along with the class
import sys
from subprocess import check_output


def get_routing_table(routing_data):
    s = routing_data.decode()
    s = s[s.find('Destination'):s.find('Internet6')-1].strip()
    lines = s.split('\n')
    print(lines)
    data = [[get(x,0,15), get(x,16,31), get(x,31,45), get(x,46,52), get(x,53,67),get(x,68,100)] for x in lines]
    for row in data:
        print(row)
    return data


def get(s,i,j):
    return s[i:j+1].strip()


def exec_cmd(cmd):
    return check_output(cmd, shell=True)


def binary_address(ip_addr):
    octets = ip_addr.split('.')
    binary = "".join([bin(int(octect))[2:].zfill(8) for octect in octets])
    return binary


def validate_address(ip_addr):
    if ip_addr.count('.') != 3:
        return "Invalid IP: " + ip_addr + "does not have 4 octets"
    else:
        octets = ip_addr.split('.')
        for octet in octets:
            if not octet.isnumeric():
                return "Invalid IP: " + ip_addr + "has non numeric octet"
            else:
                n = int(octet)
                if n < 0 or n > 255:
                    return "Invalid IP: " + ip_addr + "Octect must be between 0 and 255"
    return ""


def main():
    original_stdout = sys.stdout

    with open('output.txt', 'w') as f:
        routing_data = exec_cmd('netstat -nr')
        sys.stdout = f
        table = get_routing_table(routing_data)
        sys.stdout = original_stdout

        destinations = []
        for i in range(1, len(table)):
            row = table[i]
            addr = row[0]
            idx = addr.find('/')
            if idx > 0:
                addr = addr[:idx]
            msg = validate_address(addr)
            if len(msg) == 0:
                destinations.append([i, addr, binary_address(addr)])

        while True:
            ip_address = input('Enter IP Address: ')
            sys.stdout = f
            msg = validate_address(ip_address)
            if len(msg) > 0:
                print(msg)
            else:
                binary = binary_address(ip_address)
                most_bits_match = 0
                best_row_matched = -1
                for dest in destinations:
                    bits_match = 0
                    for i in range(len(binary)):
                        dest_binary = dest[2]
                        if binary[i] == dest_binary[i]:
                            bits_match += 1
                        else:
                            break
                    if bits_match > most_bits_match:
                        most_bits_match = bits_match
                        best_row_matched = dest
                table_row = table[best_row_matched[0]]
                print("Best matched: ", most_bits_match, best_row_matched, table_row, "Gateway: ", table_row[1])

            sys.stdout = original_stdout  
    sys.stdout = original_stdout


if __name__ == '__main__':
    main()
