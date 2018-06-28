#!/usr/bin/env python2.7.12
#-*- coding: utf-8 -*-

class Produto(object):



	def __init__(self, codigo, nome, valor): #### metodo contrutor

		self.codigo = codigo
		self.nome = nome
		self.valor = valor

	def imprimir(self):
		print "Nome do produto: ", self.nome
		print "Código do produto: ", self.codigo
		print "Valor do produto: ", self.valor
		print '\n'