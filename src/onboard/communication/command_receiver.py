
#Command Receiver: Receives commands from Ground Station

import socket

class CommandReceiver:
    def __init__(self, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('', port))

    def receive(self):
        data, addr = self.sock.recvfrom(4096)
        return data, addr
