import pessoa

class Cliente(pessoa.Pessoa):


	def __init__(self, dataNascimento, rg, nome, endereco): #### metodo contrutor

		self.dataNascimento = dataNascimento
		self.rg = rg
		super(Cliente, self).__init__(nome, endereco)

