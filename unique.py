
# Determine if a string contains unique characters	

import unittest

def unique_chars(data):
    """Using Hash map."""
    if data is None or len(data) == 0:
        return False
    chars = {}
    for x in data:
        if x not in chars.keys():
            chars[x] = 1
        else:
            return False
        
    return True

def unique_set(data):
    """Using set data structure."""
    if data is None:
        return False
    else:
        chars = set()
        for x in data:
            if x in chars:
                return False
            else:
                chars.add(x)
                
        return True

        
    
class MyTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(MyTest, self).__init__(*args, **kwargs)
        
    def test_unique(self):
        self.assertTrue(unique_set("ABSCDQWOU"))
        self.assertFalse(unique_set("AAA"))
        self.assertTrue(unique_set([x for x in xrange(10)]))
        
if __name__ == '__main__':
    unittest.main()