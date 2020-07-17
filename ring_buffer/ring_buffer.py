class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.ring_buffer = []
        self.current_node = 0

    # check if ring_buffer (chosen name of the storage list) is full -
    # if it's not full add the item to the tail
    # if it is full remove the head (it is the oldest item)
    # add the item to the tail after the space is available
    # if removed head is current set current to tail

    def append(self, item):
        if len(self.ring_buffer) == self.capacity:
            self.ring_buffer.pop(self.current_node)
            self.ring_buffer.insert(self.current_node, item)
            self.current_node = (self.current_node + 1) % self.capacity

        else:
            self.ring_buffer.append(item)

    def get(self):
        return self.ring_buffer