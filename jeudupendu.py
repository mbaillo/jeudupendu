from string import ascii_lowercase
from mots import get_random_word

def get_num_attempts():
    while True:
        num_attempts=input( 'Combien de tentatives de jeu incorrectes souhaitez-vous ?[1-25]')
        try :
            num_attempts=int(num_attempts)
            if 1<=num_attempts<=25:
                return num_attempts
            else:
                print('{0} n''est pas compris entre 1 et 25'.format(num_attempts))
        except ValueError:
                print('{0} n''est pas compris entre 1 et 25'.format(num_attempts))

def get_min_word_length():
    while True :
        min_word_length=input('Quelle longueur de mot minimale souhaitez-vous ?[4-16]')
        try :
            min_word_length=int(min_word_length)
            if 4<=min_word_length<=16:
                return min_word_length
            else:
                  print('{0} n''est pas compris entre 4 et 16'.format(min_word_length))
        except ValueError:
                print('{0} n''est pas compris entre 4 et 16'.format(min_word_length))


def get_display_word(word, idxs):
    if len(word) != len(idxs):
        raise ValueError('La longueur du mot et son index ne sont pas identiques')
    displayed_word= ''.join([letter if idxs[i] else '*' for i,
         letter in enumerate(word)])
    return displayed_word.strip()

def get_next_letter(remaining_letters):
    if len(remaining_letters)==0:
        raise ValueError('Il ne reste plus de lettres a jouer')

    while True:
        next_letter =input('Choisissez votre nouvelle lettre:').lower()
        if len(next_letter) !=1:
            print('{0} n"est pas une lettre seule'.format(next_letter))
        elif next_letter not in ascii_lowercase :
            print('{0} n"est pas une lettre seule'.format(next_letter))

        elif next_letter not in remaining_letters :
            print('{0} n"est pas une lettre seule'.format(next_letter))
        else:
            remaining_letters.remove(next_letter)
            return next_letter


def play_jeudupendu() :
    print('Demarrage du jeu...')
    nom = input("Entrez votre prenom: ")
    attempts_remaining=get_num_attempts()
    min_word_length=get_min_word_length()
    print('Choix d''un mot...')
    word=get_random_word(min_word_length)
    print()

    idxs = [letter not in ascii_lowercase for letter in word]
    remaining_letters=set(ascii_lowercase)
    wrong_letters=[]
    word_solved=False
    while attempts_remaining> 0 and not word_solved :
        print('Mot: {0}'.format(get_display_word(word, idxs)))
        print('Tentatives restantes : {0}'.format(attempts_remaining))
        print('Tentatives passées : {0}'.format(' '.join(wrong_letters)))
        next_letter=get_next_letter(remaining_letters)
        if next_letter in word :
            print('{0} figure bien dans le mot !'.format(next_letter))
            for i in range(len(word)):
                if word[i]==next_letter:
                    idxs[i]=True
        else :
            print('{0} ne fais pas partie du mot !'.format(next_letter))
            attempts_remaining-=1
            wrong_letters.append(next_letter)
        if False not in idxs:
            word_solved=True
            print()

    print('Le mot secret est : {0}'.format(word))
    if word_solved:
        print('Vous avez gagné ' + nom + ', Felicitations !!!')
    else:
        print( nom + ',  tu feras mieux la prochaine fois peut-etre :) ')
    
    try_again=input('Voulez vous jouer ?[oui/Oui]')
    return try_again.lower()=='oui'

if __name__== '__main__' :
   while play_jeudupendu():
           print()




            



