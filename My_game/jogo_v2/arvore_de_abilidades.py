from random import randint


def abilidades_fogo(level, pontos, usuario):
    
    if pontos < 5:
        print('Você não tem mais pontos !')
        

    if level >= 5 :
        
        while True:

            print('-'*20)
            print('''Olá bem vindo a árvore de abilidades
            Seleciona a abilidade que quer desbloquia
_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
[0] Para sair ''')
            if 'Golpe De Fogo' in usuario.abilidades:
               pass
                
            else:
                print('[1] Golpe De Fogo { Dano_Padrão : 80/100 }')
                
            
            if 'Exploção De Fogo'  in usuario.abilidades:
                pass
                
            else:
                print('[2] Exploção De Fogo { Dano_Padrão : 30/130 })')
               

            try:
                escolha = int(input('Escolha : '))
            
            except:
                print('Digite novamente ...')
            
            else:

                if escolha == 0 :
                    return

                if escolha == 1 :
                    if 'Golpe De Fogo' in usuario.abilidades :
                        print('Você já possui éssa abilidade')
                        abilidades_fogo(usuario.level , usuario.pontos_de_abilidades , usuario)
                
                    verificador = False
                    while True:
                        if verificador == True:
                            break
                        
                        else:
                            usuario.pontos_de_abilidades -= 5
                            botão_ataque = str(input('Digite o botão para ativar esse ataque : '))

                            if botão_ataque not in usuario.botões_abilidades :
                                usuario.abilidades.update({'Golpe De Fogo' : {'botão' : botão_ataque, 'danoMAX': 90 + usuario.usu_dano_max // 2 , 'danoMIN' : 30 + usuario.usu_dano_min // 3}})
                                usuario.botões_abilidades.update({botão_ataque : { 'abilidade' : 'Golpe De Fogo'}})
                                print("Sua abilidade foi adquirida com sucesso !")
                                verificador = True

                            else:
                                print("Essa tecla já está ocupada  ! ")
   
                if escolha == 2 :
                    
                    if 'Exploção De Fogo' in usuario.abilidades : 
                        print('Você já possui essa abilidade') 
                        abilidades_fogo(usuario.level , usuario.pontos_de_abilidades, usuario)
                    
                    verificador = False
                    while True:
                        
                        if verificador == True:
                            break
                        else:
                            usuario.pontos_de_abilidades -= 5
                            botão_ataque = str(input('Digite o botão para ativar esse ataque : '))

                            if botão_ataque not in usuario.botões_abilidades:
                                usuario.abilidades.update({'Exploção De Fogo' : {'botão': botão_ataque , 'danoMAX':130 + usuario.dano // 4 , 'danoMIN':30}})
                                usuario.botões_abilidades.update({botão_ataque : {'abilidade' : 'Exploção De Fogo'}})
                                print("Sua abilidade foi adquirido com sucesso !")
                                verificador = True
                                
                            else:
                                print('Esse botão já está acupado !')

    else:
        print('Você não tem nivel para abilidades de fogo')