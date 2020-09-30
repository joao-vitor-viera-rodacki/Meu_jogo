from time import sleep
from random import randint
from arvore_de_abilidades import abilidades_fogo
    
        
class Inimigo:
    def __init__(self):
        
        self.tipo_atake = NotImplemented
        self.level = 2
        self.dano  = (self.level // 2) * 10
        self.hp =  (self.level // 2) * 200




class Jogador:
    def __init__(self, nome):

        self.level = 6
        self.xp = 0
        self.dano  = (self.level // 2) * 10
        self.usu_dano_max = self.dano + 10
        self.usu_dano_min = self.dano

        self.abilidades = {
                              'Ataque Ariscado':{'botão': '1' , 'danoMAX': self.usu_dano_max + 100,'danoMIN': 0 },
                              'Ataque Magico de Gelo': {'botão': '2', 'danoMAX': self.usu_dano_max ,'danoMIN':self.usu_dano_min},
                              'Ataque Especial': {'botão': '3' ,'danoMAX': 200, 'danoMIN':0}
                              }
       
        self.botões_abilidades = { '1' : {'abilidade': 'Ataque Ariscado'},
                                   '2' : {'abilidade' : 'Ataque Magico De Gelo'},
                                   '3' : {'abilidade' : 'Ataque Especial'}}

        self.pontos_de_abilidades = 10
        self.hp = (self.level // 2) * 100
        self.nome = nome
        self.contagem_de_atake_especial = 2
    

usuario = Jogador('dragonogt')

inimigo = Inimigo()

def menu():
    

    while True:
        print('----'*20)
        print('''\033[1;32mSeja bem vindo !!\033[m
        \033[1;36m[1]\033[1;33m Para entrar em uma partida...
        \033[1;36m[2]\033[1;33m Para entrar em na arvore de evolução
        \033[1;36m[3]\033[1;33m Para ver status do jogador''')

        try:
            opção = int(input('Escolha : \033[m'))
            #import ipdb; ipdb.set_trace()
        except:
            print('\033[1;31m digite novamente...\033[m')
        
        else:
            if opção == 1:
                print('----'*20)
                partida()
                break
            
            elif opção == 2:
                print('----'*20)
               
                abilidades_fogo(usuario.level , usuario.pontos_de_abilidades, usuario)     
                menu()

            elif opção == 3:
                print('\033[1;34m_-'*20)
                print(f'''\033[1;33mNome :\033[m  \033[1;34m{usuario.nome}\033[m
                          \033[1;36mLevel:  {usuario.level}
                          Dano :  {usuario.dano}
                          HP   :  {usuario.hp}
                          Xp   :  {usuario.xp}
                          Pontos De Abilidades : {usuario.pontos_de_abilidades}
                          \033[m''')
                print('\033[4;33mAbilidades \033[m')
                print('\033[1;35m-='*20, '\033[m')
                for key , values  in usuario.abilidades.items():
                    
                    print(f'\033[1;32m{key} \033[1;34mDano {values["danoMAX"]}//{values["danoMIN"]}')
                    print('\033[1;33m-='*20, '\033[m')
                    
                print('\033[1;35m-='*20, '\033[m')

def partida():

    inimigo_hp_padrão = inimigo.hp
    usuario_hp_padrão = usuario.hp
    def recuperação():
        inimigo.hp = inimigo_hp_padrão
        usuario.hp = usuario_hp_padrão
        usuario.contagem_de_atake_especial = 2

    print('\033[1;32mEntrando na partida')
    print('1..')
    sleep(0.80)
    print('2..')
    sleep(0.80)
    print('3..')
    sleep(0.80)
    print('Já..\033[m')
    
    while True:
        while True:
                        
            if inimigo.hp <= 0 :
                print('===='* 20)
                print(f'\033[1;34mParabens {usuario.nome}. Você ganhou !!\033[m')
                
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
                    print('\033[1;33mVocê subio de nivel !!!\033[m')
                    print(f'\033[1;36mNivel atual {usuario.level}\033[m')

                menu()

            if usuario.hp <= 0 :
                recuperação()
                print(f'{usuario.nome} você perdeu. Tente Novamente.. ')

                menu()
            
            print('')
            print(f'''\033[4;33m Painel de skils''')
            print('_-'*20,'\033[m')
            print('')
            for key, values in usuario.abilidades.items():
                if key == 'Ataque Especial':
                    print(f'\033[1;31m [{values["botão"]}] ] ; \033[1;34m{key} [[ Dano Maximo {values["danoMAX"]}// Dano minimo {values["danoMIN"]}||{usuario.contagem_de_atake_especial} Ataques restantes...]]\033[m')
                else:
                    
                    print(f'\033[1;31m [{values["botão"]}] \033[33m] ; {key} [[ Dano Maximo {values["danoMAX"]}// Dano minimo {values["danoMIN"]}]]\033[m')
            print('')
            print('\033[4;33m_-'*20,'\033[m')           
            try:

                opção = str(input('Escolha : '))
                    
            except:
                print('Digite novamente...')
            
            else:
                atacar(opcao=opção)
            
            
        
def atacar(opcao=0):
    
    #import ipdb; ipdb.set_trace()
    if opcao == usuario.abilidades['Ataque Especial']['botão'] :

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
        
        print('\033[1;33m__-'*20)
        print(f'''\033[1;33mO inimigo levou \033[1;36m{usu_dano_total}\033[1;33m de da 
        HP Inimigo :: \033[1;36m{inimigo.hp}''')
        print('\033[1;33m__-'*20)
        print(f'''Você levou \033[1;36m{ini_dano_total}\033[1;33m De dano
        HP Seu :: \033[1;36m{usuario.hp}\033[m''')
        return
    if opcao == usuario.abilidades['Ataque Magico de Gelo']['botão']:

        
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
        
        print('\033[1;33m__-'*20)
        print(f'''\033[1;33mO inimigo levou \033[1;36m{usu_dano_total}\033[1;33m de da 
        HP Inimigo :: \033[1;36m{inimigo.hp}''')
        print('\033[1;33m__-'*20)
        print(f'''Você levou \033[1;36m{ini_dano_total}\033[1;33m De dano
        HP Seu :: \033[1;36m{usuario.hp}\033[m''')
        return
    if opcao == usuario.abilidades['Ataque Ariscado']['botão'] :
        
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

                print('\033[1;33m__-'*20)
                print(f'''\033[1;33mO inimigo levou \033[1;36m{usu_dano_total}\033[1;33m de da 
                HP Inimigo :: \033[1;36m{inimigo.hp}''')
                print('\033[1;33m__-'*20)
                print(f'''Você levou \033[1;36m{ini_dano_total}\033[1;33m De dano
                HP Seu :: \033[1;36m{usuario.hp}\033[m''')
                return  

    if 'Golpe De Fogo' in usuario.abilidades:
        
        if opcao == usuario.abilidades['Golpe De Fogo']['botão']:
                            
            inimigo.tipo_atake  = randint(1,2)
            
            ini_dano_min = inimigo.dano - (inimigo.dano // 2)

            if inimigo.tipo_atake == 1 :
                ini_dano_max = inimigo.dano 
            
            elif inimigo.tipo_atake == 2 :
                ini_dano_max = inimigo.dano + 15


            usu_dano_total = randint(30,90)

            ini_dano_total = randint(ini_dano_min, ini_dano_max)

            usuario.hp -= ini_dano_total
            inimigo.hp -= usu_dano_total


            print('\033[1;33m__-'*20)
            print(f'''\033[1;33mO inimigo levou \033[1;36m{usu_dano_total}\033[1;33m de da 
            HP Inimigo :: \033[1;36m{inimigo.hp}''')
            print('\033[1;33m__-'*20)
            print(f'''Você levou \033[1;36m{ini_dano_total}\033[1;33m De dano
            HP Seu :: \033[1;36m{usuario.hp}\033[m''')
            return  
    if 'Exploção De Fogo' in usuario.abilidades:
        
        if opcao == usuario.abilidades['Exploção De Fogo']['botão']:
                            
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


            print('\033[1;33m__-'*20)
            print(f'''\033[1;33mO inimigo levou \033[1;36m{usu_dano_total}\033[1;33m de da 
            HP Inimigo :: \033[1;36m{inimigo.hp}''')
            print('\033[1;33m__-'*20)
            print(f'''Você levou \033[1;36m{ini_dano_total}\033[1;33m De dano
            HP Seu :: \033[1;36m{usuario.hp}\033[m''')
            return  
menu()