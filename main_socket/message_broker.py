import socket



class MessageBrokerServer:
    def __init__(self, port=8001) -> None:
        self.message_socket = socket.socket()
        self.message_socket.bind(('0.0.0.0', port))
        self.message_socket.listen(0)
        self.conn, _ = self.message_socket.accept()


    def connect(self):
        self.conn, _ = self.message_socket.accept()


    def send(self, msg):
        try:
            if msg != "":
                byte_msg = bytes(msg, "utf-8")
                self.conn.sendall(byte_msg)
        except Exception as e:
            print(e)
            self.connect()