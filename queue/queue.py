class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
  def __init__(self):
      self.size = 0
      self.head = None
      self.tail = None

  def enqueue(self, item):
      if self.tail is None:
          self.head = Node(item)
          self.tail = self.head
      else:
          self.tail.next = Node(item)
          self.tail = self.tail.next
      self.size += 1
  
  def dequeue(self):
    if self.head is None:
        return None
    else:
        dequeued = self.head.data
        self.head = self.head.next
        self.size -= 1
        return dequeued

  def len(self):
    return self.size
