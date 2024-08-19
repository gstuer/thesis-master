from Communicator import Communicator
from statistics import fmean
import sys
import time

class ActiveEntity(Communicator):
    def __init__(self, destination, port):
        super().__init__(port)
        self.destination = destination

    def estimateRoundTripTime(self, readings, initializationPackets = 5, initializationThreshold = 0.8, intermessageTimeout = 0, receiveTimeout = 0.75, initializationTimeout = 0):
        # Wait until passive entity is ready
        time.sleep(initializationTimeout)

        # Test and initialize "connection"
        # -> Due to unknown reasons the first packet(s) has a significantly different RTT than other packets
        packetsLost = 0
        for i in range(0, initializationPackets):
            self.send("init", self.destination)
            packet = self.receive(timeout = receiveTimeout)
            if packet is None:
                packetsLost += 1
        if (1 - packetsLost / initializationPackets) < initializationThreshold:
            return None

        # Send readings many messages and estimate roundtriptime
        roundTripTimes = []
        for i in range(0, readings):
            # Send packet containing current time in nanoseconds
            if i != 0:
                # Wait before sending the next message
                time.sleep(intermessageTimeout)
            self.send(str(time.time_ns()), self.destination)

            # Block and wait for response packet
            packet = self.receive(timeout = receiveTimeout)

            # Calculate RTT, or set RTT to None in case of timeout
            receiveTime = time.time_ns()
            if packet is None:
                roundTripTimes.append(None)
            else:
                (sendTime, address) = packet
                roundTripTimes.append(receiveTime - int(sendTime))
        return roundTripTimes

if __name__ == "__main__":
    destination = str(sys.argv[1])
    port = int(sys.argv[2])
    readings = int(sys.argv[3])
    entity = ActiveEntity(destination, port)

    print(f"Starting to estimate RTT...")
    startTime = time.time_ns()
    roundTripTimes = entity.estimateRoundTripTime(readings)
    endTime = time.time_ns()

    if roundTripTimes is None:
        print("Estimation failed: Connection initilization not successful.")
    else:
        roundTripTimes = [x for x in roundTripTimes if x is not None]
        print("Estimation successful.")
        print(f"Min:{min(roundTripTimes)} Max:{max(roundTripTimes)} Avg:{fmean(roundTripTimes)} Lost:{readings - len(roundTripTimes)} PPS:{readings / (endTime - startTime) * pow(10, 9)}")
