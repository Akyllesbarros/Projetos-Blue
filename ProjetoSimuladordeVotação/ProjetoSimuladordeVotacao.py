# Projeto 04 - Simulador de votação:
# Crie um programa que simule um sistema de votação, ele deve receber votos até
# que o usuário diga que não tem mais ninguém para votar, esse programa precisa ter
# duas funções:

# A 1° Função precisa ser chamada autoriza_voto() ela vai receber como parâmetro o
# ano de nascimento de uma pessoa que será digitado pelo usuário, retornando um
# valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e
# OBRIGATÓRIO nas eleições.

# A 2° Função será a votacao(), ela vai receber dois parâmetros, autorização (que virá
# da função autoriza_voto()) e o voto que é o número que a pessoa votou.
# Se ela não puder votar, a 2° função terá que retornar “Você não pode votar”, caso o
# contrário a 2° função deve validar o número que a pessoa escolheu, ela pode
# escolher de 1 a 5 (crie 3 candidatos para a votação):
# ● 1, 2 ou 3 - Votos para os respectivos candidatos
# ● 4- Voto Nulo
# ● 5 - Voto em Branco
# Sua função votacao() tem que calcular e mostrar:
# ● O total de votos para cada candidato;
# ● O total de votos nulos;
# ● O total de votos em branco;
# ● Qual candidato venceu a votação



# Início



from collections import Counter # Biblioteca utilizada para listar elementos mais comuns e ordena.
import os                       # Biblioteca para limpar o terminal.
import time as tm               # Biblioteca para adicionar deley as ações. 
import pygame                   # Biblioteca para adicionar som.

# Busca e inicia o som. 

pygame.init()                           
pygame.mixer.music.load('turum.mp3')

# Cria lista ranking(lista de ordenação dos votos).
ranking = list()

# Cria lista de Dicionários alterável. 

    # O programa é maleável quanto a quantidade de candidatos e votos, logo, basta adicionar qualquer quantia de candidatos nessa lista que julgar necessário que o programa executa a contagem e apresentação normalmente. 

candidatos = [
    {
        'nome' : 'Bolsonaro',
        'numero' : 1,
        'votos' : 0
    },
    {
        'nome' : 'Lula',
        'numero' : 2,
        'votos' : 0
    },
    {
        'nome' : 'Luciano Hulk',
        'numero' : 3,
        'votos' : 0
    },
    {
        'nome' : 'Nulo',
        'numero' : 4,
        'votos' : 0
    },
    {
        'nome' : 'Branco',
        'numero' : 5,
        'votos' : 0
    }
]
    
# Função 'contarVoto()' realiza a contagem dos votos de cada candidato, e insere apenas o nome do candidato(com repetição) na lista. 
def contarVoto(voto): 
    global ranking   # transforma a variável 'ranking' em global para ser utilizada em outras funções. 
    
    for i, c in enumerate(candidatos):
    
        if candidatos[i]['numero'] == voto :
            candidatos[i]['votos'] += 1
            ranking.append(candidatos[i]['nome'])
            

# Função 'apurarVoto()' imprime a quantidade de votos de cada candidato, ordena a lista de ranking e imprime o candidato vencedor.
def apurarVotos() :
    
    for c in candidatos :
        print(f"Candidato: {c['nome']}\nvotos: {c['votos']}\n")
    for c in Counter(ranking).most_common(1) :
        print(f'O candidato {c[0]} venceu com {c[1]} votos válidos!')


# Função 'autorizaVoto' Calcula através da idade, a situação eleitoral do participante (negado, opcional, obrigatório). Se voto opcional, pergunta se deseja votar ou não. 
def autorizaVoto(anoNascimento) :
    idade = 2021 - anoNascimento
    if (idade >= 16 and idade < 18) or idade > 70 :
        print('Voto Opcional')
        opcao = int(input('Deseja votar?\n\n1 - SIM\n2 - NÃO\n'))
        os.system('cls')
        if opcao == 1 : 
            return True 
        else: 
            return False
    elif idade >= 18 and idade < 70 : 
        print('Seu voto é Voto Obrigatório!\n')
        return True 
    else: 
        print('Voto Negado, Me desculpe, você ainda não tem idade suficiente para votar :(')
        input('Tecle ENTER para continuar...')
        votar()
        return False


# Função 'continuarVotando()' Exibe menu e Pergunta ao usuário qual ação realizar ao final da votação. 
def continuarVotando() :
    continuar = int(input('O que deseja fazer?\n\n1 - Próximo voto\n2 - Encerrar Votação\n\n'))
    if continuar == 1 : 
        tm.sleep(0.5)
        os.system('cls')
        votar()
    else:
        os.system('cls')
        print('Apurando toda votação...')
        tm.sleep(2)
        apurarVotos()
        

# função votar, Função principal, Inicia o programa, e  ordena todas funções.
def votar() :
    os.system('cls')
    print('🗳️  Olá, você está em um simulador de votação 🗳️\n')
    tm.sleep(1)
    anoNascimento = int(input('Por favor, digite o seu ano de Nascimento:\n'))
    os.system('cls')

    if autorizaVoto(anoNascimento) == False : 
        return
    else:
        for i, c in enumerate(candidatos) : 
            print(f"{i+1} - {c['nome']}")


    voto = int(input('Por favor, escolha uma opção: '))
    print(f'Você escolheu a opção {voto}')
    contarVoto(voto)
    input('Digite ENTER para confirmar... ')
    pygame.mixer.music.play()
    os.system('cls')
    print('Contabilizando voto...')
    tm.sleep(2)
    print('Voto contabilizado! Obrigado por votar. ')
    continuarVotando()

# Chamando a função para executar o código. 
votar()