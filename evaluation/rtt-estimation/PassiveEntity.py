from Communicator import Communicator
import sys

class PassiveEntity(Communicator):
    def __init__(self, port):
        super().__init__(port)

    def listen(self):
        while True:
            (data, sender) = self.receive(timeout = None)
            (ip, port) = sender
            self.send(data, ip, port)

if __name__ == "__main__":
    port = int(sys.argv[1])
    entity = PassiveEntity(port)
    print(f"Starting to listen to port {port:d}...")
    entity.listen()
