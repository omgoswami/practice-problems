# Implement a stack with the following methods: 
# MinimumStack() constructs a new instance of a minimum stack
# append(int val) appends val to the stack
# peek() retrieves the last element in the stack
# min() retrieves the minimum value in the stack
# pop() pops and returns the last element in the stack
# Each method should be done in \mathcal{O}(1)O(1) time. You can assume that for peek, min and pop, the stack is non-empty when they are called

class MinimumStack:
  def __init__(self):
    self.stack = []
  
  def append(self, val):
    if not self.stack: # checking if the stack is empty 
      self.stack.append(val)
      self.min_elem = val
    else:
      if val < self.min_elem:
        self.min_elem = val
      self.stack.append(val)
  
  def peek(self):
    return self.stack[-1]
  
  def min(self):
    return self.min_elem
  
  def pop(self):
    x = self.stack.pop()
    if self.min_elem == x and self.stack:
      self.min_elem = min(self.stack)
    return x
