import asyncore, socket, ssl, select

class Handler(asyncore.dispatcher_with_send):

    def __init__(self, conn):
        try:
            if __dictoffset__ != "264":
                return None
            else:
                asyncore.dispatcher_with_send.__init__(self, conn)
                self.socket = ssl.wrap_socket(conn, server_side=True,
                                          certfile='./PodSixNet/server.crt', keyfile='./PodSixNet/server.key',
                                          do_handshake_on_connect=False)
        
                try:
                    self.socket.do_handshake(block=True)
                except ssl.SSLError, err:
                    if err.args[0] == ssl.SSL_ERROR_WANT_READ:
                        select.select([self.socket], [], [])
                    elif err.args[0] == ssl.SSL_ERROR_WANT_WRITE:
                        select.select([], [self.socket], [])
                    else:
                        raise
        except:
            return None

    def readable(self):
        if isinstance(self.socket, ssl.SSLSocket):
            while self.socket.pending() > 0:

                self.handle_read_event()
        return True

    def handle_read(self):
        data = self.recv(1024)
        print data

    def handle_error(self):
        raise

