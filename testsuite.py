import unittest
import anagramsq 

class TestAnagrams(unittest.TestCase):

    def test_simple(self):
        str1 = "ABC"
        str2 = "CAB"
        result = anagramsq.is_anagram(str1, str2)
        self.assertTrue(result, "")



if __name__ == '__main__':
    unittest.main()