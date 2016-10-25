import unittest

from co_occurrence import *

class TestCoOccurrenceMethods(unittest.TestCase):

    def test_find_close_indices_sanity_check(self):
        index_list_1 = [1,3,5,9,10,100]
        index_list_2 = [2,4,6,25]
        d = 2
        expected_output = [(1,2),(3,2),(3,4),(5,4),(5,6)]
        actual_output = find_close_indices(index_list_1, index_list_2, d)
        self.assertEqual(expected_output, actual_output)

    def test_find_close_indices_list_1_empty(self):
        index_list_1 = [1,3,5]
        index_list_2 = []
        d = 2
        expected_output = []
        actual_output = find_close_indices(index_list_1, index_list_2, d)
        self.assertEqual(expected_output, actual_output)

    def test_find_close_indices_list_2_empty(self):
        index_list_1 = []
        index_list_2 = [2,4,6]
        d = 2
        expected_output = []
        actual_output = find_close_indices(index_list_1, index_list_2, d)
        self.assertEqual(expected_output, actual_output)

    def test_co_occurrence_sanity_check(self):
        s = 'I write this word2 sentence containing word1 and word2 to check whether the co-occurrence ' \
            'on word2 word1 are working properly or not'
        word1 = 'word1'
        word2 = 'word2'
        d = 2
        expected_output = [(6,8),(16,15)]
        actual_output = co_occurrence(s, word1, word2, d)
        self.assertEqual(expected_output, actual_output)
        actual_output_s_list = co_occurrence(s.split(' '), word1, word2, d)
        self.assertEqual(expected_output, actual_output_s_list)

    def test_get_context_around_phrase_sanity_check(self):
        s = 'x such as y z a such as b c'
        phrase = 'such as'
        expected_output = [(0, 3), (5, 8)]
        actual_output = get_context_around_phrase(s, phrase)
        self.assertEqual(expected_output, actual_output)


if __name__ == '__main__':
    unittest.main()