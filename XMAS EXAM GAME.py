print('(Choose A for singleplayer as B and C not done)')
print('-----------------------------------------------------------------')
 
while True:
    gamechoice = input("Do you want to play : \n A) Singleplayer. B) Multiplayer. C) Against AI. - [A/B/C]? : ")
    
    print('-----------------------------------------------------------------')
    
    if gamechoice == 'A':
        input('Player 1 Name: ')
    elif gamechoice == 'B':
        input('Player 1 Name: ')
        input('Player 2 Name: ')
    elif gamechoice == 'C':
        input('Player 1 Name: ')
        
    print('-----------------------------------------------------------------')
    break

if gamechoice == 'A':
    choice1 = input('Welcome to the quiz. Please select your genre: \n 1) Music. 2) Sport. 3) Geography. 4) History. - [1/2/3/4]? : ')
elif gamechoice == 'B':
    choice2 = input('Welcome to the quiz. Please select your genre: \n 1) Music. 2) Sport. 3) Geography. 4) History. - [4/5/6/7]? : ')
elif gamechoice == 'C':
    choice3 = input('Welcome to the quiz. Please select the genre the AI will complete: \n 1) Music. 2) Sport. 3) Geography. 4) History. - [1/2/3/4]? : ')
    
    print('-----------------------------------------------------------------')
    

if choice1 == '1':
    print('-----------------------------------------------------------------')
    print('Question 1: ')
    ans1 = input('Who sings Wonderwall?: \n a) Blur. b) Oasis. c) One Direction. - [a/b/c]?: ')
    
    print('-----------------------------------------------------------------')
    print('Question 2: ')
    ans2 = input('Who sings Piano Man?: \n d) Billy Joel. e) Elton John. f) Ed Sheeran. - [d/e/f]?: ')
    
    print('-----------------------------------------------------------------')
    print('Question 3: ')
    ans3 = input('Who sings Billie Jean?: \n g) Michael Jackson. h) Michael Jordan. i) Michael Flatley. - [g/h/i]?: ')
    
if choice1 == '2':
    print('-----------------------------------------------------------------')
    print('Question 1: ')
    ans1 = input('Who won the 2018 FIFA World Cup?: \n a) Argentina. b) France. c) Germany. - [a/b/c]?: ')
    
    print('-----------------------------------------------------------------')
    print('Question 2: ')
    ans2 = input('How many points is a goal worth in hurling?: \n d) One. e) Three. f) Five. - [d/e/f]?: ')
    
    print('-----------------------------------------------------------------')
    print('Question 3: ')
    ans3 = input('What sport does Michael Van-Gerwen play?: \n g) Darts. h) Soccer. i) Rugby. - [g/h/i]?: ')  
    
if choice1 == '3':
    print('-----------------------------------------------------------------')
    print('Question 1: ')
    ans1 = input('What is the capital of Thailand?: \n a) Lisbon. b) Hong Kong. c) Bangkok. - [a/b/c]?: ')
    
    print('-----------------------------------------------------------------')
    print('Question 2: ')
    ans2 = input('Which of these is not a type of rock?: \n d) Morphious. e) Sedimentary. f) Igneous. - [d/e/f]?: ')
    
    print('-----------------------------------------------------------------')
    print('Question 3: ')
    ans3 = input('On what continent is the largest desert in the world?: \n g) Antarctica. h) Africa. i) Asia. - [g/h/i]?: ')  
  
if choice1 == '4':
    print('-----------------------------------------------------------------')
    print('Question 1: ')
    ans1 = input('When did WW1 begin?: \n a) 1918. b) 1922. c) 1914. - [a/b/c]?: ')
    
    print('-----------------------------------------------------------------')
    print('Question 2: ')
    ans2 = input('Which astronaut first landed on the moon?: \n d) Neil Armstrong. e) Lance Armstrong. f) Buzz Lightyear. - [d/e/f]?: ')
    
    print('-----------------------------------------------------------------')
    print('Question 3: ')
    ans3 = input('Where was the Good Friday Agreement signed?: \n g) Dublin. h) London. i) Belfast. - [g/h/i]?: ')
    
print('-----------------------------------------------------------------')
print('Congrats, the quiz is complete. Further options and features will be added soon. Thank you!')
    

    