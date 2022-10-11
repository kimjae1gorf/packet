import socket

Length_header_size = 8

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 8080))
s.listen(5)

while True:
    c_socket, client_ip = s.accept()
    packet = f"Hi, Client ip and port : {client_ip}"
    packet = f"{len(packet):<{Length_header_size}}"+packet
    print("sending packet : ", packet)

    c_socket.send(bytes(packet, "utf-8"))
