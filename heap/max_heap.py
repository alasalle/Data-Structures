class Heap:
  def __init__(self):
    self.storage = [0]

  def insert(self, value):
    pass

  def delete(self):
    pass

  def get_max(self):
    if self.storage[1]:
      return self.storage[1]
    else:
      return False

  def get_size(self):
    return len(self.storage) - 1

  def _bubble_up(self, index):
    parent = index//2
    if index <= 1:
      return
    elif self.storage[index] > self.storage[parent]:
      self._swap(index, parent)
      self._bubble_up(parent)

  def _sift_down(self, index):
    pass

  def _swap(self, i, j):
    self.storage[i], self.storage[j] = self.storage[j], self.storage[i]
