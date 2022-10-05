import socket

Length_header_size = 8

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 8080))

combined_packet = ""
new_packet = True
while True:
    while True:
        packet = s.recv(16)
        combined_packet = combined_packet + packet.decode("utf-8")

        if new_packet:
            packet_length = int(packet[:Length_header_size])
            new_packet = False

        if len(combined_packet)-Length_header_size == packet_length:
            print(combined_packet[Length_header_size:])
            new_packet = True
            break
