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

	# def total(self): FUNÇÃO DEPRECIADA, ISSO É COISA DE CALOURO, QUERO ORIENTAÇÃO A OBJETOS, CEEEEEERTO!
	# 	total = 0;
	# 	for x in range(0,len(self.venda.itens)):
	# 		parcial = self.valor[x] * self.quantidade[x]
	# 		print "\t" + self.itens[x] + "\t" + self.valor[x] + "\t" + parcial
	# 		total += parcial
