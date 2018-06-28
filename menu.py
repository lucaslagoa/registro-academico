#!/usr/bin/env python2.7.12
#-*- coding: utf-8 -*-

import produto
import re
import cliente
import itemVenda
import venda


class Menu(object):

	produtos = [] ### lista de produtos
	clientes = [] #### lista de pessoas
	vendas_menu = [] ### lista de itens vendidos

	def adicionarProdutos(self, opcao, p):
		op = 0
		nome = Menu.coletaInfo(self, "Digite o nome do produto: ", op)
		op = 1
		codigo = Menu.coletaInfo(self, "Digite o codigo do produto: ", op)
		op = 2
		valor = Menu.coletaInfo(self, "Digite o preço do produto: ", op)
		
		if opcao == "adicionar":
			Menu.produtos.append(produto.Produto(codigo, nome, valor)) #### instancia produto
		else:
			Menu.produtos[p] = produto.Produto(codigo, nome, valor)

	def adicionarCliente(self, opcao, p):
		op = 5
		nome = Menu.coletaInfo(self, "Digite o nome do Cliente: ", op)
		op = 4
		endereco = Menu.coletaInfo(self, "Digite o endereço do Cliente: ", op)
		op = 1
		rg = Menu.coletaInfo(self, "Digite o RG: (apenas números, por favor): ", op)
		op = 3
		nascimento = Menu.coletaInfo(self, "Digite a data de nascimento do Cliente: (no seguinte formato DD/MM/AAAA)", op)

		if opcao == "adicionar":
			Menu.clientes.append(cliente.Cliente(nascimento, rg, nome, endereco)) ### data de nascimento, rg, nome e endereço
		else:
			Menu.clientes[p] = cliente.Cliente(nascimento, rg, nome, endereco)

	def adicionarVenda(self, opcao, p):

		if len(Menu.produtos)>0: ## numero, data, itens (venda)

			op=5
			
			if len(Menu.clientes)>0:
				marcador = 0
				nome = Menu.coletaInfo(self, "Digite o nome do Cliente: ", op)
				for i in range(0, len(Menu.clientes)):
					if Menu.clientes[i].nome == nome:
						cliente = Menu.clientes[i]
						marcador = 1

				if marcador == 0:
					print "Não há clientes com este nome, por favor, digite um nome dentro desta lista ou cadastre este cliente ! \n"
					print "Os nomes presentes na lista de clientes são: \n"
					print "-------------------------------"
					for i in range(0, len(Menu.clientes)):
						print Menu.clientes[i].nome
					print "-------------------------------"
					nome = " "
				else:
					marcador = 0

			else: 
				print "Não há clientes cadastrados. Cadastre primeiro um cliente !"
				nome = " "
			if nome != " ":
				op = 1 ### seria esse número o código do produto ???
				numero = Menu.coletaInfo(self, "Digite o número da venda: ", op)
				op = 3
				dataVenda = Menu.coletaInfo(self, "Digite a data da venda: (no seguinte formato DD/MM/AAAA)", op)
				flag=0
				marcador=0
				if flag==1:
					print "Você digitou o nome dos produtos fora do formato, por favor digite novamente! \n"
					
				print "Digite os produtos: (no seguinte formato: produto1,produto2, ...) sem espaços"
				flag=1
				prod = raw_input()
				try:
					prod = prod.split(',')
				except:
					prod = prod

				for i in prod: # verifica se os produtos foram cadastrados
					if(re.match(r'\S+', i)) and len(i)>0:
						for k in range(0, len(Menu.produtos)):
							if i == Menu.produtos[k].nome:
								marcador = 1
								break;
							marcador = 0
						if marcador == 0:
							print "\n\nATENÇÃO: Produto " + i + " não existe!\n\n"

						
				prod = sorted(prod) ### ordenando os produtos por nome

				if marcador==1: #### quer dizer que tá tudo certo, então pode instaciar de forma correta
					vendaItens = []
					for i in range(0, len(prod)):
						op = 1
						quantidade = Menu.coletaInfo(self, "Digite a quantidade de produtos do tipo " + prod[i] + " foram comprados: ", op)
						
						for j in range(0, len(Menu.produtos)):
							if prod[i] == Menu.produtos[j].nome:
								produto = Menu.produtos[j].nome
								valor = Menu.produtos[j].valor
								break
						vendaItens.append(itemVenda.itemVenda(produto, valor, quantidade))

					venda_atual = venda.Venda(numero, dataVenda, cliente, vendaItens)
					if opcao == "adicionar":
						self.vendas_menu.append(venda_atual)
					else:
						self.vendas_menu[p] = venda_atual

					venda_atual.imprimir()
		else:
			print "Não existem produtos para serem vendidos ! Cadastre um produto para depois vende-lo !"

	def adicionarDados(self):

		print "O que você deseja adicionar ? \n"
		print "Digite 0 para adicionar um produto !\n"
		print "Digite 1 para adicionar um cliente !\n"
		print "Digite 2 para adicionar uma venda !\n"
		opcao = raw_input()

		if int(opcao) == 0: #### adicionar um produto 

			Menu.adicionarProdutos(self, "adicionar", 0)
			
		elif int(opcao) == 1: ##### adiciona um cliente

			Menu.adicionarCliente(self, "adicionar", 0)
		
		elif int(opcao) == 2: ### adicionar uma venda

			Menu.adicionarVenda(self, "adicionar", 0)

		else:

			print " A opção que você digitou está incorreta, digite novamente ! "


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

		elif (palavra=='s' or palavra=='n') and op==6 and len(palavra)>0: ### aceita palavras apenas

			return True

	def alterarInfo(self, lista, op): ###### função para alterar dados

		if len(lista) == 0 :
			print "Não há " + op + " para alterar.\n"
			return
		Menu.imprimeDados(self, lista, op)
		numero = 0
		flag=0
		while(1):
			if flag== 1:
				print "Você digitou um número que não está presente na lista, por favor digite novamente: "
			flag=1	
			aux = 0
			numero = Menu.coletaInfo(self, "Digite o número do "+op+" que deseja alterar: ", aux)
			numero = int(numero)

			if numero<=len(lista)-1:
				aux = 6
				if op != "venda":
					resp = Menu.coletaInfo(self, "Você deseja alterar o "+op+" : " + lista[numero].nome + " ? (Digite S para sim e N para não)", aux)
				else:
					resp = Menu.coletaInfo(self, "Você deseja alterar o "+op+" : " + lista[numero].numero + " ? (Digite S para sim e N para não)", aux)
				if op == "produto": Menu.adicionarProdutos(self, "alterar", numero)
				elif op == "cliente":Menu.adicionarCliente(self, "alterar", numero)
				elif op == "venda":Menu.adicionarVenda(self, "alterar", numero)
				break


	def alterarDados(self):

		print "O que você deseja alterar ? \n"
		print "Digite 0 para alterar um produto !\n"
		print "Digite 1 para alterar um cliente !\n"
		print "Digite 2 para alterar uma venda !\n"
		opcao = raw_input()

		if int(opcao) == 0: ###### alterar um produto

			Menu.alterarInfo(self, Menu.produtos, "produto")

		elif int(opcao) == 1: #### alterar um cliente

			Menu.alterarInfo(self, Menu.clientes, "cliente")

		elif int(opcao) == 2: #### alterar uma venda

			Menu.alterarInfo(self, Menu.vendas_menu, "venda")
			
		else:
			print " A opção que você digitou está incorreta, digite novamente ! "


	def removeProdutos(self, tipo, lista):
		numeroProd = 0
		op = 1
		flag=0
		while(1):
			if flag== 1:
				print "Você digitou um número que não está presente na lista, por favor digite novamente: "
			flag=1	
			numeroProd = Menu.coletaInfo(self, "Digite o número do "+tipo+" que deseja retirar: ", op)
			numeroProd = int(numeroProd)

			if numeroProd<=len(lista)-1:
				op = 6
				if tipo == 'venda':
					resp = Menu.coletaInfo(self, "Você deseja retirar o "+tipo+" : " + lista[numeroProd].numero + " ? (Digite S para sim e N para não)", op)
				else:
					resp = Menu.coletaInfo(self, "Você deseja retirar o "+tipo+" : " + lista[numeroProd].nome + " ? (Digite S para sim e N para não)", op)

				return resp, numeroProd

		

	def removeItens(self, tipo, lista):

		Menu.imprimeDados(self, lista, tipo)

		if len(lista)>0:
			
			resp, numeroProd = Menu.removeProdutos(self, tipo, lista)
			
			if resp == 's':

				lista.pop(numeroProd)

			else:

				while (resp=='n'):

					resp, numeroProd = Menu.removeProdutos(self, tipo, lista)

	def removerDados(self): ### remoção dos dados

		print "O que você deseja remover ? \n"
		print "Digite 0 para remover um produto !\n"
		print "Digite 1 para remover um cliente !\n"
		print "Digite 2 para remover uma venda !\n"
		opcao = raw_input()

		if int(opcao) == 0: ###### remover um produto

			Menu.removeItens(self, "produto", Menu.produtos)

		elif int(opcao) == 1: #### remover um cliente


			Menu.removeItens(self, "cliente", Menu.clientes)

		elif int(opcao) == 2:

			Menu.removeItens(self, "venda", Menu.vendas_menu)


		else:
			print " A opção que você digitou está incorreta, digite novamente ! "

	def visualizarDados(self):

		print "Você selecionou o modo de visualização de dados, aqui serão dispostos todos os dados presentes até o momento ! \n"
		Menu.imprimeDados(self, Menu.produtos, "produto")
		Menu.imprimeDados(self, Menu.clientes, "cliente")
		Menu.imprimeDados(self, Menu.vendas_menu, "venda")

	def imprimeDados(self, dados, tipoDado):

		if len(dados)==0:
			print "Não há informação para " + tipoDado + "\n"
		else:
			print "Os dados para " + tipoDado + " são: "
			print '---------------------------------'

			for i in range(0, len(dados)):
				
				if tipoDado == "cliente":
					print "Cliente " + str(i)
					
				elif tipoDado == "produto":
					print "Produto "+ str(i)
				
				elif tipoDado == "venda":
					print "Venda " + str(i)

				dados[i].imprimir()
