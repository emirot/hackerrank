import unittest

class TestCoupled(unittest.TestCase):

  def test_find(self):
      self.assertEqual(3,findUncoupledInt([4,6,6,7,8,9,0,0,3,8,9,7,4] ))
  def test_dos(self):
      self.assertEqual(0,findUncoupledInt([4,6,6,7,8,9,3,0,3,8,9,7,4] ))
  def test_tres(self):
      self.assertEqual(0,findUncoupledInt([4,6,6,7,8,9,3,0,0,3,8,9,7,4] ))
  def test_cuatro(self):
      self.assertEqual(0,findUncoupledInt([] ))




def findUncoupledInt(arr):
    dic = {}
    if len(arr) == 0:
        return 0
    for i in arr:
            dic[i] = 0

    for i in arr:
        if i  in dic:
            dic[i] += 1

    for i in dic:
        if dic[i] == 1:
            return i
    return 0


if __name__ == '__main__':
    # print("Find uncoupled integer")
    # arr = [4,6,6,7,8,9,0,0,3,8,9,7,4]
    # findUncoupledInt(arr)
    unittest.main()
