from time import sleep
from random import randint
from arvore_de_abilidades import abilidades_fogo
    
        



DEFAULT_ATK =  {
    'Ataque Especial': 100,
    'Ataque Ariscado': 200,
    'Ataque Magico De Gelo': 300
}



class Jogador:
    def __init__(self, nome):

        self.level = 6
        self.xp = 0
        self.dano  = (self.level // 2) * 10
        self.usu_dano_max = self.dano + 10
        self.usu_dano_min = self.dano

        self.abilidades = DEFAULT_ATK
       
        self.botões_abilidades = { '1' : 'Ataque Ariscado',
                                   '2' : 'Ataque Magico De Gelo',
                                   '3' : 'Ataque Especial'}

        self.pontos_de_abilidades = 10
        self.hp = (self.level // 2) * 500
        self.nome = nome
        self.contagem_de_atake_especial = 2
    
    def add_habilidade(self, nome_habilidade, dano_habilidade, botão ):
        
        verificador = self._verificador_pontos(self.pontos_de_abilidades)

        if botão in self.botões_abilidades or nome_habilidade in self.abilidades or verificador == False:
            return False
        else:
            self.abilidades.update({nome_habilidade : dano_habilidade})
            self.botões_abilidades.update({botão : nome_habilidade})
    
    def _atacar(self, botao):
        nome_abilidade = self.botões_abilidades[botao]
        valor_abilidade = self.abilidades[nome_abilidade]
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
