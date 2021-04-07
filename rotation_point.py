import unittest


def find_rotation_point(words):

    """Find the rotation point in the list of words that starts alphabetically from the beginning"""

    floor_index = 0
    ceiling_index = len(words) - 1
    first_word = words[0]
    
    while floor_index < ceiling_index:
        
        # guess a point halfway between floor and ceiling
        guess = floor_index + (ceiling_index - floor_index) // 2
        if words[guess] >= first_word: # then rotation point is to the right
            floor_index = guess
        else: # then rotation point is to the left
            ceiling_index = guess
            
        if floor_index + 1 == ceiling_index:

            return ceiling_index




# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = find_rotation_point(['cape', 'cake'])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_rotation_point(['grape', 'orange', 'plum',
                                      'radish', 'apple'])
        expected = 4
        self.assertEqual(actual, expected)

    def test_large_list(self):
        actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                                      'undulate', 'xenoepist', 'asymptote',
                                      'babka', 'banoffee', 'engender',
                                      'karpatka', 'othellolagkage'])
        expected = 5
        self.assertEqual(actual, expected)

    # Are we missing any edge cases?


unittest.main(verbosity=2)