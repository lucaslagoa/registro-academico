import totalizavel
import venda

class itemVenda(totalizavel.Totalizavel):


	def __init__(self, valor, quantidade, numero, data, itens): #### metodo contrutor

		self.quantidade = quantidade
		self.valor = valor
		venda.Venda(numero, data, itens)
