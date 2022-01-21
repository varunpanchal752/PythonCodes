import random as rdm  
  
name1 = input("Enter your NAME ? ")  
  
print("Welcome ", name1)  
   
words = ['Dumbledore', 'Aircraft', 'India', 'Code',  
         'Cpp', 'Python', 'Baseball', 'Soccer',  
         'Compiler', 'Bike', 'Car', 'Bus']  

word = rdm.choice(words)  
print ("Please guess the characters: ")  
guesses = ''  
   
turns = 10  
while turns > 0:  
    failed = 0  
    for char in word:  
        if char in guesses:  
            print(char)  
        else:  
            print("_")  
            failed += 1  
    if failed == 0:  
        print("User Win")  
        print("The correct word is: ", word)  
        break  
    guess = input("Guess another character:")  
    guesses += guess  
    if guess not in word:  
        turns -= 1  
        print("Wrong Guess")  
        print("You have ", + turns, 'more guesses ')  
        if turns == 0:  
            print("User Loose")  
