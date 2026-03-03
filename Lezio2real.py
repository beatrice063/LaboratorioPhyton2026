'''
#
# File: HelloWorld.py
#
# Author: E.Romelli, D.Tavagnacco
#
# Date: 2026/03/03
#
# Version: 1.0
#
# Description: My First Project Program to print "Hello, World!".
#

print('Hello, World!')
'''


import turtle               # Importo modulo turtle

window = turtle.Screen()    # Creo una finestra dove lavorare
raffaello = turtle.Turtle() # Creo una tartaruga e la assegno alla variabile "raffaello"

raffaello.color('purple')

#for i in range(0, 4, 1):
for i in ['red', 'blue', 'purple', 'orange']:
  
    raffaello.color(i)
    
    raffaello.forward(50)       # Dico a "raffaello" di andare avanti di 50 passi
    raffaello.left(90)          # Dico a "raffaello" di girare a sinistra di 90 gradi
#raffaello.forward(50)       # Dico a "raffaello" di andare avanti di 30 passi
#raffaello.left(90)
#raffaello.forward(50)
#raffaello.left(90)
#raffaello.forward(50)
#raffaello.left(90)

leonardo = turtle.Turtle()
leonardo.color('blue')

leonardo.forward(50)
leonardo.left(120)
leonardo.forward(50)
leonardo.left(120)
leonardo.forward(50)
leonardo.left(120)

window.mainloop()           # Attende che l'utente chiuda la finestra di gioco o fermi il programma
