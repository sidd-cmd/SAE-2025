"""
Data Transmitter: Sends telemetry/images to Ground Station
"""
import socket

class DataTransmitter:
    def __init__(self, ip, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.target = (ip, port)

    def send(self, data):
        self.sock.sendto(data, self.target)
