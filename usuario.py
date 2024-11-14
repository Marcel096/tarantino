class Usuario:
    def __init__(self, nome, apelido, email):
        self.nome = nome
        self.apelido = apelido
        self.email = email
    
    
    def cadastro(self):
        pass

    def exibir_dados(self):
        '''Exibir dados no console'''
        print(f'Nome: {self.nome}'),
        print(f'Apelido: {self.apelido}'),
        print(f'Email: {self.email}')

    def alterar_nome(self, novo_nome):
        '''Alterar o nome do usuário para um novo valor fornecido'''
        if len(novo_nome) < 2:
            print('Nome muito curto. Tente novamente')
            return
        
        if not novo_nome.replace(' ', '').isalpha():
            print('Nome inválido. Use apenas letras.')
            return
        
        self.nome = novo_nome
        print(f'Nome alterado com sucesso para: {self.nome}')
        
    def alterar_email(self, novo_email):
       '''Alterar o email do usuário para um novo valor fornecido'''
       pass

    def alterar_apelido(self, novo_apelido):
        '''Alterar o apelido do usuário para um novo valor fornecido'''
        if len(novo_apelido) < 2:
            print('Apelido muito curto. Tente novamente.')
            return
        self.apelido = novo_apelido
        print(f'Apelido alterado com sucesso para: {self.apelido}')

    def excluir_conta(self):
        '''Deletar a conta do usuário no banco de dados '''
        pass