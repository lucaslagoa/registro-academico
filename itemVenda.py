#-*- coding: utf-8 -*-
import totalizavel
import venda as sell

class itemVenda(totalizavel.Totalizavel):


	def __init__(self, produto, valor, quantidade): #### metodo contrutor
		self.quantidade = quantidade
		self.valor = valor
		self.produto = produto

	#Calcula o total do itemVenda 
	def total(self):
		return int(self.quantidade) * float(self.valor)

	# imprime o itemVenda
	def __str__(self): 
		return self.produto + "\t" + self.quantidade + "\t" + str(self.valor) + "\t" + str(self.total())
