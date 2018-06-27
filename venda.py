#-*- coding: utf-8 -*-

import totalizavel

class Venda(totalizavel.Totalizavel):


	def __init__(self, numero, data, cliente, itens): #### Numero da venda, data, cliente, list(itensVenda)
		self.numero = numero
		self.data = data
		self.cliente = cliente
		self.itens = itens

	def total(self):

		valor = 0

		for produto in self.itens:
			valor += produto.total()

		return valor

	def imprimir(self):
		print "\t\tVenda ao cliente"
		print "Nome:   " + self.cliente.nome
		print "Data:   " + self.data
		print "Número: " + self.numero
		print "Os produtos presentes na lista são: "
		print "Item Qntd Custo_unt Total" 
		print "----------------------------------"
		for produto in self.itens:
			print produto
		print "Total:  " + str(self.total())
		print "----------------------------------"
	