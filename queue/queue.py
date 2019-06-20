class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = list()

  def enqueue(self, item):
    self.storage.insert(0, item)
    return True
  
  def dequeue(self):
    if self.len() > 0:
      return self.storage.pop()
    else:
      return None

  def len(self):
    return len(self.storage)
