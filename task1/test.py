import unittest
from Utils import find_number_of_all_sentences , find_number_of_all_non_dec_sentences, find_average_len_of_sentences, find_average_len_of_words, find_top_n_gramms

class T(unittest.TestCase):
    def test_sentence_counter(self):
        self.assertEqual(find_number_of_all_sentences("Hello Mr. Djon. My name is Sam!"),2)
        self.assertEqual(find_number_of_all_sentences(""),0)
        self.assertEqual(find_number_of_all_sentences("What should I do now... I want to know! It is scared me."),3)

    def test_nondeclarative_counter(self):
        self.assertEqual(find_number_of_all_non_dec_sentences("Do you know the way? Yes, of course!"), 2)
        self.assertEqual(find_number_of_all_non_dec_sentences("Hello, my name is Nikita. I like do nothing."), 0)
        self.assertEqual(find_number_of_all_non_dec_sentences("Are you happy now? Because I am dying..."), 1)
    
    def test_average_sentence_length(self):
        self.assertEqual(find_average_len_of_sentences("Hello dear."), 9)
        self.assertEqual(find_average_len_of_sentences("Hello my world. I love you!"), 10)
        self.assertEqual(find_average_len_of_sentences("Do you wanna see a trick? I am gonna show you. It is bounced."), 15)
    
    def test_average_word_length(self):
        self.assertEqual(find_average_len_of_words("Hello."), 0.2)
        self.assertEqual(find_average_len_of_words("I want to know your nam."), 0.3333333333333333)
        self.assertEqual(find_average_len_of_words("If everything okay, it is okay?"), 0.25)

    def test_n_grams(self):
        self.assertEqual(find_top_n_gramms("Will come calling out.", 3, 2), [('ll', 2), ('Wi', 1), ('il', 1)])
        self.assertEqual(find_top_n_gramms("Nothing ever comes without a consequence or cost, tell me."), 
                         [('Noth', 1), ('othi', 1), ('thin', 1), ('hing', 1), ('ever', 1), ('come', 1), ('omes', 1), ('with', 1), ('itho', 1), ('thou', 1)])
        self.assertEqual(find_top_n_gramms("Rather be the hunter than the prey.", 7, 1), [('e', 6), ('t', 5), ('h', 5), ('r', 3), ('a', 2), ('n', 2), ('R', 1)])


if __name__ == '__main__':
    unittest.main()