#!/usr/bin/env python2.7.12
#-*- coding: utf-8 -*-

import produto
import re
import cliente
#import venda


class Menu(object):

	produtos = [] ### lista de produtos
	clientes = [] #### lista de pessoas

	def adicionarDados(self):

		print "O que você deseja adicionar ? \n"
		print "Digite 0 para adicionar um produto !\n"
		print "Digite 1 para adicionar um cliente !\n"
		print "Digite 2 para adicionar uma venda !\n"
		opcao = raw_input()

		if int(opcao) == 0: #### adicionar um produto 

			op = 0
			nome = Menu.coletaInfo(self, "Digite o nome do produto: ", op)
			op = 1
			codigo = Menu.coletaInfo(self, "Digite o codigo do produto: ", op)
			op = 2
			valor = Menu.coletaInfo(self, "Digite o preço do produto: ", op)
			
			Menu.produtos.append(produto.Produto(codigo, nome, valor)) #### instancia produto

		elif int(opcao) == 1: ##### adiciona um cliente

			op = 5
			nome = Menu.coletaInfo(self, "Digite o nome do Cliente: ", op)
			op = 4
			endereco = Menu.coletaInfo(self, "Digite o endereço do Cliente: ", op)
			op = 1
			rg = Menu.coletaInfo(self, "Digite seu RG: (apenas números, por favor): ", op)
			op = 3
			nascimento = Menu.coletaInfo(self, "Digite a sua data de nascimento: (no seguinte formato DD/MM/AAAA)", op)


			Menu.clientes.append(cliente.Cliente(nascimento, rg, nome, endereco)) ### data de nascimento, rg, nome e endereço
		
		elif int(opcao) == 2: ### adicionar uma venda

			if len(Menu.produtos)>0: ## numero, data, itens (venda)

				op=5
				nome = Menu.coletaInfo(self, "Digite o nome do Cliente: ", op)
				op = 1 ### seria esse número o código do produto ???
				numero = Menu.coletaInfo(self, "Digite o número da venda: ", op)
				op = 3
				dataVenda = Menu.coletaInfo(self, "Digite a data da venda: (no seguinte formato DD/MM/AAAA)", op)
				flag=0
				marcador=0
				while(1):
					if flag==1:
						print "Você digitou o nome dos produtos fora do formato, por favor digite novamente! \n"
						
					print "Digite os produtos: (no seguinte formato: produto1, produto2, ...)"
					flag=1
					prod = raw_input()
					try:
						prod = prod.split(',')
					except:
						prod = prod

					for i in prod:
						if(re.match(r'\S+', i)) and len(i)>0:

							for k in range(0, len(Menu.produtos)):
								if i != Menu.produtos[k].nome:
									print "O nome do produto que você digitou não está presente na lista!\n"
									print "Os produtos presentes na lista são: "
									print "----------------------------------"
									for k in range(0, len(Menu.produtos)):
										print Menu.produtos[k].nome
									print "----------------------------------"
									break

							marcador = 1

					if marcador==1: #### quer dizer que tá tudo certo, então pode instaciar de forma correta


						break

					




				





			else:
				print "Não existem produtos para serem vendidos ! Cadastre um produto para depois vende-lo !"

		else:

			print " A OPÇÃO QUE VOCÊ DIGITOU ESTÁ INCORRETA ! TENTE NOVAMENTE ! "


	def coletaInfo(self, pergunta, op):
		
		nome = ''
		flag=0
		while not Menu.verificaEntrada(self, nome, op):
			if(flag==0):
				print pergunta
				flag=1
			else:
				print "Você digitou de forma incorreta a informação, por favor digite novamente !\n"
				print pergunta
			nome = raw_input()
			nome = nome.lower()
		return nome

	def verificaEntrada(self, palavra, op):


		if (re.match(r'\S+', palavra)) and op==0 and len(palavra)>0: #### regex para identificar nome

			return True

		elif (re.match(r'^[0-9]+$', palavra)) and op==1 and len(palavra)>0: #### regex para identificar int

			return True

		elif (re.match(r'[+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?', palavra)) and op==2 and len(palavra)>0: #### regex para verificar float

			return True

		elif (re.match(r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/[12][0-9]{3}$', palavra)) and op==3 and len(palavra)>0: ### regex para verificar data

			return True

		elif (re.match(r'^[A-Z_0-9a-z ]+$', palavra)) and op==4 and len(palavra)>0: ### aceita palavras e números

			return True

		elif (re.match(r'^[A-Za-z]+$', palavra)) and op==5 and len(palavra)>0: ### aceita palavras apenas

			return True


	def alterarDados(self):

		print 'everbody is doing the time'


	def removerDados(self):

		print 'ou não'

	def visualizarDados(self):

		print 'oyeeeeeeeeeee'

	

