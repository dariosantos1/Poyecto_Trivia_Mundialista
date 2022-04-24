# Proyecto Trivia Mundialista

# Juego en donde por consola el programa hace preguntas a jugadores, los cuales deberán
# elegir por multiple choice (4 posibles respuestas por pregunta). Al finalizar gana
# el jugador con más respuesta acertadas.
# Mínimo el programa debe soportar 2 jugadores.

# Entrada del sistema
# El programa recibe un archivo “csv” en donde se colocará las preguntas
# del juego, las 4 posibles respuestas y la en cada caso cuál es la
# respuesta correcta (número del 1 al 4).
# El archivo consta de una fila por pregunta, 6 columnas por fila
# (pregunta, 4 respuestas, respuesta correcta).
# Puede agregarse si se desea más detalles como categorías o cualquier
# cosa que el alumno crea que puede sumar al programa.

# Salida del sistema
# Al finalizar el programa se deberá presentar los resultados de cuántas
# preguntas correctas realizó cada jugador y el ganador del juego, dando
# un puntaje final a cada uno.
# Se debe grabar en un archivo el ganador del juego con el puntaje
# alcanzado a fin de tener una tabla de ganadores históricos.

import csv
import os #sirve para la funcion de limpiar la pantalla de la consola
csvfile = open("preguntas.csv")
data = list(csv.DictReader(csvfile))
csvfile.close()

def borrar_consola (): # Limpia la pantalla de la consola
    os.system("cls" if os.name == "nt" else "clear")

def grabar_puntaje (nombre, puntaje) : # Crea un archivo csv con el puntaje historico

    csvfile = open('puntajes.csv', 'a', newline='') # Abrir archivo para escritura
    header = ['Nombre', 'Puntaje'] # Detalla los nombres de las columnas
    writer = csv.DictWriter(csvfile, fieldnames=header) # Crear el objeto para escribir las lineas de archivo basado en los nombres de las columnas
    fila = {"Nombre": nombre, "Puntaje" : puntaje}
    writer.writerow(fila)
    csvfile.close()

def ganadores_historicos () : # Consulta en el archivo "puntajes.csv" todos los ganadores historicos de la trivia
    csvfile = open ("puntajes.csv")
    data = list (csv.DictReader(csvfile))
    cantidad_filas = len(data)
    print ("Este Son Los Ganadores Históricos De La Trivia")
    for i in range (cantidad_filas) :
        filanombre = data [i].get("Nombre")
        filapuntaje = data [i].get("Puntaje")
        print (filanombre ,"Con un puntaje de",filapuntaje,"aciertos")
    csvfile.close ()


def preguntar_1_jugador () : #Recorre todas las preguntas cargadas en el archivo preguntas para la opción de 1 jugador.csv
    puntaje_jugador = 0
    cantidad_preguntas = len(data)
    for i in range (cantidad_preguntas) :
        row = data[i] 
        pregunta = data[i].get("Pregunta")
        respuesta_1 = data[i].get("Respuesta_1")
        respuesta_2 = data[i].get("Respuesta_2")
        respuesta_3 = data[i].get("Respuesta_3")
        respuesta_4 = data[i].get("Respuesta_4")
        respuesta_correcta = data[i].get("Respuesta_correcta")
        
        try :
            print ("Pregunta para",jugador1)
            print (pregunta)
            print ("1 :", respuesta_1)
            print ("2 :", respuesta_2)
            print ("3 :", respuesta_3)
            print ("4 :", respuesta_4)
            respuesta_usuario = input("Ingrese su respuesta : ")
            if respuesta_usuario == respuesta_correcta :
                borrar_consola ()
                print ("Su respuesta fue correcta")
                puntaje_jugador = puntaje_jugador + 1
                
            else :
                borrar_consola ()
                print ("Su respuesta fue incorrecta")
                
    
        except :
                print ("error")
    print ("La trivia a finalizado, su puntaje final es de",puntaje_jugador,"aciertos sobre" ,cantidad_preguntas)
    grabar_puntaje (jugador1,puntaje_jugador)

    

