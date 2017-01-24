from Partida import Partida
import unittest


class PArtidaTest(unittest.TestCase):

    # Test para Nombre Adrian-- meter Adrian de nombre
    def test_info_jugador_nombre(self):
        p=Partida()
        p.info_jugadores(2,"Adrian","azul","Alberto","verde")
        expected="Adrian"
        self.assertEqual(p.jugadores[0].nombre,expected)
        expected="Alberto"
        self.assertEqual(p.jugadores[1].nombre,expected)

     # Test para color "azul" -- meter azul de color
    def test_info_jugador_color(self):
         p=Partida()
         p.info_jugadores(2,"Adrian","azul","Alberto","verde")
         expected="azul"
         self.assertEqual(p.jugadores[0].color,expected)
         expected="verde"
         self.assertEqual(p.jugadores[1].color,expected)

    # Test compureba todo tanto nombre y colores ( que anade al jugador ) 5 jugadores
    def test_jugadores(self):
        p=Partida()
        p.info_jugadores(5,"Adrian","azul","Alberto","verde","Sandra","rojo","Diego","amarillo","Yo","negro")
        jugs=["Adrian","Alberto","Sandra","Diego","Yo"]
        cols=["azul","verde","rojo","amarillo", "negro"]

        for n in range(4):
            expected= jugs[n]
            self.assertEqual(p.jugadores[n].nombre,expected)
            expected2=cols[n]
            self.assertEqual(p.jugadores[n].color,expected2)

    # test anade jugadores al array
    def test_mete_jugadores (self):
       p=Partida()
       self.assertEqual(len(p.jugadores),0)
       p.info_jugadores(3,"Adrian","azul","Alberto","verde","Sandra","amarillo")
       self.assertEqual(len(p.jugadores), 3)


      # test para ckeck los jugadores anadidos al array no son None
    def test_notNone (self):
        p=Partida()
        p.info_jugadores(5,"Adrian","azul","Alberto","verde","Sandra","rojo","Diego","amarillo","Yo","negro")
        for jug in p.jugadores:
            self.assertIsNotNone(jug)

     #test para comprobar que pasa de turno a los jugadores. primer turno Adrian
    def test_pasar_turno(self):
         p=Partida()
         p.info_jugadores(2,"Adrian","azul","Alberto","verde")
         jugador=p.pasar_turno(p.jugadores[0])
         expected="Alberto"
         self.assertEqual(expected,jugador.nombre)


     # test pos valida
    def test_elegir_coord_correcta(self):
         p=Partida()
         p.info_jugadores(2,"Adrian","azul","Alberto","verde")
         expected="(12, 15)"
         self.assertEqual(expected,p.elegir([(12,15), (25,32), (25,39)],"(12, 15)"))


     # test para girar
    def test_elegir_coord_incorrecta(self):
         p=Partida()
         p.info_jugadores(2,"Adrian","azul","Alberto","verde")
         expected="G"
         self.assertEqual(expected,p.elegir([(12,15), (25,32), (25,39)],"G"))

    def test_colocar_seg(self):
        p=Partida()
        ficha=Fichas('A','A','A','A','A','A','A','A','A','A','A','A','A',[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        jugador= Jugador('Adrian', 'Rojo')
        expected=p.seguidores-1
        self.assertEqual(expected,p.colocar_seg(ficha,jugador))

if __name__ == '__main__':
	unittest.main()
