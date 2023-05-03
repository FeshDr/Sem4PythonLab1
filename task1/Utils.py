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

regex_pattertn = r"(([0-9]*[a-zA-Z\']+[0-9]*[a-zA-Z\']*[0-9]*)(\.\.\.|!|\?|\.)?(\"|\')?(\.\.\.|!|\?|\.)?)"

def find_number_of_all_sentences(input_str,  writer = True):

    number_of_all_sentences = 0

    result = re.findall(regex_pattertn, input_str, flags=0)

    for word in result:
        if word[2] != '':
            good_check = check_exceptions(word[1])
            if good_check:
                if word[3] != '':
                    if word[4] != '':
                        number_of_all_sentences += 1
                else:
                    number_of_all_sentences += 1
            else:
                #number_of_all_sentences += 1
                None
    
    if writer:
        print(f"Number of all sentences is {number_of_all_sentences}")

    return number_of_all_sentences
    
def find_number_of_all_non_dec_sentences(input_str):

    number_of_non_declarative_sentences = 0

    result = re.findall(regex_pattertn, input_str, flags=0)

    for word in result:
        if word[2] != '':
            #print(word[0])
            #print(word[1])
            #print(word[2])
            #print(word[3])
            good_check = check_exceptions(word[1])
            if good_check:
                if word[3] != '':
                    if word[4] != '':
                        if word[4] != '.' and word[4] != '...':
                            number_of_non_declarative_sentences += 1
                else:
                    if word[2] != '.' and word[2] != '...':
                        number_of_non_declarative_sentences += 1
            else:
                if word[2] != '.' and word[2] != '...':
                    number_of_non_declarative_sentencess += 1
    
    print(f"Number of all non-declarative sentences is {number_of_non_declarative_sentences}")

    return number_of_non_declarative_sentences

def get_len_of_all_text(input_str):

    lengs = 0

    result = re.findall(regex_pattertn, input_str, flags = 0)
    
    for word in result:
        lengs += len(word[1])

    return lengs

def find_average_len_of_sentences(input_str):
    sentences_number = find_number_of_all_sentences(input_str, False)
    lengs = get_len_of_all_text(input_str)

    print(f"Average length of the sentence in characters: {lengs/sentences_number}")

    return lengs/sentences_number

def find_average_len_of_words(input_str):

    result = re.findall(regex_pattertn, input_str)
    lengs = get_len_of_all_text(input_str)

    print(f"Average length of the word in the text in characters is {len(result)/lengs}")

    return len(result)/lengs

def find_top_n_gramms(input_str, K = 10, N = 4):

    result = re.findall(regex_pattertn, input_str, flags = 0)

    n_gramm_dict = {}

    for word in result:
        #print(word[1])
        if(len(word[1]) >= N):
            for i in range(0, len(word[1]) - N + 1):
                n_gramm_dict[word[1][i:i+N]] = n_gramm_dict.get(word[1][i:i+N],0) + 1

    n_gramm_dict_res = sorted(n_gramm_dict.items(), key = lambda x: x[1], reverse = True)[:K] 

    print(n_gramm_dict_res)
    return n_gramm_dict_res



def stat_of_text():

    validator = 1

    while(validator):
        get = input("Do you want to load default file? Y/N : ")
        if(get == "Y"):
            validator = 0
            input_str = read_file()
        elif(get == "N"):
            validator = 0
            input_str = input("Write text : ")
            if(input_str == "exit"):
                return None
        else:
            print("Wrong input")
    
    find_number_of_all_sentences(input_str)
    find_number_of_all_non_dec_sentences(input_str)
    find_average_len_of_sentences(input_str)
    find_average_len_of_words(input_str)

    print("Enter K and N for last task enter default or empty string (K = 10, N = 4)")
    K = input()
    if K == "default" or K == '':
        find_top_n_gramms(input_str)
    else:
        try:
            N = int(input())
            find_top_n_gramms(input_str, int(K), N)
        except:
            print("Epp good job wrong input, set default value")
            find_top_n_gramms(input_str)