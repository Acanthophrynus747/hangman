import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear') #clear either the linux or windows way or linux way

try:
    while True:

        lives = 6
        word_selected = False
        word_array = [[],[]]
        display_array = []
        guessed_letters = ""

        word = list(input("input a word: "))
        clear() #no peeking

        for i in word:
            word_array[0].append(i) 
            word_array[1].append(0) #guessed correctly indicator
            display_array.append("_")

        while True:
            num_correct = 0
            total_correct = 0
            over = False
            display_str = ""
            
            guess = input("guess a letter: ")
                        
            for i in range(len(word_array[0])): #iterate through word
                if word_array[0][i] == guess:
                    word_array[1][i] = 1 #indicate letter guessed correctly
                    num_correct += 1
                    
            if num_correct == 0:
                clear()
                print("WRONG\n")           
                guessed_already = guess in guessed_letters
                if guessed_already == False:
                    lives -= 1
                print(f"Lives remaining: {lives}\n")
                if lives == 0:
                    over = True
                    
            guessed_letters += guess
            print(f"Guesses: {guessed_letters}\n")
                    
            for i in range(len(word_array[1])):
                if word_array[1][i] != 0:
                    total_correct += 1
                    display_array[i] = word_array[0][i]
                    
                if int(total_correct) == len(word_array[1]): #if num correctly guessed equals length of word'
                    over = True 
            
            for char in display_array:
                display_str += char

            print(display_str)
            
            if over == True: #when you lose
                if lives == 0: 
                    print("YOU LOSE")
                else:
                    print("YOU WIN")
                
                time.sleep(1)
                
                again = input("enter y to play again, or any other character to exit: ")
                if again == "y" or again == "Y":
                    clear()
                    break #break to beginning of game
                else:
                    clear()
                    print("goodbye")
                    time.sleep(1)
                    clear()
                    exit()
        
except KeyboardInterrupt:
    clear()
    exit()

