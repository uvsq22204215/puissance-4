testttt 
ramdom.randit pour choisir le 1er joueur
#définir colonne et ligne
from tkinter import*
 
from random import*
 
##création d'une fenêtre
fen=Tk()
fen.title("Puissance 4")
 
##création du canevas
can=Canvas(fen,width=710, heigh=610, bg="blue")
can.pack()
 
##fonction qui permet d'alterner les couleurs à chaque clique grâce à "couleurs.reverse()"
couleurs=[('red',1),('yellow',2)]
def player(event):
    Aléatoire=randint(1,2)
    if Aléatoire==1:
        player='red'
    else:
        player='yellow'
couleurs.reverse()
 
 
##fonction qui détecte le clique et éxécute la fonction "mouvement"
def detec_clic(event):
    x , y = event.x, event.y
    command=mouvement
 
can.bind("<Button-1>", detec_clic,player)
 
##fonction qui fait apparître un pion à la case cliquéé
def mouvement(event):
    x,y, = event.x, event.y
    if detec_clic >0 and detec_clic <700 :
        print("d'accord")
##        can.create_oval(event.x, event.y,fill="player")
    else:
        print("oups, il semblerait qu'il y'ai une erreur")
    command=tableur
 
 
 
 
 
 
##création de la grille
x=00
y=00
def grille():
    can.delete(all)
    global x, y
for i in range(6):
    for j in range(7):
        can.create_oval(x,y,x+100,y+100,fill='white')
 
        x=x+100
    y=y+100
    x=00
 
 
##compteur_pions_réunis=0
##compteur_pion_rouge=0
##compteur_pion_jaune=0
## if compeur_pions_réunis>=42:
##    print("match nul")
 
##liste contenant chacun des 42 cercles ainsi que ses coordonnés
cercles={1:(0,0,100,100),
         2:(0,100,100,200),
         3:(0,200,100,300),
         4:(0,300,100,400),
         5:(0,400,100,500),
         6:(0,500,100,600),
         7:(100,0,200,100),
         8:(100,100,200,200),
         9:(100,200,200,300),
         10:(100,300,200,400),
         11:(100,400,200,500),
         12:(100,500,200,600),
         13:(200,0,300,100),
         14:(200,100,300,200),
         15:(200,200,300,300),
         16:(200,300,300,400),
         17:(200,400,300,500),
         18:(200,500,300,600),
         19:(300,0,400,100),
         20:(300,100,400,200),
         21:(300,200,400,300),
         22:(300,300,400,400),
         23:(300,400,400,500),
         24:(300,500,400,600),
         25:(400,0,500,100),
         26:(400,100,500,200),
         27:(400,200,500,300),
         28:(400,300,500,400),
         29:(400,400,500,500),
         30:(400,500,500,600),
         31:(500,0,600,100),
         32:(500,100,600,200),
         33:(500,200,600,300),
         34:(500,300,600,400),
         35:(500,400,600,500),
         36:(500,500,600,600),
         37:(600,0,700,100),
         38:(600,100,700,200),
         39:(600,200,700,300),
         40:(600,300,700,400),
         41:(600,400,700,500),
         42:(600,500,700,600)}
 
 
##Liste qui représente le tableau, le but est que le programme se "souvienne" des choix des joueurs
tableau=[   [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]]
 
def tableur():
 
 
def score():
    return (tableau)
 
fen.mainloop()