import random
Man = ['''
  +---+
  |   |
      |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''']
word = random.choice(open("words.txt").read().split())
words=list(word)
blanks=list("_"*(len(word)))
used=[]
life=0
def output():
    print(Man[life])
    print("Word : ","".join(blanks).replace("_"," _ "),sep="")
    if(len(used)>0): print("Guesses : ",", ".join(used),sep="")

output()
while life < 6 :
    if "_" in blanks:
        guess=input("\nEnter a letter :   ").casefold()
        if guess not in used:
            used.append(guess)
            if guess in word:
                for i, j in enumerate(words):
                    if j == guess:                  
                        blanks[i]=guess
            else:
                life+=1
            output()              
        else:
            print(f"You have already used {guess}.\n")
    else:
        print('''\n\t
              +~~~~~~~~~~~~~~~~~~~~~~+
              |       YOU WON        |
              +~~~~~~~~~~~~~~~~~~~~~~+
              ''')
        exit()

print(f"You lost. The word was '{word}'.")
