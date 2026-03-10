
import turtle

"""
def disegna_quadrato(tartaruga, size):
  for i in range(4):
    tartaruga.forward(50)
    tartaruga.left(90)
    

def somma (a,b) :
  risultato = a + b
  return risultato
  
  
##########################################
    
    

window = turtle.Screen()               # istanza "window" di Screen
window.bgcolor("lightgreen")           # imposto lo stato della "window"
# window.title("Raffaello & Donatello")

raffaello = turtle.Turtle()            # Istanza di Turtle chiamata raffaello
raffaello.color("red")                 # attributi per lo stato di raffaello    
raffaello.pensize(5)

disegna_quadrato(raffaello, 50)

#raffaello.forward(50)                  # movimenti per disegnare quadrato
#raffaello.left(90)                     # con raffaello
#raffaello.forward(50)
#raffaello.left(90)
#raffaello.forward(50)
#raffaello.left(90)
#raffaello.forward(50)
#raffaello.left(90)

raffaello.right(180)                   # giro e sposto dall'origine raffaello
raffaello.forward(80)                  # 

def disegna_triangolo(tartaruga):
  for i in range(3):
    tartaruga.forward(80)
    tartaruga.left(120)


donatello = turtle.Turtle()            # Istanza di Turtle chiamata donatello
donatello.color("violet")              # attributi per lo stato di donatello

disegna_triangolo(donatello)

#donatello.forward(80)                  # movimenti per disegnare un triangolo
#donatello.left(120)                    # con donatello
#donatello.forward(80)
#donatello.left(120)
#donatello.forward(80)
#donatello.left(120)               


window.mainloop()                      # Attendo chiusura finestra di gioco o stop del programma
"""

def koch(t, order, size):
    """
       La tartaruga t disegna frattale Koch di 'order' and 'size'
       lasciando la tartaruga nella direzioni iniziale
    """

    if order == 0:          
        # caso base che termina la ricorsione
        t.forward(size)
    else:
        # caso ricorsivo (ordine 1) in cui disegna i 4 segmenti
        koch(t, order-1, size/3)  
        t.left(60)
        koch(t, order-1, size/3)
        t.right(120)
        koch(t, order-1, size/3)
        t.left(60)
        koch(t, order-1, size/3)
        ##
        
window = turtle.Screen()               # istanza "window" di Screen
window.bgcolor("lightgreen")           # imposto lo stato della "window"
# window.title("Raffaello & Donatello")

raffaello = turtle.Turtle()            # Istanza di Turtle chiamata raffaello
raffaello.color("red")                 # attributi per lo stato di raffaello    
raffaello.pensize(5)

koch(raffaello, 3, 200) 

window.mainloop()                      # Attendo chiusura finestra di gioco o stop del programma