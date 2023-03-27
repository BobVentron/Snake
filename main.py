from qtido import * 
from time import sleep
from fond import fondf
from serpant import serpantgeneration, serpantdeplacement, serpantagrandi
from random import randrange

def principale():
    
    f = creer(800, 800)
    fondf(f)

    [x_pomme,y_pommme] = [600, 400]
    co_serpant = [[400,400],[360,400],[320,400],[280,400]]

    serpantgeneration(f,co_serpant)
    d = "right"
    while not est_fermee(f) : 

        effacer(f)
        fondf(f)
        serpantgeneration(f,co_serpant)
        couleur(f,0.9,0,0)
        disque(f,x_pomme+20,y_pommme+20,15)
            

        attendre_evenement(f,500)
        ev = dernier_evenement(f)

        top1 = 16777235
        bot1 = 16777237
        left1 = 16777234
        right1 = 16777236

        if co_serpant[0] == [x_pomme,y_pommme]:
            [co_serpant, d] = serpantagrandi(f, co_serpant, d)
            [x_pomme,y_pommme]= [(randrange(0, 20))*40, (randrange(0, 20))*40]
            
        



        if ev == top1: 
            [co_serpant, d] = serpantdeplacement(f, co_serpant, "top",d)
        elif ev == bot1: 
            [co_serpant, d] = serpantdeplacement(f, co_serpant, "bot",d)
        elif ev == left1: 
            [co_serpant, d] = serpantdeplacement(f, co_serpant, "left",d)
        elif ev == right1:
            [co_serpant, d] = serpantdeplacement(f, co_serpant, "right",d)
        else : 
            [co_serpant, d] = serpantdeplacement(f, co_serpant, None, d)

        

    attendre_fermeture(f)

principale()

