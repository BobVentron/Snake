from qtido import * 

#affichage du serpant
def serpantgeneration(f,co):
    couleur(f,0,0,0.8)
    for e in co:
        disque(f,e[0]+20,e[1]+20,15)

#gestion du deplacement du serpant quand le joueur a apuyer sur une touche
def serpantdeplacement(f,co,direction,d):
    if direction == "top": 
        new_tete = [[(int(co[0][0])),(int(co[0][1])-40)]]
        d = "top"
        co.pop()
    elif direction == "bot": 
        new_tete = [[(int(co[0][0])),(int(co[0][1])+40)]]
        d = "bot"
        co.pop()
    elif direction == "left": 
        new_tete = [[(int(co[0][0])-40),(int(co[0][1]))]]
        d = "left"
        co.pop()
    elif direction == "right":
        new_tete = [[(int(co[0][0])+40),(int(co[0][1]))]]
        d = "right"
        co.pop()
    else :
        new_tete = [(serpantdeplacement(f, co, d,d))[0][0]]

    new_serpant = new_tete

    for e in co: 
        new_serpant.append(e)

    return [new_serpant, d]

#gestion de l'agrandissement du serpant quand ce dernier a mangé une pomme 
def serpantagrandi(f,co,direction) :
    if direction == "top": 
        new_tete = [[(int(co[0][0])),(int(co[0][1])-40)]]
    elif direction == "bot": 
        new_tete = [[(int(co[0][0])),(int(co[0][1])+40)]]
    elif direction == "left": 
        new_tete = [[(int(co[0][0])-40),(int(co[0][1]))]]
    elif direction == "right":
        new_tete = [[(int(co[0][0])+40),(int(co[0][1]))]]

    new_serpant = new_tete

    for e in co: 
        new_serpant.append(e)

    return [new_serpant, direction]