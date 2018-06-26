import totalizavel
import venda as sell

class itemVenda(totalizavel.Totalizavel):


	def __init__(self, valor, quantidade, numero, data, itens): #### metodo contrutor

		self.quantidade = quantidade
		self.valor = valor
		self.venda = sell.Venda(numero, data, itens)
