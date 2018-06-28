#!/usr/bin/env python2.7.12
#-*- coding: utf-8 -*-

import menu
### sistema para registro acadêmico matéria, feito para matéria de conceitos de linguagens de programação

if __name__ == '__main__':

	sis = menu.Menu()

	while(1):

		print "Digite 0 para adicionar dados ! \n"
		print "Digite 1 para alteração de dados !\n"
		print "Digite 2 para remoção de dados ! \n"
		print "Digite 3 para visulizar os dados ! \n"
		print "Digite 4 para sair ! \n"
		
		print "Digite a ação que deseja tomar:  \n"
		opcao = raw_input()

		if int(opcao) == 0:

			sis.adicionarDados()
			
		elif int(opcao) == 1:

			sis.alterarDados()

		elif int(opcao) == 2:

			sis.removerDados()
		
		elif int(opcao) == 3:

			sis.visualizarDados()

		elif int(opcao) == 4:

			break

		else:

			print " A OPÇÃO QUE VOCÊ DIGITOU ESTÁ INCORRETA ! TENTE NOVAMENTE ! "