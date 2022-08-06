import random
LISTEMOTS= 'listemots.txt'
def get_random_word(min_word_length) :
    pass
def get_random_word(min_word_length):
    words= []
    with open(LISTEMOTS, 'r') as f:
        for word in f:
            if '('or')' in word:
                continue
            word=word.strip().lower()
            if len(word)<min_word_length:
                continue
                words.append(word)
        return random.choice(words)
def get_random_word(min_word_length):
    num_words_processed=0
    curr_word=None
    with open(LISTEMOTS, 'r') as f:
        for word in f:
            if'(' in word or')' in word:
                    continue
            word=word.strip().lower()
            if len(word)<min_word_length:
                continue
            num_words_processed+=1
            if random.randint(1,num_words_processed)==1:
                        curr_word=word
    return curr_word
                    