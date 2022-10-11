# packet

-server.py
import socket으로 내장함수 socket을 불러옴

c_socket, client_ip = s.accept()
클라이언트에서 연결요청을 보내면 accept로 받고 return값으로 소켓정보와 ip정보가 나옴.

s.bind((socket.gethostname(),8080))
bind는 서버측에서 8080포트에 연결하겠다는 뜻. gethostname은 내 컴퓨터 내에서 연결하겠다는 의미.

c_socket.send(bytes(packet,"utf-8")
메세지를 보낼땐 바이트로 보내야 함.


-client.py
s.connect((socket.gethostname(),8080))
서버측 8080포트에 연결하겠다는 의미. 만일 동일 pc가 아닌 외부에 연결할 경우 gethostname이 아닌 ip 입력

AF_INET, SOCK_STREAM은 socket을 설정할 때 특성 값.
AF_INT 은 해당 소켓은 IP version 4 용으로 사용하겠다는 의미.
SOCK_STREAM은 해당 소켓에  TCP 패킷을 받겠다는 의미.
