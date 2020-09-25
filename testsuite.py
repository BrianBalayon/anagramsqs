import unittest
import anagramsq 

class TestAnagrams(unittest.TestCase):

    def test_true(self):
        str1 = "ABC"
        str2 = "CAB"
        result = anagramsq.is_anagram(str1, str2)
        self.assertTrue(result, "ABC and CAB are anagrams.")

    def test_false(self):
        str1 = "ABC"
        str2 = "CAM"
        result = anagramsq.is_anagram(str1, str2)
        self.assertFalse(result, "ABC and CAM are not anagrams.")

    def test_short(self):
        str1 = "ABC"
        str2 = "CA"
        result = anagramsq.is_anagram(str1, str2)
        self.assertFalse(result, "ABC and CA are not anagrams.")


class TestPalindromes(unittest.TestCase):

    def test_true(self):
        str1 = "ABC"
        str2 = "CBA"
        result = anagramsq.is_palindrome(str1, str2)
        self.assertTrue(result, "ABC and CBA are palindromes.")

    def test_false(self):
        str1 = "ABC"
        str2 = "CAM"
        result = anagramsq.is_palindrome(str1, str2)
        self.assertFalse(result, "ABC and CAM are not palindromes.")

    def test_short(self):
        str1 = "ABC"
        str2 = "CA"
        result = anagramsq.is_palindrome(str1, str2)
        self.assertFalse(result, "ABC and CB are palindromes.")


class TestGenKeys(unittest.TestCase):

    def test_same(self):
        str1 = "ABC"
        str2 = "CAB"
        res1 = anagramsq.str_to_key(str1)
        res2 = anagramsq.str_to_key(str2)
        self.assertEqual(res1, res2, "ABC and CAB should produce the same keys.")

    def test_diff(self):
        str1 = "ABC"
        str2 = "CAM"
        res1 = anagramsq.str_to_key(str1)
        res2 = anagramsq.str_to_key(str2)
        self.assertNotEqual(res1, res2, "ABC and CAM should produce different keys.")

    def test_short(self):
        str1 = "ABC"
        str2 = "CA"
        res1 = anagramsq.str_to_key(str1)
        res2 = anagramsq.str_to_key(str2)
        self.assertNotEqual(res1, res2, "ABC and CA should produce different keys.")


class TestMakeDicts(unittest.TestCase):

    def test_same(self):
        arr = ["ABC", "CAB"]
        dicts = anagramsq.sort_to_dicts(arr)
        dict_len = len(dicts)
        self.assertEqual(dict_len, 1, "ABC and CAB should be in the same dictionary key.")

    def test_diff(self):
        arr = ["ABC", "CA"]
        dicts = anagramsq.sort_to_dicts(arr)
        dict_len = len(dicts)
        self.assertEqual(dict_len, 1, "ABC and CAB should be in different dictionary key.")




if __name__ == '__main__':
    unittest.main()