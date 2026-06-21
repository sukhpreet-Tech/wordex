import random

while True:
    user_id=input("enter a user id :->")
    print("welcome",user_id)
    print("enjoy word guessing game ")
    print("LEVEL 1 [EASY]")

    while True :

        list=["apple","mango","table","screen","temple","green"]
        choose =random.choice(list)
    
        breaked="".join(random.sample(choose,len(choose)))
        print(breaked)
    
        guess=input("guess the word :->>")
        if guess==choose :
            print("well done ,great ",user_id) 
            break
    
        else:
            print("try again")
            print("better luck next time")
    break



while True:
    print("LEVEL 2 [MEDIUM]")
    while True:  
        answer=input("are you ready player?")
        if answer=="yes":
            print("great")
            break   
    
        else:
            print("get ready fast game is waiting for you")
    break


while True :
    print("lets continue game")
    
    while True:

        list2=["laptop","motarcar","television","homemade","basketball","gardan"]
        choose2 =random.choice(list2)
    
        breaked2="".join(random.sample(choose2,len(choose2)))
        print(breaked2)
    
        guess2=input("guess the word :->>")
        if guess2==choose2 :
            print("well done ,great ",user_id) 
            break
    
        else:
            print("try again")
        print("better luck next time")
    break

while True:
    print("LEVEL 3 [HARD]")
    while True:  
        answer2=input("are you ready player?")
        if answer2=="yes":
            print("great")
            break   
    
        else:
            print("get ready fast game is waiting for you")
    break


while True :
    print("lets continue game")
    
    while True:

        list3=["refridgerature","important","instruction","manufacture","punjabkings"]
        choose3 =random.choice(list2)
    
        breaked3="".join(random.sample(choose3,len(choose3)))
        print(breaked3)
    
        guess3=input("guess the word :->>")
        if guess3==choose3 :
            print("well done ,great ",user_id) 
            print("GAME FINISH")
            break
    
        else:
            print("try again")
        print("better luck next time")
    break