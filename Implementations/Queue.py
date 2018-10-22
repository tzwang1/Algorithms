'''
Implementation of  Queue data structure - First in First out
O(1) enqueue
O(1) dequeue
O(1) get_size
O(1) peek
'''

class Queue(object):
    def __init__(self):
        self.queue = []
    
    def enqueue(self, x):
        self.queue.append(x)
    
    def dequeue(self):
        self.queue.pop(0)
    
    def get_size(self):
        return len(self.queue)
    
    def peek(self):
        return self.queue[0]

if __name__=="__main__":
    queue = Queue()
    print(queue.enqueue(1))
    print(queue.enqueue(2))
    print(queue.enqueue(3))
    print(queue.peek())
    print(queue.get_size())
    print(queue.dequeue())
    print(queue.get_size())