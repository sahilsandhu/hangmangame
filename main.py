import random
def getwords():
    word_list=['Phone','charger','lead','mohit','shikha','sahil','sandhu']
    index=random.randint(0,len(word_list)-1)
    word=word_list[index]
    return word.upper()
def animation(tries):
    stages= [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]
def play(word):
    print("------------Welcome to the HANGMAN GAME-------------")
    print("RULES")
    print("1.Yoyu will get only 6 chances and you have to select in these chances only")
    choice=input("IF you want to play the game------ENTER -> 'Y'").upper()
    if choice=='Y':
        guessed_letter=[]
        chance=6
        guessed_word=[]
        guessed=False
        word_completion="_"*len(word)
        print(animation(chance))
        print(word_completion)
        while guessed is False and chance>0:
            guess=input("ENTER YOUR WORD").upper()
            if len(guess)==1 :
                if guess in guessed_letter:
                    print("STOP---this word is already choosen")
                elif guess not in word:
                    print("STOP----This Letter is not Present")
                    guessed_word.append(guess)
                    chance=chance-1
                else: 
                    print("KUDOS!!--- Letter is in the word")
                    
                    guessed_letter.append(guess)
                    word_in_list=list(word_completion)
                    index=[i for i, letter in enumerate(word)if letter==guess]
                    for indexes in index:
                        word_in_list[indexes]=guess
                    str(word_in_list)  
                    if "_" not in word_in_list:
                        guessed=True
                    
            elif len(guess)==len(word):
                if guess in guessed_word:
                    print("STOP----this word is already choosen")
                elif guess!=word:
                    print("STOP---this is not a word")
                    guessed_word.append(guess)
                    chance=chance-1
                else:
                    guessed=True
                    word_completion=word
                    
            else:
                print("SORRY CHOICE!!!!!!!! try Again")
            print(animation(chance))
            print(word_completion)
            print("\n")
        if guessed:
            print("'-------!!!!!!!Vous gagnez'!!!!!------")
            animation(chance)
        else:
            print("##Sorry,BETTER LUCK NEXT TIME, YOU LOSSE!!!, the word is ",word)
            
def main():
    word=getwords()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = getwords()
        play(word)


if __name__ == "__main__":
    main()       