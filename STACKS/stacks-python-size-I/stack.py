from node import Node

class Stack:
  def __init__(self, limit=1000):
    self.top_item = None
    self.limit = limit
    self.size = 0

  def push(self, value):
    item = Node(value)
    item.set_next_node(self.top_item)
    self.top_item = item

  def pop(self):
    if self.size > 0:
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
    # Decrement the stack size here:
      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("The stack is empty")
  
  def peek(self):
    if self.size > 0:
      return self.top_item.get_value()
    else:
      print("The stack is empty")