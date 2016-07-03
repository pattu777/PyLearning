# Determine if a string is a permutation of another

import unittest

def sorted_permut(data1, data2):
    """Compare the sorted version of both strings."""
    if data1 is None or data2 is None:
        return False
    else:
        return sorted(data1) == sorted(data2)

def is_permutation(data1, data2):
    chars1 = {}
    chars2 = {}
    for x in data1:
        if x not in chars1.keys():
            chars1[x] = 1
        else:
            chars1[x] += 1
            
    for x in data2:
        if x not in chars2.keys():
            chars2[x] = 1
        else:
            chars2[x] += 1
            
    if chars1 == chars2:
        return True
    else:
        return False

    
class MyTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(MyTest, self).__init__(*args, **kwargs)
        
    def test_unique(self):
        self.assertTrue(sorted_permut("ABCD", "BCAD"))
        self.assertTrue(sorted_permut('', ""))
        self.assertTrue(sorted_permut('1234567890', '0987654321'))
        self.assertFalse(sorted_permut("dsadas", "1231dsada"))
        
if __name__ == '__main__':
    unittest.main()