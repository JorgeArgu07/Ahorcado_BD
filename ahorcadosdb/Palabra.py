import random


class Palabra:



    def llenararchivo(self):
        listapalabras = []
        archivo = open('palabras1.txt', 'r')
        for linea in archivo.readlines():
            listapalabras.append(linea[:-1])
        archivo.close()
        archivo2 = open("palabras2.txt", "w")
        for linea in range(len(listapalabras)):
            archivo2.write(listapalabras[linea] + '\n')
        archivo2.close()
        return listapalabras


    def obtenerpalabras(self):
        listapalabras = []
        archivo = open('palabras2.txt', 'r')
        for linea in archivo.readlines():
            listapalabras.append(linea[:-1])
        archivo.close()

        return listapalabras

    def agregarpalabra(self, palabra):
        listapalabranueva = []
        for pal in self.llenararchivo():
            listapalabranueva.append(pal)
        listapalabranueva.append(palabra)
        archivo = open("palabras1.txt", "w")
        for linea in range(len(listapalabranueva)):
            archivo.write(listapalabranueva[linea] + '\n')
        archivo.close()
        print("Palabra añadida")


    def obtenerarreglopalabra(self):
        palabras = self.obtenerpalabras()
        palabra = random.choice(palabras)
        palabras.remove(palabra)

        archivo2 = open("palabras2.txt", "w")
        for linea in range(len(palabras)):
            archivo2.write(palabras[linea] + '\n')
        archivo2.close()

        splitted = []

        for char in palabra:
            splitted.append(char)
        return splitted

# var=Palabra()
#
# var.llenararchivo()
# var.obtenerpalabras()
# var.obtenerarreglopalabra()
