import totalizavel

class Venda(totalizavel.Totalizavel):


	def __init__(self, numero, data, itens): #### metodo contrutor

		self.numero = numero
		self.data = data
		self.itens = itens

	def total(self, produtos):

		valor = 0


		return valor