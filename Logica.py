from Array_Fichas import ArrayFichas
from Tablero import Tablero
from Fichas import Fichas

class Logica:

    def __init__(self):
        self.array_caminos = []
        self.array_aldeas = []


    def contiene_camino(self, ficha):
        return ArrayFichas().type(ficha) in [15, 16, 17, 18]

    def contiene_iglesia(self, ficha):
        return ArrayFichas().type(ficha) in [19]

    def contiene_iglesia_camino(self, ficha):
        return ArrayFichas().type(ficha) in [10]

    def contiene_aldea(self, ficha):
        return ArrayFichas().type(ficha) in [1, 2, 3, 4, 5, 6, 7]


    def contiene_camino_y_aldea(self, ficha):
        return ArrayFichas().type(ficha) in [8, 9, 11, 12, 14]


    def es_bifurcacion(self, ficha):
        return ArrayFichas().type(ficha) in [15, 16]


    def es_bifurcacion_y_aldea(self, ficha):
        return ArrayFichas().type(ficha) == 13


    def es_limite_camino(self, ficha):
        return ArrayFichas().type(ficha) in [8, 10, 13, 15, 16]


    def es_doble_limite_aldea(self,ficha):
        return ArrayFichas().type(ficha) in [5, 6]


    def que_ficha_es(self, ficha):
        if self.contiene_camino(ficha) and not self.es_bifurcacion(ficha):
            return "con_C"
        if self.es_doble_limite_aldea(ficha):
            return "con_DLA"
        if self.contiene_aldea(ficha):
            return "con_A"
        if self.contiene_camino_y_aldea(ficha):
            return "con_CA"
        if self.es_bifurcacion(ficha):
            return "con_B"
        if self.es_bifurcacion_y_aldea(ficha):
            return "con_BA"
        if self.contiene_iglesia(ficha):
            return "con_I"
        if self.contiene_iglesia_camino(ficha):
            return "con_CI"




    def dame_pos_contiguas(self, x, y):
        #Devuelve dos arrays con las posiciones de las fichas contiguas y sus direcciones
        pos_contiguas = [(x-1, y), (x+1, y), (x, y+1), (x, y-1)]
        lados = ["arriba", "abajo", "derecha", "izquierda"]
        return (pos_contiguas, lados)


    def dame_camino(self, pos):
        #Devuelve el camino dentro del array de todos los caminos
        #en el que se encuentre la posicion pasada como parametro
        for camino in self.array_caminos:
            if pos in camino:
                return camino #devolvemos el camino que contenga la posicion


    def dame_camino_valido_B(self, pos_B):
        #Si una de las fichas adyacentes resulta ser una bifurcacion, no podemos pedir
        #un camino que contenga esa posicion sin mas, necesitamos uno que contenga la
        #posicion de la bifurcacion y solo esa posicion
        caminos_con_B = []
        for camino in self.array_caminos:
            if pos_B in camino:
                caminos_con_B.append(camino) #nos quedamos con todos los caminos que contengan esa posicion

        for c in caminos_con_B:
            if len(c) == 1:
                return c  #elegimos el primero que contenga solo esa posicion y ninguna mas


    def dame_aldea(self, pos):
        #Devuelve la aldea dentro del array de todas las aldeas
        #en el que se encuentre la posicion pasada como parametro
        for aldea in self.array_aldeas:
            if pos in aldea:
                return aldea #devolvemos la aldea que contenga la posicion


    def dame_aldea_valida_DLA(self, pos): #Doble Limite Aldea
        #Si una de las fichas adyacentes resulta ser una aldea con doble limite de aldea,
        #no podemos pedir una aldea que contenga esa posicion sin mas, necesitamos una que
        #contenga la posicion de la ficha de doble limite y solo esa posicion
        aldeas_con_DLA = []
        for aldea in self.array_aldeas:
            if pos in aldea:
                aldeas_con_DLA.append(aldea) #nos quedamos con todas las aldeas que contengan esa posicion

        for a in aldeas_con_DLA:
            if len(a) == 1:
                return a  #elegimos la primera que contenga solo esa posicion y ninguna mas


    def continua_camino(self, tablero, pos, pos_contigua, lado): #lado: arriba,abajo,dcha,izda
        #Comprueba si la ficha que estamos colocando y una de las fichas contiguas
        #forman un mismo camino
        ficha_contigua = tablero.dame_ficha(pos_contigua)
        ficha_actual = tablero.dame_ficha(pos)
        response = False
        if lado == "arriba":
            if ficha_actual.territorio[1][1] == 'C': #comprobamos si en ese lado hay camino
                if ficha_actual.territorio[1][1] == ficha_contigua.territorio[2][1]: #si la ficha contigua no es vacia
                    response = True
        elif lado == "abajo":
            if ficha_actual.territorio[2][1] == 'C': #comprobamos si en ese lado hay camino
                if ficha_actual.territorio[2][1] == ficha_contigua.territorio[1][1]: #si la ficha contigua no es vacia
                    response = True
        elif lado == "derecha":
            if ficha_actual.territorio[3][1] == 'C': #comprobamos si en ese lado hay camino
                if ficha_actual.territorio[3][1] == ficha_contigua.territorio[4][1]: #si la ficha contigua no es vacia
                    response = True
        elif lado == "izquierda":
            if ficha_actual.territorio[4][1] == 'C': #comprobamos si en ese lado hay camino
                if ficha_actual.territorio[4][1] == ficha_contigua.territorio[3][1]: #si la ficha contigua no es vacia
                    response = True
        return response


    def continua_aldea(self, tablero, pos, pos_contigua, lado): #lado: arriba,abajo,dcha,izda
        #Comprueba si la ficha que estamos colocando y una de las fichas contiguas
        #forman una misma aldea
        ficha_contigua = tablero.dame_ficha(pos_contigua)
        ficha_actual = tablero.dame_ficha(pos)
        response = False
        if lado == "arriba":
            if ficha_actual.territorio[1][1] == 'A': #comprobamos si en ese lado hay aldea
                if ficha_actual.territorio[1][1] == ficha_contigua.territorio[2][1]: #si la ficha contigua no es vacia
                    response = True
        elif lado == "abajo":
            if ficha_actual.territorio[2][1] == 'A': #comprobamos si en ese lado hay aldea
                if ficha_actual.territorio[2][1] == ficha_contigua.territorio[1][1]: #si la ficha contigua no es vacia
                    response = True
        elif lado == "derecha":
            if ficha_actual.territorio[3][1] == 'A': #comprobamos si en ese lado hay aldea
                if ficha_actual.territorio[3][1] == ficha_contigua.territorio[4][1]: #si la ficha contigua no es vacia
                    response = True
        elif lado == "izquierda":
            if ficha_actual.territorio[4][1] == 'A': #comprobamos si en ese lado hay aldea
                if ficha_actual.territorio[4][1] == ficha_contigua.territorio[3][1]: #si la ficha contigua no es vacia
                    response = True
        return response


    def coloca_ficha_con_C(self, tablero, pos):
        #Busca si la ficha pertenece a algun camino existente
        #Si pertenece a un camino, incluye la posicion de la ficha en ese camino
        #Si pertenece a caminos inconexos, los une en un mismo camino
        #Si no pertence a ningun camino, crea un nuevo camino con la posicion de la ficha
        posiciones = [] #array en el que se iran agregrando las posiciones contiguas al camino
        pos_contiguas = self.dame_pos_contiguas(pos[0], pos[1])[0]
        lados = self.dame_pos_contiguas(pos[0], pos[1])[1]

        #Guardamos en posiciones las fichas adyacentes que continuen el camino
        for i in range(len(lados)):
            if self.continua_camino(tablero, pos, pos_contiguas[i], lados[i]): #si pertenece a un camino existente
                posiciones.append(pos_contiguas[i]) #nos quedamos con esa posicion

        if posiciones == []: #no pertenece a un camino existente
            self.array_caminos.append([pos])
        elif len(posiciones) == 2: #pertenece a dos caminos que estaban inconexos
            camino1 = self.dame_camino(posiciones[0])
            camino2 = self.dame_camino(posiciones[1])
            self.array_caminos.remove(camino1) #eliminamos los antiguos caminos
            self.array_caminos.remove(camino2)
            camino1.append(pos)
            for elem in camino2:
                camino1.append(elem)
            self.array_caminos.append(camino1) #agregamos el camino completo
        else: #pertence a un solo camino existente
            camino = self.dame_camino(posiciones[0]) #busco el camino al que pertenece
            self.array_caminos.remove(camino) #eliminamos el antiguo camino
            camino.append(pos)
            self.array_caminos.append(camino) #agregamos el camino completo


    def coloca_ficha_con_B(self, tablero, pos):
        #Si la ficha que hay que colocar contiene una bifurcacion:
        #Hay que incluirla en tantos caminos como ramas tenga la bifurcacion
        #Por cada lado, si es continuacion de camino agregaremos la ficha al camino correspondiente,
        #si no es continuacion crearemos un camino nuevo para esa posicion
        ficha_actual = tablero.dame_ficha(pos)
        pos_contiguas = self.dame_pos_contiguas(pos[0], pos[1])[0]
        lados = self.dame_pos_contiguas(pos[0], pos[1])[1]

        for i in range(1,5): #1 arriba, 2 abajo, 3 derecha, 4 izquierda
            if ficha_actual.territorio[i][1] == 'C': #comprobamos si en ese lado hay rama
                if self.continua_camino(tablero, pos, pos_contiguas[i-1], lados[i-1]): #si hay rama y continua un camino existente
                    if self.es_bifurcacion(tablero.dame_ficha(pos_contiguas[i-1])): #si la ficha adyacente tambien es bifurcacion
                        camino = self.dame_camino_valido_B(pos_contiguas[i-1])
                    else:
                        camino = self.dame_camino(pos_contiguas[i-1])
                    self.array_caminos.remove(camino)
                    camino.append(pos)
                    self.array_caminos.append(camino)
                else:
                    self.array_caminos.append([pos]) #si no continua creamos un nuevo camino



    def coloca_ficha_con_A(self, tablero, pos):
        #Busca si la ficha pertenece a alguna aldea existente
        #Si pertenece a una aldea, incluye la posicion de la ficha en esa aldea
        #Si pertenece a aldeas inconexas, las une en una misma aldea
        #Si no pertence a ninguna aldea, crea una nueva aldea con la posicion de la ficha
        posiciones = [] #array en el que se iran agregrando las posiciones contiguas a la aldea
        pos_contiguas = self.dame_pos_contiguas(pos[0], pos[1])[0]
        lados = self.dame_pos_contiguas(pos[0], pos[1])[1]

        #Guardamos en posiciones las fichas adyacentes que continuen la aldea
        for i in range(len(lados)):
            if self.continua_aldea(tablero, pos, pos_contiguas[i], lados[i]): #si pertenece a una aldea existente
                print pos_contiguas[i]
                print "continua"
                posiciones.append(pos_contiguas[i]) #nos quedamos con esa posicion

        if posiciones == []: #no pertenece a una aldea existente
            self.array_aldeas.append([pos])
        elif len(posiciones) == 2: #pertenece a dos aldeas que estaban inconexas
            ficha1 = tablero.dame_ficha(posiciones[0])
            ficha2 = tablero.dame_ficha(posiciones[1])
            if self.es_doble_limite_aldea(ficha1):
                aldea1 = self.dame_aldea_valida_DLA(posiciones[0])
            else:
                aldea1 = self.dame_aldea(posiciones[0])
            if self.es_doble_limite_aldea(ficha2):
                aldea2 = self.dame_aldea_valida_DLA(posiciones[1])
            else:
                aldea2 = self.dame_aldea(posiciones[1])
            self.array_aldeas.remove(aldea1) #eliminamos las antiguas aldeas
            self.array_aldeas.remove(aldea2)
            aldea1.append(pos)
            for elem in aldea2:
                aldea1.append(elem)
            self.array_aldeas.append(aldea1) #agregamos la aldea completa
        else: #pertence a una sola aldea existente
            ficha = tablero.dame_ficha(posiciones[0])
            if self.es_doble_limite_aldea(ficha):
                aldea = self.dame_aldea_valida_DLA(posiciones[0])
            else:
                aldea = self.dame_aldea(posiciones[0])
            self.array_aldeas.remove(aldea) #eliminamos la antigua aldea
            aldea.append(pos)
            self.array_aldeas.append(aldea) #agregamos la aldea completa

    def coloca_ficha_con_DLA(self, tablero, pos):
        #Si la ficha que hay que colocar es DLA:
        #Hay que incluirla en tantas aldeas como limites tenga
        #Por cada lado, si es continuacion de aldea agregaremos la ficha a la aldea correspondiente,
        #si no es continuacion crearemos una aldea nueva para esa posicion
        ficha_actual = tablero.dame_ficha(pos)
        pos_contiguas = self.dame_pos_contiguas(pos[0], pos[1])[0]
        lados = self.dame_pos_contiguas(pos[0], pos[1])[1]

        for i in range(1,5): #1 arriba, 2 abajo, 3 derecha, 4 izquierda
            if ficha_actual.territorio[i][1] == 'A': #comprobamos si en ese lado hay rama
                if self.continua_aldea(tablero, pos, pos_contiguas[i-1], lados[i-1]): #si hay rama y continua un camino existente
                    if self.es_doble_limite_aldea(tablero.dame_ficha(pos_contiguas[i-1])): #si la ficha adyacente tambien es bifurcacion
                        aldea = self.dame_aldea_valida_DLA(pos_contiguas[i-1])
                    else:
                        aldea = self.dame_aldea(pos_contiguas[i-1])
                    self.array_aldeas.remove(aldea)
                    aldea.append(pos)
                    self.array_aldeas.append(aldea)
                else:
                    self.array_aldeas.append([pos]) #si no continua creamos una nueva aldea


    def comprueba_ficha(self, tablero, pos, ficha):
        #Segun el tipo de ficha del que se trate (con camino, con aldea, con camino y aldea),
        #agregaremos esa ficha a una aldea o/y a un camino de los arrays correspondientes
        tipo_ficha = self.que_ficha_es(ficha)

        if tipo_ficha == "con_C":
            self.coloca_ficha_con_C(tablero, pos)

        elif tipo_ficha == "con_DLA":
            print "esdela"
            self.coloca_ficha_con_DLA(tablero, pos)

        elif tipo_ficha == "con_A":
            self.coloca_ficha_con_A(tablero, pos)

        elif tipo_ficha == "con_CA":
            self.coloca_ficha_con_A(tablero, pos)
            self.coloca_ficha_con_C(tablero, pos)

        elif tipo_ficha == "con_B":
            self.coloca_ficha_con_B(tablero, pos)

        elif tipo_ficha == "con_BA":
            self.coloca_ficha_con_B(tablero, pos)
            self.coloca_ficha_con_A(tablero, pos)

    def camino_completado(self, tablero ,camino):
        cont = 0
        for elem in camino:
            if self.es_limite_camino(tablero.dame_ficha(elem)):

                cont += 1
        if cont == 2:
            return True
        else:
            return False

    def aldea_completada(self, tablero ,aldea):
        #Para cada ficha que compone la aldea, si en alguno de sus lados necesita otra
        #ficha con aldea para cerrar y la ficha contigua correspondiente no se encuentra
        #en la aldea, la aldea aun no esta completada
        if len(aldea) == 1:
            return False

        for elem in aldea: #comprobamos cada ficha que compone la aldea
            ficha = tablero.dame_ficha(elem)
            if not self.es_doble_limite_aldea(ficha):# en estos dos casos no es necesario hacer la comprobacion por ser limites
                pos_contiguas = self.dame_pos_contiguas(elem[0], elem[1])[0]
                lados = self.dame_pos_contiguas(elem[0], elem[1])[1]
                for i in range(1,5):  #1 arriba, 2 abajo, 3 derecha, 5 izquierda
                    if ficha.territorio[i][1] == 'A': #Si hay aldea abierta por ese lado
                        if not pos_contiguas[i-1] in aldea: #y la posicion contigua por ese lado no se encuentra dentro de la aldea
                            return False
        return True #si todas las fichas por todos los lados estan cubiertas por las fichas adyacentes correspondientes, esta completa


    def numero_escudos_aldea(self, tablero, aldea):
        escudos = 0
        for pos in aldea:
            ficha = tablero.dame_ficha(pos)
            if ficha.escudo == True:
                escudos += 1
        return escudos

    def dar_puntuacion(self,jugadores,seguidores_total,len_array,escudos=0):
        colores_maximos=[]
        maximo=0
        puntos=0
        for valor in seguidores_total.values():
            if valor > maximo:
                    maximo = valor

        for color in seguidores_total:
            if seguidores_total[color] == maximo:
                colores_maximos.append(color)

        for color in colores_maximos:
            for jugador in jugadores:
                 if jugador.color == color:
                     puntos= len_array+1
                     if escudos > 0:
                         puntos = puntos + 2*escudos
                     jugador.puntuacion += puntos
                     jugador.seguidores += 1
                     break
        return puntos

    def computar_puntos_turno(self,tablero,pos,jugadores):
        seguidores_total = {'negro':0, 'rojo':0, 'amarillo':0, 'azul':0, 'verde':0}
        numero_caminos = []
        ficha=tablero.dame_ficha(pos)
        tipo=self.que_ficha_es(ficha)
        puntos = 0
        if tipo == "con_I" or tipo == "con_CI":
            zona = ficha.zonas[1]
            if ficha.seguidor != None:
                if zona == ficha.seguidor.zona:
                    color = ficha.seguidor.color
                    for jugador in jugadores:
                         if jugador.color == color:
                             jugador.puntuacion += 1
                             jugador.seguidores += 1
                             break
        if tipo == "con_C" or tipo == "con_B" or tipo == "con_CA" or tipo == "con_CI":
            seguidores_total = {'negro':0, 'rojo':0, 'amarillo':0, 'azul':0, 'verde':0}
            for pos_camino in self.array_caminos:
                if pos in pos_camino:
                    numero_caminos.append(pos_camino)
            for camino in numero_caminos:
                if self.camino_completado(tablero,camino):
                    break
            if self.camino_completado(tablero,camino):
                for elem in camino:
                    x = elem[0]
                    y = elem[1]
                    pos = (x, y)
                    ficha_aux = tablero.dame_ficha(pos)
                    if ficha_aux.seguidor == None:
                        continue
                    if (x-1, y) in camino: #Arriba
                        zona = ficha_aux.zonas[4]
                        if zona == ficha_aux.seguidor.zona:
                            seguidores_total[ficha_aux.seguidor.color] += 1

                    elif (x+1, y) in camino: #Abajo
                        zona = ficha_aux.zonas[7]
                        if zona == ficha_aux.seguidor.zona:
                            seguidores_total[ficha_aux.seguidor.color] += 1

                    elif (x, y+1) in camino: #Derecha
                        zona = ficha_aux.zonas[10]
                        if zona == ficha_aux.seguidor.zona:
                            seguidores_total[ficha_aux.seguidor.color] += 1

                    elif (x, y-1) in camino: #Izquierda
                        zona = ficha_aux.zonas[13]
                        if zona == ficha_aux.seguidor.zona:
                            seguidores_total[ficha_aux.seguidor.color] += 1

                puntos=self.dar_puntuacion(jugadores,seguidores_total,len(camino))
                self.array_caminos.remove(camino)


        if tipo == "con_A" or tipo == "con_CA" or tipo == "con_DLA":
            seguidores_total = {'negro':0, 'rojo':0, 'amarillo':0, 'azul':0, 'verde':0}
            aldea= self.dame_aldea(pos)
            if self.aldea_completada(tablero,aldea):
                for elem in aldea:
                    x = elem[0]
                    y = elem[1]
                    pos = (x, y)
                    ficha_aux = tablero.dame_ficha(pos)
                    if ficha_aux.seguidor == None:
                        continue
                    if (x-1, y) in aldea: #Arriba
                        zona = ficha_aux.zonas[4]
                        if zona == ficha_aux.seguidor.zona:
                            seguidores_total[ficha_aux.seguidor.color] += 1

                    elif (x+1, y) in aldea: #Abajo
                        zona = ficha_aux.zonas[7]
                        if zona == ficha_aux.seguidor.zona:
                            seguidores_total[ficha_aux.seguidor.color] += 1

                    elif (x, y+1) in aldea: #Derecha
                        zona = ficha_aux.zonas[10]
                        if zona == ficha_aux.seguidor.zona:
                            seguidores_total[ficha_aux.seguidor.color] += 1

                    elif (x, y-1) in aldea: #Izquierda
                        zona = ficha_aux.zonas[13]
                        if zona == ficha_aux.seguidor.zona:
                            seguidores_total[ficha_aux.seguidor.color] += 1
                escudos=self.numero_escudos_aldea(tablero,aldea)
                puntos=self.dar_puntuacion(jugadores,seguidores_total,2*len(aldea),escudos)
                self.array_aldeas.remove(aldea)
        return puntos
