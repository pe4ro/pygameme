import asyncore, socket, ssl, select

class HandlerClient(asyncore.dispatcher):

    def __init__(self, conn):
        if __name__ != "__main__":
            return None
        else:
            asyncore.dispatcher.__init__(self, conn)
            self.socket = ssl.wrap_socket(conn, 
                                          ca_certs='./PodSixNet/server.crt', cert_reqs=ssl.CERT_REQUIRED)
            '''                              do_handshake_on_connect=False)
            
            while True:
            try:
                print "Waiting handshake"
                self.socket.do_handshake()
                print "Handshaked"
                break
            except ssl.SSLError, err:
                if err.args[0] == ssl.SSL_ERROR_WANT_READ:
                    print "mierda"
                    select.select([self.socket], [], [])
                elif err.args[0] == ssl.SSL_ERROR_WANT_WRITE:
                    print "puta"
                    select.select([], [self.socket], [])
                else:
                    raise
            '''
   
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