def preguntar_2_jugadores () : #Recorre todas las preguntas cargadas en el archivo preguntas para la opcion de 2 jugadores.csv
    puntaje_jugador_1 = 0
    puntaje_jugador_2 = 0
    cantidad_preguntas = len(data)
    for i in range (cantidad_preguntas) :
        row = data[i] 
        if i % 2 == 0: # Esto preguntara a un jugaror los renglones pares y al otro los impares

            pregunta = data[i].get("Pregunta")
            respuesta_1 = data[i].get("Respuesta_1")
            respuesta_2 = data[i].get("Respuesta_2")
            respuesta_3 = data[i].get("Respuesta_3")
            respuesta_4 = data[i].get("Respuesta_4")
            respuesta_correcta = data[i].get("Respuesta_correcta")

            print ("Pregunta para",jugador1)
            print (pregunta)
            print ("1 :", respuesta_1)
            print ("2 :", respuesta_2)
            print ("3 :", respuesta_3)
            print ("4 :", respuesta_4)
            respuesta_usuario1 = input("Ingrese su respuesta : ")
            if respuesta_usuario1 == respuesta_correcta :
                borrar_consola ()
                print ("Su respuesta fue correcta")
                puntaje_jugador_1 = puntaje_jugador_1 + 1
                
            else :
                borrar_consola ()
                print ("Su respuesta fue incorrecta")
        else :
            pregunta = data[i].get("Pregunta")
            respuesta_1 = data[i].get("Respuesta_1")
            respuesta_2 = data[i].get("Respuesta_2")
            respuesta_3 = data[i].get("Respuesta_3")
            respuesta_4 = data[i].get("Respuesta_4")
            respuesta_correcta = data[i].get("Respuesta_correcta")
        
            print ("Pregunta para",jugador2)
            print (pregunta)
            print ("1 :", respuesta_1)
            print ("2 :", respuesta_2)
            print ("3 :", respuesta_3)
            print ("4 :", respuesta_4)
            respuesta_usuario2 = input("Ingrese su respuesta : ")
            if respuesta_usuario2 == respuesta_correcta :
                borrar_consola ()
                print ("Su respuesta fue correcta")
                puntaje_jugador_2 = puntaje_jugador_2 + 1
                
            else :
                borrar_consola ()
                print ("Su respuesta fue incorrecta")
                       
    if puntaje_jugador_1 > puntaje_jugador_2 :
        print ("La trivia a finalizado, el ganador de este duelo es",jugador1,"con un puntaje final de",puntaje_jugador_1,"aciertos")
        print ("Quedando como cebollita subcampeón",jugador2, "con un puntaje de", puntaje_jugador_2, "aciertos")
        grabar_puntaje (jugador1, puntaje_jugador_1)
    else :
        print ("La trivia a finalizado, el ganado de este duelo es ", jugador2, "con un puntaje final de",puntaje_jugador_2)
        print ("Quedando como cebollita subcampeón ", jugador1, "con un puntaje de", puntaje_jugador_1, "aciertos")
        grabar_puntaje (jugador2, puntaje_jugador_2)
    
        
       
    



  



if __name__ == "__main__":
    
    print ("Bienvenido a la trivia mundialista")
    print ("Ingrese el número de opción que necesita ejecutar :")
    print ("1 : Un solo jugador")
    print ("2 : Dos jugadores")
    print ("3 : Ver puntajes historicos")

    
    numero = input()
    
    if numero == "1" :
        jugador1 = input("Ingrese el nombre del Jugador : ")
        print ("Bienvenido", jugador1, "que comience el juego")
        preguntar_1_jugador () # traigo la funcion creada para preguntar a un solo jugador
        
        
        
    elif numero == "2" :
        jugador1 = input("Ingrese el nombre del Jugador 1 : ")
        jugador2 = input ("ingrese el nombre del jugador 2 : ")
        print ("Bienvenidos", jugador1, "y",jugador2,"al juego")
        preguntar_2_jugadores () # traigo la funcion creada para preguntar a dos jugadores

    elif numero == "3" :
        ganadores_historicos () # traigo la funcion creada para imprimir en pantalla el archivo csv de los ganadores historicos
    else :
        print ("No se marcó una opción valida")
    
    

            
    


    
    













