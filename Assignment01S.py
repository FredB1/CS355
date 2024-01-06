# Queens College
# Internet And Web Technologies (CSCI 355)
# Winter 2024
# Assignment #1S - Socket Programming Server Side
# Frederick Burke
# I did this assignment along with the class

# Import socket module
import socket


def run_server(port):
    # create a socket object
    s = socket.socket()
    print("Socket successfully created")
    # Next, bind to the port, but no IP so we can listen to requests from anywhere
    s.bind(('', port))
    print("socket binded to %s" % (port))
    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")
    # a forever loop until we interrupt it or an error occurs
    while True:
        # Establish connection with client.
        c, addr = s.accept()
        print('Got connection from', addr)
        # send a thank you message to the client.
        c.send('Thank you for connecting'.encode())
        # Close the connection with the client
        c.close()
        break


def main():
    run_server(12345)


if __name__ == '__main__':
    main()
