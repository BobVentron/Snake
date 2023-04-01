from qtido import * 
from time import sleep
from fond import fondf
from serpant import serpantgeneration, serpantdeplacement, serpantagrandi
from random import randrange

def principale():
    
    f = creer(1400, 800)

    play = 0
    
    while not est_fermee(f) : 

        if play == 1 :
            supprime_widgets(f)
            effacer(f)
            fondf(f)
            serpantgeneration(f,co_serpant)
            couleur(f,0.9,0,0)
            disque(f,x_pomme+20,y_pommme+20,15)
            ##score
            Tscore = "score :" +str(score)
            texte(f, 900, 50, 35, Tscore)   

        attendre_evenement(f,500)
        ev = dernier_evenement(f)
        if play == 3: 
            texte(f, 1000, 200, 35, "Perdue")
            
        if play == 0 or play == 3:
            ajouter_bouton(f, "play", 900, 300, 1300, 500, "Play")
            [x_pomme,y_pommme] = [600, 400]
            co_serpant = [[400,400],[360,400],[320,400],[280,400]]
            d = "right"
            score = 0
            play = 2
            fondf(f)
        if ev == "play":
            play = 1

        if play == 1 :
            top1 = 16777235
            bot1 = 16777237
            left1 = 16777234
            right1 = 16777236

            if co_serpant[0] == [x_pomme,y_pommme]:
                [co_serpant, d] = serpantagrandi(f, co_serpant, d)
                [x_pomme,y_pommme]= [(randrange(0, 20))*40, (randrange(0, 20))*40]
                score += 1
            
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

            (x, y) = co_serpant[0]
            ##sortie du cadre
            if x > 799 or y > 799 or x < 0 or y < 0:
                play = 3
                score = 0
                [x_pomme,y_pommme] = [600, 400]
                co_serpant = [[400,400],[360,400],[320,400],[280,400]]
                d = "right"
                effacer(f)

            ##mord la queue
            for e in range(1, len(co_serpant)):
                if co_serpant[e] == co_serpant[0]: 
                    play = 3
                    effacer(f)


    attendre_fermeture(f)

principale()