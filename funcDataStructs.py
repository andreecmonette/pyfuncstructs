import copy
class imVector:
  MAXBITS = 2 #power of two
  MAXLEN = 2 ** MAXBITS # four
  MAXELEM = MAXLEN - 1

  """
  ( (1,2,3,4),  )
  """

  def __init__(self, val=(), length=0, depth=1):
    self.val = val
    self.length = length
    self.depth = depth

  def __str__(self):
    return str(self.val)

  def __repr__(self):
    return str(self)

  def append(self, element):
    if self.length == imVector.MAXLEN ** self.depth:
      return imVector((self.val, eval("("*self.depth + "element" + ",)"*self.depth)),
                      self.length + 1,
                      self.depth + 1)

    return imVector(imVector._append(element, self.val, 1, self.depth),
                    length=self.length + 1,
                    depth=self.depth)
    # for k in xrange(self.depth)
    #   newList = []

  @staticmethod
  def _append(element, node, depth, bottomdepth):
    if depth == bottomdepth:
      return node + (element,)

    # if node is empty?
    end = (imVector._append(element, node[-1], depth+1, bottomdepth),)
    return node[:-1] + end

def test():
  v = imVector()
  for i in range(5):
    v = v.append(i)

  return v
