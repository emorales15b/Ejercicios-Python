def run():
    global cadena_resultado, usuario_letra_adivinar
    cadena_resultado = ""
    usuario_letra_adivinar = []

    def ahorcado():
        global cadena_resultado, usuario_letra_adivinar
        letra_adivinar = str(input('Escribe una letra: ')[0:1])
    
        #for para saber que no se repite la misma letra
        for verificar_letra_repetida in usuario_letra_adivinar:
            if verificar_letra_repetida == letra_adivinar:
                print("\nYa pusiste esta letra, intenta con otra \n")
                ahorcado()
        
        usuario_letra_adivinar.append(letra_adivinar)

        with open("./archivos/ahorcado.txt", "r", encoding="utf-8") as f:
            for line in f:
                nombre_adivinar = line
            
            #cuantos caracteres tiene la palabra a adivinar del txt
            longitud_nombre_adivinar = len(nombre_adivinar)
            bandera_adivinado = 0
            bandera_espacio_blanco = 0

            #for para obtener letra por letra del nombre del archivo txt
            for letra_nombre in nombre_adivinar:

                bandera_espacio_blanco = 0

                #for para obtener las letras que ha introducido el usuario
                for letra_usuario_letra_adivinar in usuario_letra_adivinar:

                    if letra_nombre == letra_usuario_letra_adivinar:
                        cadena_resultado = cadena_resultado+letra_usuario_letra_adivinar+" "
                        bandera_adivinado = bandera_adivinado +1
                        bandera_espacio_blanco = bandera_espacio_blanco+1

                if bandera_espacio_blanco == 0:
                    cadena_resultado = cadena_resultado+"__ "

            if bandera_adivinado == longitud_nombre_adivinar:
                print("adivinaste la palabra "+ nombre_adivinar)
                breakpoint
            else:
                print(cadena_resultado+"\n")
                cadena_resultado = ""
                ahorcado()

    ahorcado()


if __name__ == '__main__':
    run()
