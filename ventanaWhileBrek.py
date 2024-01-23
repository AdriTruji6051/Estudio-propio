import random
import turtle

#Crear la ventana
ventana = turtle.Screen()
ventana.bgcolor("White")
ventana.title("Carrera de caracoles")
ventana.setup(width=800,height=800)

#Crear los competidores
caracol1 = turtle.Turtle()
caracol1.shape("turtle")
caracol1.color("red")
caracol1.penup()
caracol1.goto(-300,100)

caracol2 = turtle.Turtle()
caracol2.shape("turtle")
caracol2.color("blue")
caracol2.penup()
caracol2.goto(-300,200)

meta = 300

# #Dibujar un cuadrado --------------- Usado en otro codigo, pero aqui pa que no se pierda xd

# for _ in range(6):
#     tortuga.forward(200) #Line size
#     tortuga.right(60) #Rotation degrees

#Dibujar una linea de meta
linea_meta = turtle.Turtle()
linea_meta.penup()
linea_meta.goto(meta, 300)
linea_meta.pendown()
linea_meta.goto(meta, -100)
linea_meta.hideturtle()

while True:
    avance_caracol1 = random.randint(1,20)
    avance_caracol2 = random.randint(1,20)
    
    if avance_caracol1 % 2 == 0 or avance_caracol2 % 2 == 0:
        continue
    
    caracol1.forward(avance_caracol1)
    caracol2.forward(avance_caracol2)
    
    print(f"El caracol 1 avanza {avance_caracol1}, para un total de: {caracol1.xcor()}")
    print(f"El caracol 2 avanza {avance_caracol2}, para un total de: {caracol2.xcor()}")
    
    if caracol1.xcor() >= meta or caracol2.xcor() >= meta:
        break
    

if caracol1.xcor() > caracol2.xcor():
    print("El caracol rojo ha ganado")
elif caracol2.xcor() > caracol1.xcor():
    print("El caracol azul ha ganado")
else:
    print("Empate macuin")    
    
ventana.mainloop()
    