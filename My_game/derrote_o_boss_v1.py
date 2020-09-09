from time import sleep
from random import randint
import arvore_de_abilidades


#def ataque(habilidade, especial=false):
    
        
class Inimigo:
    def __init__(self):
        
        self.tipo_atake = NotImplemented
        self.level = 2
        self.dano  = (self.level // 2) * 10
        self.hp =  (self.level // 2) * 200




class Jogador:
    def __init__(self, nome):

        self.level = 2
        self.xp = 0
        self.dano  = (self.level // 2) * 10
        self.usu_dano_max = self.dano + 10
        self.usu_dano_min = self.dano
        self.abilidades = {   "3": {'nome': 'Ataque especial','danoMAX': 200, 'danoMIN':0},
                              "2": {'nome': 'Ataque Magico de Gelo', 'danoMAX': self.usu_dano_max ,'danoMIN':self.usu_dano_min},
                              "1":{'nome': 'Ataque Ariscado', 'danoMAX': self.usu_dano_max + 100,'danoMIN': 0 } }

        
        self.pontos_de_abilidades = 0
        self.hp = (self.level // 2) * 100
        self.nome = nome
        self.contagem_de_atake_especial = 2
    

usuario = Jogador('dragonogt')

inimigo = Inimigo()

def menu():
    
    print('----'*20)
    print('''Seja bem vindo !!
    [1] Para entrar em uma partida...
    [2] Para entrar em na arvore de evolução
    [3] Para ver status do jogador''')

    while True:
        try:
            opção = int(input('Escolha : '))

        except:
            print('digite novamente...')
        
        else:
            if opção == 1:
                print('----'*20)
                partida()
                break
            
            elif opção == 2:
                print('----'*20)
                arvore_de_evolução()      
                break

            elif opção == 3:
                print('_-'*20)
                print(f'''Nome :  {usuario.nome}
                          Level:  {usuario.level}
                          Dano :  {usuario.dano}
                          HP   :  {usuario.hp}
                          Xp   :  {usuario.xp}
                          Pontos De Abilidades : {usuario.pontos_de_abilidades}
                          ''')
                print('Abilidades')
                print('-='*20)
                for key  in usuario.abilidades.keys():
                    print(f'{key}')
                    print('-='*20)
                    
                print('_-'*20)

def partida():

    inimigo_hp_padrão = inimigo.hp
    usuario_hp_padrão = usuario.hp
    def recuperação():
        inimigo.hp = inimigo_hp_padrão
        usuario.hp = usuario_hp_padrão
        usuario.contagem_de_atake_especial = 2

    print('Entrando na partida')
    print('1..')
    sleep(0.80)
    print('2..')
    sleep(0.80)
    print('3..')
    sleep(0.80)
    print('Já..')
    print('_-'*20)
    while True:
        while True:
                        
            if inimigo.hp <= 0 :
                print('===='* 20)
                print(f'Parabens {usuario.nome}. Você ganhou !!')
                
                usuario.xp += 100
                proximo_nivel = (usuario.level * 100) + 100
                recuperação()

                if usuario.xp >= proximo_nivel :
                    usuario.level += 1
                    inimigo.level += 1 

                    usuario.dano  = (usuario.level // 2) * 10
                    usuario.hp = (usuario.level // 2) * 100
                    usuario.xp = 0
                    usuario.pontos_de_abilidades += 3 
                    print('Você subio de nivel !!!')
                    print(f'Nivel atual {usuario.level}')

                menu()

            if usuario.hp <= 0 :
                recuperação()
                print(f'{usuario.nome} você perdeu. Tente Novamente.. ')

                menu()

            print('_-'*20)
            print(f'''Painel de skils''')

            for key, values in usuario.abilidades.items():
                if key == '3':
                    print(f'[{key}] ; {values["nome"]} [[ Dano Maximo {values["danoMAX"]}// Dano minimo {values["danoMIN"]}||{usuario.contagem_de_atake_especial} Ataques restantes...]]')
                else:
                    print(f'[{key}] ; {values["nome"]} [[ Dano Maximo {values["danoMAX"]}// Dano minimo {values["danoMIN"]}]]')
            print('_-'*20)           
            try:

                opção = str(input('Escolha : '))
                    
            except:
                print('Digite novamente...')
            
            else:
                atacar(opcao=opção)
            
            
        
def atacar(opcao=0):
    
    if opcao == usuario.abilidades['2']:

        inimigo.tipo_atake = randint(1,2)
        
        ini_dano_min = inimigo.dano - (inimigo.dano // 2)

        if inimigo.tipo_atake == 1:
            ini_dano_max = inimigo.dano 
        elif inimigo.tipo_atake == 2:
            ini_dano_max = inimigo.dano + 15

        usu_dano_total =  randint(usuario.usu_dano_min, usuario.usu_dano_max)
        ini_dano_total = randint(ini_dano_min, ini_dano_max)
        
        
        usuario.hp -= ini_dano_total
        inimigo.hp -= usu_dano_total
        
        print('__-'*20)
        print(f'''O inimigo levou {usu_dano_total} de da 
        HP Inimigo :: {inimigo.hp}''')
        print('__-'*20)
        print(f'''Você levou {ini_dano_total} De dano
        HP Seu :: {usuario.hp}''')

    if opcao == usuario.abilidades['1']:

        
        inimigo.tipo_atake = randint(1,2)
        
        ini_dano_min = inimigo.dano - (inimigo.dano // 2)

        if inimigo.tipo_atake == 1:
            ini_dano_max = inimigo.dano 
        elif inimigo.tipo_atake == 2:
            ini_dano_max = inimigo.dano + 15

        usu_dano_total =  randint( 0 ,usuario.usu_dano_max + 100 )
        ini_dano_total = randint(ini_dano_min, ini_dano_max )
        
        
        usuario.hp -= ini_dano_total
        inimigo.hp -= usu_dano_total
        
        print('__-'*20)
        print(f'''O inimigo levou {usu_dano_total} de da 
        HP Inimigo :: {inimigo.hp}''')
        print('__-'*20)
        print(f'''Você levou {ini_dano_total} De dano
        HP Seu :: {usuario.hp}''')

    if opcao == usuario.abilidades['3'] :
        
        if usuario.contagem_de_atake_especial == 0 :
            print("Voçê não tem mais power para realizar esse ataque !!")

        else:    
            usuario.contagem_de_atake_especial -= 1

        
            if usuario.contagem_de_atake_especial < 0 :
                print("Voçê não tem mais power para realizar esse ataque !!")
            
            else:
            
                inimigo.tipo_atake  = randint(1,2)
                
                ini_dano_min = inimigo.dano - (inimigo.dano // 2)

                if inimigo.tipo_atake == 1 :
                    ini_dano_max = inimigo.dano 
                
                elif inimigo.tipo_atake == 2 :
                    ini_dano_max = inimigo.dano + 15

                usu_dano_total =  randint(80 , 200)
                ini_dano_total = randint(ini_dano_min, ini_dano_max)

                usuario.hp -= ini_dano_total
                inimigo.hp -= usu_dano_total

                print('__-'*20)
                print(f'''O inimigo levou {usu_dano_total} De Dano 
                HP Inimigo :: {inimigo.hp}''')
                print('__-'*20)
                print(f'''Você levou {ini_dano_total} De dano
                HP Seu :: {usuario.hp}''')    

    if 'Golpe De Fogo' in usuario.abilidades:
        
        if opcao == usuario.abilidades['Golpe De Fogo']:
                            
            inimigo.tipo_atake  = randint(1,2)
            
            ini_dano_min = inimigo.dano - (inimigo.dano // 2)

            if inimigo.tipo_atake == 1 :
                ini_dano_max = inimigo.dano 
            
            elif inimigo.tipo_atake == 2 :
                ini_dano_max = inimigo.dano + 15


            usu_dano_total = randint(80,100 + (usuario.dano // 4))

            ini_dano_total = randint(ini_dano_min, ini_dano_max)

            usuario.hp -= ini_dano_total
            inimigo.hp -= usu_dano_total


            print('_-'*20)
            print(f'''O inimigo levou {usu_dano_total} De Dano
            HP inimigo {inimigo.hp}''')
            print('_-'*20)
            print(f'''Você levou {ini_dano_total} De Dano
            Seu HP {usuario.hp}''')

    if 'Exploção de Fogo' in usuario.abilidades:
            
            if opcao == usuario.abilidades['Exploção de Fogo']:
                                
                inimigo.tipo_atake  = randint(1,2)
                
                ini_dano_min = inimigo.dano - (inimigo.dano // 2)

                if inimigo.tipo_atake == 1 :
                    ini_dano_max = inimigo.dano 
                
                elif inimigo.tipo_atake == 2 :
                    ini_dano_max = inimigo.dano + 15


                usu_dano_total = randint(30,130 + (usuario.dano // 4))

                ini_dano_total = randint(ini_dano_min, ini_dano_max)

                usuario.hp -= ini_dano_total
                inimigo.hp -= usu_dano_total


                print('_-'*20)
                print(f'''O inimigo levou {usu_dano_total} De Dano
                HP inimigo {inimigo.hp}''')
                print('_-'*20)
                print(f'''Você levou {ini_dano_total} De Dano
                Seu HP {usuario.hp}''')
    
def arvore_de_evolução():

    arvore_de_abilidades.abilidades_fogo(usuario.level , usuario.pontos_de_abilidades, usuario )
    menu()

menu()
