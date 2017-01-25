from Fichas import Fichas
import random

class ArrayFichas:

	saco = []
	# centro arriba abajo derecha izquierda
	vacia = Fichas('-','-','-','-','-','-','-','-','-','-','-','-','-', ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'],False)
	inicial = Fichas('C','A','A','A','P','P','P','P','C','P','P','C','P',[1,1,1,2,2,2,3,3,3,4,1,3,4,1,3],False)
	tipo1 = Fichas('A','A','A','A','A','A','A','A','A','A','A','A','A',[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],True)
	tipo2 = Fichas('A','A','A','A','P','P','P','A','A','A','A','A','A',[1,1,1,1,1,1,2,2,2,1,1,1,1,1,1],False)
	tipo2E = Fichas('A','A','A','A','P','P','P','A','A','A','A','A','A',[1,1,1,1,1,1,2,2,2,1,1,1,1,1,1],True)
	tipo3 = Fichas('A','P','P','P','P','P','P','A','A','A','A','A','A',[1,1,1,2,2,2,2,2,2,1,1,1,1,1,1],False)
	tipo3E = Fichas('A','P','P','P','P','P','P','A','A','A','A','A','A',[1,1,1,2,2,2,2,2,2,1,1,1,1,1,1],True)
	tipo4 = Fichas('P','A','A','A','P','P','P','P','P','P','A','A','A',[1,1,1,2,2,2,1,1,1,1,1,1,2,2,2],False)
	tipo4E = Fichas('P','A','A','A','P','P','P','P','P','P','A','A','A',[1,1,1,2,2,2,1,1,1,1,1,1,2,2,2],True)
	tipo5 = Fichas('P','A','A','A','P','P','P','A','A','A','P','P','P',[1,1,1,2,2,2,1,1,1,3,3,3,1,1,1],False)
	tipo6 = Fichas('P','P','P','P','P','P','P','A','A','A','A','A','A',[1,1,1,1,1,1,1,1,1,2,2,2,2,2,2],False)
	tipo7 = Fichas('P','A','A','A','P','P','P','P','P','P','P','P','P',[1,1,1,2,2,2,1,1,1,1,1,1,1,1,1],False)
	tipo8 = Fichas('A','A','A','A','P','C','P','A','A','A','A','A','A',[1,1,1,1,1,1,2,3,4,1,1,1,1,1,1],False)
	tipo8E = Fichas('A','A','A','A','P','C','P','A','A','A','A','A','A',[1,1,1,1,1,1,2,3,4,1,1,1,1,1,1],True)
	tipo9 = Fichas('P','A','A','A','P','C','P','P','C','P','A','A','A',[1,1,1,2,2,2,1,3,4,1,3,4,2,2,2],False)
	tipo9E = Fichas('P','A','A','A','P','C','P','P','C','P','A','A','A',[1,1,1,2,2,2,1,3,4,1,3,4,2,2,2],True)
	tipo10 = Fichas('I','P','P','P','P','C','P','P','P','P','P','P','P',[1,1,1,2,2,2,2,3,2,2,2,2,2,2,2],False)
	tipo11 = Fichas('P','A','A','A','P','C','P','P','C','P','P','P','P',[1,1,1,2,2,2,1,3,4,1,3,4,1,1,1],False)
	tipo12 = Fichas('P','A','A','A','P','C','P','P','P','P','P','C','P',[1,1,1,2,2,2,3,4,1,1,1,1,1,4,3],False)
	tipo13 = Fichas('B','A','A','A','P','C','P','P','C','P','P','C','P',[0,0,0,1,1,1,2,3,4,5,6,4,5,7,2],False)
	tipo14 = Fichas('C','A','A','A','P','P','P','P','C','P','P','C','P',[1,1,1,2,2,2,3,3,3,4,1,3,4,1,3],False)
	tipo15 = Fichas('B','P','C','P','P','C','P','P','C','P','P','C','P',[0,0,0,1,2,3,4,5,6,3,7,6,1,8,4],False)
	tipo16 = Fichas('B','P','P','P','P','C','P','P','C','P','P','C','P',[0,0,0,1,1,1,2,3,4,1,5,4,1,6,2],False)
	tipo17 = Fichas('C','P','C','P','P','C','P','P','P','P','P','P','P',[1,1,1,2,1,3,2,1,3,3,3,3,2,2,2],False)
	tipo18 = Fichas('C','P','P','P','P','C','P','P','P','P','P','C','P',[1,1,1,2,2,2,3,1,2,2,2,2,2,1,3],False)
	tipo19 = Fichas('I','P','P','P','P','P','P','P','P','P','P','P','P',[1,1,1,2,2,2,2,2,2,2,2,2,2,2,2],False)


	def __init__(self):

		self.saco.append(self.tipo1)

		for i in range(3):
			self.saco.append(self.tipo2)
		# Con escudo
		self.saco.append(self.tipo2E)

		self.saco.append(self.tipo3)
		for i in range(2):
			self.saco.append(self.tipo3E)

		for i in range(3):
			self.saco.append(self.tipo4)
		for i in range(2):
			self.saco.append(self.tipo4E)

		for i in range(2):
			self.saco.append(self.tipo5)

		for i in range(3):
			self.saco.append(self.tipo6)

		for i in range(5):
			self.saco.append(self.tipo7)

		for i in range(2):
			self.saco.append(self.tipo8E)
		self.saco.append(self.tipo8)

		for i in range(3):
			self.saco.append(self.tipo9)
		for i in range(2):
			self.saco.append(self.tipo9E)

		for i in range(2):
			self.saco.append(self.tipo10)

		for i in range(3):
			self.saco.append(self.tipo11)

		for i in range(3):
			self.saco.append(self.tipo12)
		for i in range(3):
			self.saco.append(self.tipo13)
		for i in range(3):
			self.saco.append(self.tipo14)

		self.saco.append(self.tipo15)

		for i in range(4):
			self.saco.append(self.tipo16)

		for i in range(8):
			self.saco.append(self.tipo17)

		for i in range(9):
			self.saco.append(self.tipo18)

		for i in range(4):
			self.saco.append(self.tipo19)

	def sacar_ficha(self,pos=None):
		if pos == None:
			pos=random.randint(0,len(self.saco)-1)
		return self.saco[pos]


	def eliminar_ficha(self, ficha):
		self.saco.remove(ficha)
