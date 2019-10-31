palabras = [line.rstrip() for line in open("jugadores.txt")]
jugadoresconpuntaje=[]
puntaje=[]
nombre=[]
jugadoresconpuntajeciclo=[]

for palabra in range(len(palabras)):
    jugadoresconpuntajeciclo.append(palabras[palabra].split())

""" for jugador in range(len(jugadoresconpuntajeciclo)):
    puntaje.append(jugadoresconpuntajeciclo[jugador][1].split())
    nombre.append(jugadoresconpuntajeciclo[jugador][0].split())

for jugadorpartido in range(len(nombre)):
    print(nombre[jugadorpartido][0])
    print(puntaje[jugadorpartido][0])"""

archivojugadores=open("jugadores2.txt","r+")
for jugadorpartido in range(len(jugadoresconpuntajeciclo)):
    """ print(nombre[jugadorpartido][0])
    print(puntaje[jugadorpartido][0]) """
    if jugadorpartido==0:
        archivojugadores.write(jugadoresconpuntajeciclo[jugadorpartido][0]+"\t"+jugadoresconpuntajeciclo[jugadorpartido][1])
    else:
        archivojugadores.write("\n"+jugadoresconpuntajeciclo[jugadorpartido][0]+"\t"+jugadoresconpuntajeciclo[jugadorpartido][1])
    print("ok") 

print(jugadoresconpuntajeciclo[0][0])
""" print(puntaje[0][0])
print(nombre[0][0]) """
