from qtido import * 

#creation du damier qui sert de fond au jeu
def fondf(f): 
    for i in range(20):
        for j in range(20): 
            if (i+j) % 2 == 0:
                couleur(f,0,1,0)
            else : 
                couleur(f,0,0.9,0)
            rectangle(f,40*i,40*j,40*i+40,40*j+40)