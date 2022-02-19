#Lógica do APP

######Crie um programa que calcula gastos mensais e os classifica por tags######

#Iniciar dando opções ao usuário
#Checar credenciais
#Quais os dados necessários para o APP? (item, valor e a tag);
#solicitar os imputs necessários;
#organizar-los em listas por tags;
#reservar os valores classificados nas suas tags;
#somar todos os valores;

""" class AppCalculadora:
    def __init__(self, menuMain, receitas, despesas, adicionar, remover, alterar, sair):
        self.menuMain = {'RECEITAS': 1, 'DESPESAS': 2, 'SAIR': 6}
        self.receitas = receitas
        self.despesas = despesas
        self.item = item
        self.valor = valor
        self.lista_de_tags = ['TRANSPORTE', 'ALIMENTAÇÃO', 'SAÚDE', 'EDUCAÇÃO', 'LAZER']
        self.tag = tag
    
    def menu (self, showMenu):
        self.menu = {'RECEITAS': 1, 'DESPESAS': 2, 'ADICIONAR': 3, 'REMOVER': 4, 'ALTERAR': 5, 'SAIR': 6}
        print('MENU PRINCIPAL - DIGITE UMA OPÇÃO VÁLIDA')
        c = 0
        for m in menu:
            print(f'{m:10}-----> {c:5}.')
            c+=1
        opcoes = [0,1,2,3,4,5] """


c = 0
resposta = int()

for m in menu:
    print(f'{m:10}-----> {c:5}.')
    c+=1



while resposta not in opcoes:
    r = input('Digite uma opção válida: ')
    if resposta in opcoes:
        print('Opção válidada!')

    def receitas (self, showIns):
        print('receitas')
        pass

    def despesas (self, showOuts):
        pass

    def adicionar (self, entrada):
        pass

    def alterar (self, trocar):
        pass

    def remover (self, excluir):
        pass

    def sair (self, fechar):
        pass






#menu = {'RECEITAS': 1, 'DESPESAS': 2, 'ADICIONAR': 3, 'REMOVER': 4, 'ALTERAR': 5, 'SAIR': 6}
#tags = ['TRANSPORTE', 'ALIMENTAÇÃO', 'SAÚDE', 'EDUCAÇÃO']


opcoes = [0,1,2,3,4,5]


c = 0
resposta = int()

for m in menu:
    print(f'{m:10}-----> {c:5}.')
    c+=1



while resposta not in opcoes:
    r = input('Digite uma opção válida: ')
    if resposta in opcoes:
        print('Opção válidada!')
    



item = input(f'Digite o nome do item para adicionar a lista de gastos: ')
valor = input(f'Digite o preço: ')


print(f'o {item} custou R$ {valor}?')


