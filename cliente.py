#-*- coding: utf-8 -*-
import pessoa

class Cliente(pessoa.Pessoa):


	def __init__(self, dataNascimento, rg, nome, endereco): #### metodo contrutor

		self.dataNascimento = dataNascimento
		self.rg = rg
		super(Cliente, self).__init__(nome, endereco)

	def imprimir(self):
		print "Nome do cliente: ", self.nome
		print "Data de nascimento do cliente: ", self.dataNascimento
		print "RG do cliente: ", self.rg
		print "Endereço do cliente: ", self.endereco
		print '\n'