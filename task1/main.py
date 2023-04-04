import re
from CONSTS import SHORTS

def read_file():
    with open("InputTestText","r+") as f:
        str = f.read()
        return str

def check_exceptions(word) -> bool:
    
    for trap in SHORTS:
        if word == trap:
            return False
    return True

def stat_of_text(input):

    number_of_all_sentences = 0
    number_of_non_declarative_sentences = 0
    len_of_current_sentence = 0
    number_of_words = 0
    full_number_of_words = 0
    full_len_of_text = 0
    average_len_str = ''
    good_word = True

    result = re.findall(r'(([0-9]*[a-zA-Z\']+[0-9]*[a-zA-Z\']*[0-9]*)(\.\.\.|!|\?|\.)?)', input, flags=0)

    for word in result:   
        len_of_current_sentence += len(word[1])
        number_of_words += 1

        if word[2] != '':

            good_word = check_exceptions(word[1])

            if good_word:

                number_of_all_sentences += 1
                average_len_str += f"In {number_of_all_sentences} sentence average len of words is {len_of_current_sentence/number_of_words}\n"
                full_number_of_words += number_of_words
                full_len_of_text += len_of_current_sentence
                number_of_words = 0
                len_of_current_sentence = 0
                
                if word[2] != '.' and word[2] != '...':
                    number_of_non_declarative_sentences += 1
    
    print(f"Number of all sentences is {number_of_all_sentences}")
    print(f"Number of all non-declarative sentences is {number_of_non_declarative_sentences}")
    print(f"Average length of the sentence in characters:\n{average_len_str}")
    print(f"Average length of the word in the text in characters is {full_len_of_text/full_number_of_words}")

if __name__ == "__main__":
    
    stat_of_text(read_file())
