from random import randint

def abilidades_fogo(level, pontos, usuario):

    if pontos < 5:
        print('Você não tem mais pontos !')
        return 

    if level >= 5 :
        
        while True:
            pontos = usuario.pontos_de_abilidades
            print('-'*20)
            print('''Olá bem vindo a árvore de abilidades
            Seleciona a abilidade que quer desbloquia
_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
[0] Para sair ''')
            if 'Golpe De Fogo' in usuario.abilidades:
               pass
                
            else:
                print('[1] Golpe De Fogo { Dano_Padrão : 80/100 }')
                
            
            if 'Exploção de Fogo'  in usuario.abilidades:
                pass
                
            else:
                print('[2] Exploção De Fogo { Dano_Padrão : 30/130 })')
               
                

            if  not pontos < 5:

                try:
                    escolha = int(input('Escolha : '))
                
                except:
                    print('Digite novamente ...')
                
                else:

                    if escolha == 0 :
                        break

                   
                    if escolha == 1 :
                        if 'Golpe De Fogo' in usuario.abilidades :
                            print('Você já possui éssa abilidade')
                            abilidades_fogo(usuario.level , usuario.pontos_de_abilidades, usuario)

                        usuario.pontos_de_abilidades -= 5
                        
                        verificador = False                    
                        while verificador == False: 
                            botão_ataque = input('Digite o botão para ativar esse ataque : ')
                            
                            if botão_ataque in usuario.abilidades.values():
                                print('Esse botão está atribuido a outro ataque')
                            
                            else:
                                
                                usuario.abilidades['Golpe De Fogo'] = botão_ataque
                                verificador = True
                                

                    
                    if escolha == 2 :
                        
                        if 'Exploção De Fogo' in usuario.abilidades : 
                            print('Você já possui essa abilidade') 
                            print('deu ruim') 
                            abilidades_fogo(usuario.level , usuario.pontos_de_abilidades, usuario)
                        usuario.pontos_de_abilidades -= 5
                        
                        verificador = False
                        while verificador == False :
                            botão_ataque = input('Digite o botão para ativar esse ataque : ')

                            if botão_ataque in usuario.abilidades.values():
                                print('Esse botão está atribuido a outro ataque !!')
                                
                            else:
                                
                                usuario.abilidades['Exploção de Fogo'] = botão_ataque
                                verificador = True

            else:
                print('você não tem pontos !')
                break