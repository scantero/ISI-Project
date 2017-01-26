from Fichas import Fichas
import random

class ArrayFichas:


	vacia = Fichas('-','-','-','-','-','-','-','-','-','-','-','-','-', ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],False)
	inicial = Fichas('C','A','A','A','P','P','P','P','C','P','P','C','P',[1,1,1,2,2,2,3,3,3,4,1,3,4,1,3],False)

	def __init__(self):

		# centro arriba abajo derecha izquierda
		self.saco = []

		tipo1 = Fichas('A','A','A','A','A','A','A','A','A','A','A','A','A',[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],True)
		self.saco.append(tipo1)

		for i in range(3):
			tipo2 = Fichas('A','A','A','A','P','P','P','A','A','A','A','A','A',[1,1,1,1,1,1,2,2,2,1,1,1,1,1,1],False)
			self.saco.append(tipo2)

		# Con escudo
		tipo2E = Fichas('A','A','A','A','P','P','P','A','A','A','A','A','A',[1,1,1,1,1,1,2,2,2,1,1,1,1,1,1],True)
		self.saco.append(tipo2E)

		tipo3 = Fichas('A','P','P','P','P','P','P','A','A','A','A','A','A',[1,1,1,2,2,2,2,2,2,1,1,1,1,1,1],False)
		self.saco.append(tipo3)

		for i in range(2):
			tipo3E = Fichas('A','P','P','P','P','P','P','A','A','A','A','A','A',[1,1,1,2,2,2,2,2,2,1,1,1,1,1,1],True)
			self.saco.append(tipo3E)

		for i in range(3):
			tipo4 = Fichas('P','A','A','A','P','P','P','P','P','P','A','A','A',[1,1,1,2,2,2,1,1,1,1,1,1,2,2,2],False)
			self.saco.append(tipo4)

		for i in range(2):
			tipo4E = Fichas('P','A','A','A','P','P','P','P','P','P','A','A','A',[1,1,1,2,2,2,1,1,1,1,1,1,2,2,2],True)
			self.saco.append(tipo4E)

		for i in range(2):
			tipo5 = Fichas('P','A','A','A','P','P','P','A','A','A','P','P','P',[1,1,1,2,2,2,1,1,1,3,3,3,1,1,1],False)
			self.saco.append(tipo5)

		for i in range(3):
			tipo6 = Fichas('P','P','P','P','P','P','P','A','A','A','A','A','A',[1,1,1,1,1,1,1,1,1,2,2,2,2,2,2],False)
			self.saco.append(tipo6)

		for i in range(5):
			tipo7 = Fichas('P','A','A','A','P','P','P','P','P','P','P','P','P',[1,1,1,2,2,2,1,1,1,1,1,1,1,1,1],False)
			self.saco.append(tipo7)

		tipo8 = Fichas('A','A','A','A','P','C','P','A','A','A','A','A','A',[1,1,1,1,1,1,2,3,4,1,1,1,1,1,1],False)
		self.saco.append(tipo8)

		for i in range(2):
			tipo8E = Fichas('A','A','A','A','P','C','P','A','A','A','A','A','A',[1,1,1,1,1,1,2,3,4,1,1,1,1,1,1],True)
			self.saco.append(tipo8E)


		for i in range(3):
			tipo9 = Fichas('P','A','A','A','P','C','P','P','C','P','A','A','A',[1,1,1,2,2,2,1,3,4,1,3,4,2,2,2],False)
			self.saco.append(tipo9)

		for i in range(2):
			tipo9E = Fichas('P','A','A','A','P','C','P','P','C','P','A','A','A',[1,1,1,2,2,2,1,3,4,1,3,4,2,2,2],False)
			self.saco.append(tipo9E)

		for i in range(2):
			tipo10 = Fichas('I','P','P','P','P','C','P','P','P','P','P','P','P',[1,1,1,2,2,2,2,3,2,2,2,2,2,2,2],False)
			self.saco.append(tipo10)

		for i in range(3):
			tipo11 = Fichas('P','A','A','A','P','C','P','P','C','P','P','P','P',[1,1,1,2,2,2,1,3,4,1,3,4,1,1,1],False)
			self.saco.append(tipo11)

		for i in range(3):
			tipo12 = Fichas('P','A','A','A','P','C','P','P','P','P','P','C','P',[1,1,1,2,2,2,3,4,1,1,1,1,1,4,3],False)
			self.saco.append(tipo12)

		for i in range(3):
			tipo13 = Fichas('B','A','A','A','P','C','P','P','C','P','P','C','P',[0,0,0,1,1,1,2,3,4,5,6,4,5,7,2],False)
			self.saco.append(tipo13)

		for i in range(3):
			tipo14 = Fichas('C','A','A','A','P','P','P','P','C','P','P','C','P',[1,1,1,2,2,2,3,3,3,4,1,3,4,1,3],False)
			self.saco.append(tipo14)

		tipo15 = Fichas('B','P','C','P','P','C','P','P','C','P','P','C','P',[0,0,0,1,2,3,4,5,6,3,7,6,1,8,4],False)
		self.saco.append(tipo15)

		for i in range(4):
			tipo16 = Fichas('B','P','P','P','P','C','P','P','C','P','P','C','P',[0,0,0,1,1,1,2,3,4,1,5,4,1,6,2],False)
			self.saco.append(tipo16)

		for i in range(8):
			tipo17 = Fichas('C','P','C','P','P','C','P','P','P','P','P','P','P',[1,1,1,2,1,3,2,1,3,3,3,3,2,2,2],False)
			self.saco.append(tipo17)

		for i in range(9):
			tipo18 = Fichas('C','P','P','P','P','C','P','P','P','P','P','C','P',[1,1,1,2,2,2,3,1,2,2,2,2,2,1,3],False)
			self.saco.append(tipo18)

		for i in range(4):
			tipo19 = Fichas('I','P','P','P','P','P','P','P','P','P','P','P','P',[1,1,1,2,2,2,2,2,2,2,2,2,2,2,2],False)
			self.saco.append(tipo19)

	def sacar_ficha(self,pos=None):
		if pos == None:
			pos=random.randint(0,len(self.saco)-1)
		return self.saco[pos]


	def eliminar_ficha(self, ficha):
		self.saco.remove(ficha)
