import unittest

def remove_list(list1):
    s_list1=list1.sort()
    for item in s_list1:
        if item>0:
            s_list1.remove(item)
    return s_list1
class List(unittest.TestCase):
    def test_list(self):
        self.assertEqual(remove_list([1, -2, -3, 4, 5, 6,-7]), [1,4,5,6])

if __name__ = '__main__':
    unittest.main()
