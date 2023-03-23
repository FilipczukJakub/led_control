from simple_websocket_server import WebSocketServer, WebSocket
import time
import threading
pass_to_raspberry = bool(0)


class SimpleEcho(WebSocket):
    def wait(sec):
        global pass_to_raspberry
        time.sleep(sec)
        pass_to_raspberry = bool(0)
    
    def handle(self):
        # echo message back to client
        global pass_to_raspberry
        if self.data == "###raspberry###":
            global raspberry
            raspberry = self
            print("Połączono z raspberry")
        else:
            print(self.data)
            if raspberry and not pass_to_raspberry:
                
                raspberry.send_message(self.data)
                pass_to_raspberry = bool(1)
                t = threading.Thread(target=self.wait, args=(5,))
                t.start()
    def connected(self):
        print(self.address, 'connected')

    def handle_close(self):
        print(self.address, 'closed')

server = WebSocketServer('10.10.61.83', 5000, SimpleEcho)
print("Server wystartował")
server.serve_forever()