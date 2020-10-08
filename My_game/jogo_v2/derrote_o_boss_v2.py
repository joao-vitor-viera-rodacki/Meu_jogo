from time import sleep
from random import randint
from arvore_de_abilidades import abilidades_fogo
    


DEFAULT_ATK =  {
    'Ataque Especial': 300,
    'Ataque Ariscado': 200,
    'Ataque Magico De Gelo': 100
}


class Jogador:
    def __init__(self, nome):

        self.level = 6
        self.xp = 0
        self.dano  = (self.level // 2) * 10
        self.usu_dano_max = self.dano + 10
        self.usu_dano_min = self.dano

        self.habilidades = DEFAULT_ATK
       
        self.botões_habilidades = { '1' : 'Ataque Ariscado',
                                   '2' : 'Ataque Magico De Gelo',
                                   '3' : 'Ataque Especial'}

        self.pontos_de_habilidades = 10
        self.hp = (self.level // 2) * 500
        self.nome = nome
        self.contagem_de_atake_especial = 2
    

    def _atacar(self, botao):
        nome_abilidade = self.botões_habilidades[botao]
        valor_abilidade = self.habilidades[nome_abilidade]
        dano_total = self.calcula_dano(valor_abilidade)
        print(f'{nome_abilidade} dano: {dano_total}')

        return dano_total

    def _verificador_pontos(self, pontos):
        if pontos < 5 :
            return False
        else:
            return True


    def atacar_player(self, botao, player_alvo):
        dano_total = self._atacar(botao)
        player_alvo.hp -= dano_total

    def calcula_dano(self, dano_base):
        valor_jogador = randint(self.usu_dano_min, self.usu_dano_max)
        return valor_jogador + dano_base
            
    def add_habilidade(self, nome_habilidade, dano_habilidade, botão ):
        
        verificador = self._verificador_pontos(self.pontos_de_habilidades)

        if botão in self.botões_habilidades or nome_habilidade in self.habilidades or verificador == False:
            return False
        else:
            self.habilidades.update({nome_habilidade : dano_habilidade})
            self.botões_habilidades.update({botão : nome_habilidade})

player1 = Jogador('joao')
player2 = Jogador('LUCAS')

def cont_especial(player):
    player.contagem_de_atake_especial -= 1
    if player.contagem_de_atake_especial <= 0:
        return False
    else :
        return True

def interface(player):
        verificador = cont_especial(player)
        print(f'\033[1;36m{player.nome}\033[1;33m] Sua vez de atacar !!')
        print(f'Menu De skils')
        print('-'*20)
        for botao, habilidade in player.botões_habilidades.items():
            if verificador == False :
                if botao == '3':
                    print(f'\033[31m[{botao}] {habilidade}\033[m')
                else:
                    print(f'[{botao}] {habilidade}')
            else:        
                print(f'[{botao}] {habilidade}')
        print('\033[1;33m-'*20,'\033[m')
        while True:
            Input = input(str('===>> : \033[m'))

            if Input == '3':
                
                if verificador :
                    return Input
                else:
                    print('você não tem mais power para esse poder')
            else: 
                return Input

def verifica_hp_adverdario(player):

    if player.hp <= 0 :
        return True
    else:
        return False

def menu():
    print('''\033[32m
[1] Entrar em uma partida
[2] Adicionar uma habilidade
[3] Mostar estatos do player''')

    Input = input(str('\033[31m===> : \033[m'))

    if Input == '1':
        while True :

            if verifica_hp_adverdario(player1):
                print(f'{player1.nome} Você perdeu !!')
                break
            if verifica_hp_adverdario(player2):
                print(f'{player2.nome} Você perdeu !!')
                break
            Input = interface(player1)
            player1.atacar_player(Input,player2)
            Input = interface(player2)
            player2.atacar_player(Input,player1)
            
menu()