import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 1300
altura = 550

bgColor = (50,50,50)

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Dominó')

heuristicaUm = []
heuristicaUmPecas = []
meroMortal = []
meroMortalPecas = []

def redimensionaPecas(img, escala):
	s = pygame.transform.scale(img, (int(125*escala), int(225*escala)))	# baseado nas dimensões da imagem (peça do dominó)
	return s

def distribuiPecas_meroMortal():

	while True:
		n = randint(0,27)
		if len(meroMortal) == 14:
			break

		if n not in meroMortal and n not in heuristicaUm:
			meroMortal.append(n)

	for i in range(len(meroMortal)):
		a = meroMortal[i]
		meroMortalPecas.append(pecasMapeadas[a])

	return meroMortalPecas

def distribuiPecas_heuristicaUm():

	while True:
			n = randint(0,27)
			if len(heuristicaUm) == 14:
				break

			if n not in heuristicaUm and n not in meroMortal:
				heuristicaUm.append(n)

	for i in range(len(heuristicaUm)):
		a = heuristicaUm[i]
		heuristicaUmPecas.append(pecasMapeadas[a])

	return heuristicaUmPecas

def identificaNumerosNaPeca_Esquerda(peca):
	peca = peca.replace('(','').replace(')','').replace('\'','').replace(', ','')
	ladoEsquerdoIdentificado = peca[0]

	return int(ladoEsquerdoIdentificado)

def identificaNumerosNaPeca_Direita(peca):
	peca = peca.replace('(','').replace(')','').replace('\'','').replace(', ','')
	ladoDireitoIdentificado = peca[1]

	return int(ladoDireitoIdentificado)

def encontraIndiceEmPecas(aleatorio, pecaEsquerda, pecaDireita):

	if int(pecaEsquerda) == 0:
		indicePecas = pecaDireita

	if int(pecaEsquerda) == 1:
		s = str(pecaEsquerda) + str(pecaDireita)
		s = int(s)
		indicePecas = s - 4

	if int(pecaEsquerda) == 2:
		s = str(pecaEsquerda) + str(pecaDireita)
		s = int(s)
		indicePecas = s - 9

	if int(pecaEsquerda) == 3:
		s = str(pecaEsquerda) + str(pecaDireita)
		s = int(s)
		indicePecas = s - 15

	if int(pecaEsquerda) == 4:
		s = str(pecaEsquerda) + str(pecaDireita)
		s = int(s)
		indicePecas = s - 22

	if int(pecaEsquerda) == 5:
		s = str(pecaEsquerda) + str(pecaDireita)
		s = int(s)
		indicePecas = s - 30

	if int(pecaEsquerda) == 6:
		s = str(pecaEsquerda) + str(pecaDireita)
		s = int(s)
		indicePecas = s - 39

	return int(indicePecas)

zero_zero = pygame.image.load('peças/00.png')
zero_um = pygame.image.load('peças/01.png')
zero_dois = pygame.image.load('peças/02.png')
zero_tres = pygame.image.load('peças/03.png')
zero_quatro = pygame.image.load('peças/04.png')
zero_cinco = pygame.image.load('peças/05.png')
zero_seis = pygame.image.load('peças/06.png')
um_um = pygame.image.load('peças/11.png')
um_dois = pygame.image.load('peças/12.png')
um_tres = pygame.image.load('peças/13.png')
um_quatro = pygame.image.load('peças/14.png')
um_cinco = pygame.image.load('peças/15.png')
um_seis = pygame.image.load('peças/16.png')
dois_dois = pygame.image.load('peças/22.png')
dois_tres = pygame.image.load('peças/23.png')
dois_quatro = pygame.image.load('peças/24.png')
dois_cinco = pygame.image.load('peças/25.png')
dois_seis = pygame.image.load('peças/26.png')
tres_tres = pygame.image.load('peças/33.png')
tres_quatro = pygame.image.load('peças/34.png')
tres_cinco = pygame.image.load('peças/35.png')
tres_seis = pygame.image.load('peças/36.png')
quatro_quatro = pygame.image.load('peças/44.png')
quatro_cinco = pygame.image.load('peças/45.png')
quatro_seis = pygame.image.load('peças/46.png')
cinco_cinco = pygame.image.load('peças/55.png')
cinco_seis = pygame.image.load('peças/56.png')
seis_seis = pygame.image.load('peças/66.png')


zero_zero = redimensionaPecas(zero_zero, 0.35)
zero_um = redimensionaPecas(zero_um, 0.35)
zero_dois = redimensionaPecas(zero_dois, 0.35)
zero_tres = redimensionaPecas(zero_tres, 0.35)
zero_quatro = redimensionaPecas(zero_quatro, 0.35)
zero_cinco = redimensionaPecas(zero_cinco, 0.35)
zero_seis = redimensionaPecas(zero_seis, 0.35)
um_um = redimensionaPecas(um_um, 0.35)
um_dois = redimensionaPecas(um_dois, 0.35)
um_tres = redimensionaPecas(um_tres, 0.35)
um_quatro = redimensionaPecas(um_quatro, 0.35)
um_cinco = redimensionaPecas(um_cinco, 0.35)
um_seis = redimensionaPecas(um_seis, 0.35)
dois_dois = redimensionaPecas(dois_dois, 0.35)
dois_tres = redimensionaPecas(dois_tres, 0.35)
dois_quatro = redimensionaPecas(dois_quatro, 0.35)
dois_cinco = redimensionaPecas(dois_cinco, 0.35)
tres_tres = redimensionaPecas(tres_tres, 0.35)
tres_quatro = redimensionaPecas(tres_quatro, 0.35)
tres_cinco = redimensionaPecas(tres_cinco, 0.35)
tres_seis = redimensionaPecas(tres_seis, 0.35)
quatro_quatro = redimensionaPecas(quatro_quatro, 0.35)
quatro_cinco = redimensionaPecas(quatro_cinco, 0.35)
quatro_seis = redimensionaPecas(quatro_seis, 0.35)
cinco_cinco = redimensionaPecas(cinco_cinco, 0.35)
cinco_seis = redimensionaPecas(cinco_seis, 0.35)
seis_seis = redimensionaPecas(seis_seis, 0.35)


pecas = []
pecas.append(zero_zero)			#0
pecas.append(zero_um)			#1
pecas.append(zero_dois)			#2
pecas.append(zero_tres)			#3
pecas.append(zero_quatro)		#4
pecas.append(zero_cinco)		#5
pecas.append(zero_seis)			#6
pecas.append(um_um)				#7			-4
pecas.append(um_dois)			#8
pecas.append(um_tres)			#9
pecas.append(um_quatro)			#10
pecas.append(um_cinco)			#11
pecas.append(um_seis)			#12
pecas.append(dois_dois)			#13			-9
pecas.append(dois_tres)			#14
pecas.append(dois_quatro)		#15
pecas.append(dois_cinco)		#16
pecas.append(dois_seis)			#17
pecas.append(tres_tres)			#18			-15
pecas.append(tres_quatro)		#19
pecas.append(tres_cinco)		#20
pecas.append(tres_seis)			#21
pecas.append(quatro_quatro)		#22			-22
pecas.append(quatro_cinco)		#23
pecas.append(quatro_seis)		#24
pecas.append(cinco_cinco)		#25			-30
pecas.append(cinco_seis)		#26
pecas.append(seis_seis)			#27			-39



pecasMapeadas = [
					('0', '0'),
					('0', '1'),
					('0', '2'),
					('0', '3'),
					('0', '4'),
					('0', '5'),
					('0', '6'),
					('1', '1'),
					('1', '2'),
					('1', '3'),
					('1', '4'),
					('1', '5'),
					('1', '6'),
					('2', '2'),
					('2', '3'),
					('2', '4'),
					('2', '5'),
					('2', '6'),
					('3', '3'),
					('3', '4'),
					('3', '5'),
					('3', '6'),
					('4', '4'),
					('4', '5'),
					('4', '6'),
					('5', '5'),
					('5', '6'),
					('6', '6')
]


pecasMeroMortal = distribuiPecas_meroMortal()
pecasHeuristicaUm = distribuiPecas_heuristicaUm()

print()
print(f'peças de Mero mortal: {pecasMeroMortal}')
print()
print(f'peças de Heurística 1: {pecasHeuristicaUm}')

# print(f'teste: peça nº 7 de meroMortal {pecasMeroMortal[0]}')
# print(f'teste: peça nº 7 de heuristicaUm {pecasHeuristicaUm[0]}')



relogio = pygame.time.Clock()
tela.fill(bgColor)

pecasJogadas = [] # peças que já foram jogadas e que não podem se repetir na mesa
jogoIniciado = False
proximaJogada = False
proximaJogadaLiberada = False
pecaRecenteEmPe = False
encerrarJogo = False
meroMortalPodeJogar = False
heuristicaUmPodeJogar = False
numeroJogadas = 0

while True:
	relogio.tick(30)
	# tela.fill(bgColor)
	for event in pygame.event.get():
		# encerra o jogo ao fechar a janela
		if event.type == QUIT: 
			pygame.quit()
			exit()
		
		# ação ao pressionar qualquer tecla
		if event.type == KEYDOWN: 
			if event.key == K_m:
				# próxima jogada
				if jogoIniciado == True and proximaJogada == True:

					if numeroJogadas == 28 or encerrarJogo == True:
						print()
						print('- - -')
						print('Fim de jogo.')
						print()
						break

					proximaJogadaLiberada = True
					while proximaJogadaLiberada == True and encerrarJogo == False and meroMortalPodeJogar == True:

						escolheLado = randint(0,1) 
						if escolheLado == 0: # lado esquerdo
							
							for i in range(14):

								# encontra o "match"
							
								# isola cada lado da peça em variáveis
								peca_Esquerda = identificaNumerosNaPeca_Esquerda(str(pecasMeroMortal[i]))
								peca_Direita = identificaNumerosNaPeca_Direita(str(pecasMeroMortal[i]))

								# encontra o índice para mapear a peça escolhida aleatoriamente na lista "pecas[]"
								indicePecas = encontraIndiceEmPecas(i, peca_Esquerda, peca_Direita)

								if ladoEsquerdoDaUltimaPecaJogada == peca_Esquerda:

									# print(f'Achei {pecasMeroMortal[i]}')

									# impede que uma peça na mesa seja jogada novamente	
									if pecasMeroMortal[i] not in pecasJogadas:
										
										ladoDireitoDaPecaAtual = peca_Direita
										ladoEsquerdoDaPecaAtual = peca_Esquerda

										# deixa "em pé" se a peça for uma carroça
										if ladoEsquerdoDaPecaAtual == ladoDireitoDaPecaAtual: 
											img = pecas[indicePecas].copy()
											# img = pygame.transform.rotate(img,90)					# gira a peça
											posicaoX_esquerdo =  posicaoX_esquerdo + 30
											pecaRecenteEmPe = True
											tela.blit(img, (posicaoX_esquerdo, 230))				# posiciona a imagem na tela
											posicaoX_esquerdo = posicaoX_esquerdo - int(125//2.958)	# atualiza posição de X para a próxima peça
											pecasJogadas.append(pecasMeroMortal[i])					# adiciona a peça à lista das peças jogadas
											print(f'Peças jogadas: {pecasJogadas}')
											ladoEsquerdoDaUltimaPecaJogada = ladoEsquerdoDaPecaAtual
											print(f'lado esquerdo da ultima peça jogada: {ladoEsquerdoDaUltimaPecaJogada}')
											proximaJogadaLiberada = False
											# print('saindo do while...')
											numeroJogadas = numeroJogadas + 1
											print(f'numero de peças na mesa: {numeroJogadas}')
											print('-')
											break
										else:
											# deixa "deitada" se a peça não for uma carroça
											img = pecas[indicePecas].copy()
											img = pygame.transform.rotate(img,-90) # aqui a imagem gira 90º para seguir o "match" no lado esquerdo
											
											# ajuste para encaixar a peça deitada quando a anterior ficou em pé
											if pecaRecenteEmPe == True:
												posicaoX_esquerdo =  posicaoX_esquerdo - 30
												pecaRecenteEmPe = False

											tela.blit(img, (posicaoX_esquerdo, 250))
											posicaoX_esquerdo = posicaoX_esquerdo - int(225//2.958)
											pecasJogadas.append(pecasMeroMortal[i])
											print(f'Peças jogadas: {pecasJogadas}')
											ladoEsquerdoDaUltimaPecaJogada = ladoDireitoDaPecaAtual # invertido, pois aqui a peça girou
											print(f'lado esquerdo da ultima peça jogada: {ladoEsquerdoDaUltimaPecaJogada}')
											proximaJogadaLiberada = False
											# print('saindo do while...')
											numeroJogadas = numeroJogadas + 1
											print(f'numero de peças na mesa: {numeroJogadas}')
											print('-')
											break
									# else:
									# 	print(f'Esquerda 1: achei {pecasMeroMortal[i]}, mas já está na mesa.')

								# encontra o "match"
								if ladoEsquerdoDaUltimaPecaJogada == peca_Direita:
									# print(f'Achei {pecasMeroMortal[i]}')

									# impede que uma peça na mesa seja jogada novamente	
									if pecasMeroMortal[i] not in pecasJogadas:
										
										ladoDireitoDaPecaAtual = peca_Direita
										ladoEsquerdoDaPecaAtual = peca_Esquerda

										# deixa "em pé" se a peça for uma carroça
										if ladoEsquerdoDaPecaAtual == ladoDireitoDaPecaAtual: 
											img = pecas[indicePecas].copy()
											# img = pygame.transform.rotate(img,90)					# gira a peça
											posicaoX_esquerdo =  posicaoX_esquerdo + 30
											pecaRecenteEmPe = True
											tela.blit(img, (posicaoX_esquerdo, 230))				# posiciona a imagem na tela
											posicaoX_esquerdo = posicaoX_esquerdo - int(125//2.958)	# atualiza posição de X para a próxima peça
											pecasJogadas.append(pecasMeroMortal[i])					# adiciona a peça à lista das peças jogadas
											print(f'Peças jogadas: {pecasJogadas}')
											ladoEsquerdoDaUltimaPecaJogada = ladoEsquerdoDaPecaAtual
											print(f'lado esquerdo da ultima peça jogada: {ladoEsquerdoDaUltimaPecaJogada}')
											proximaJogadaLiberada = False
											# print('saindo do while...')
											numeroJogadas = numeroJogadas + 1
											print(f'numero de peças na mesa: {numeroJogadas}')
											print('-')
											break
										else:
											# deixa "deitada" se a peça não for uma carroça
											img = pecas[indicePecas].copy()
											img = pygame.transform.rotate(img,90) # aqui a imagem gira 90º para seguir o "match" no lado esquerdo
											
											# ajuste para encaixar a peça deitada quando a anterior ficou em pé
											if pecaRecenteEmPe == True:
												posicaoX_esquerdo =  posicaoX_esquerdo - 30
												pecaRecenteEmPe = False

											tela.blit(img, (posicaoX_esquerdo, 250))
											posicaoX_esquerdo = posicaoX_esquerdo - int(225//2.958)
											pecasJogadas.append(pecasMeroMortal[i])
											print(f'Peças jogadas: {pecasJogadas}')
											ladoEsquerdoDaUltimaPecaJogada = ladoEsquerdoDaPecaAtual # sentido normal, já que neste ponto está ocorrendo uma comparação com o elemento 1
											print(f'lado esquerdo da ultima peça jogada: {ladoEsquerdoDaUltimaPecaJogada}')
											proximaJogadaLiberada = False
											# print('saindo do while...')
											numeroJogadas = numeroJogadas + 1
											print(f'numero de peças na mesa: {numeroJogadas}')
											print('-')
											break
									# else:
									# 	# chegar neste ponto significa que não há mais jogadas e o último que jogou a peça ganhou o jogo
									# 	# print(f'Esquerda 2: achei {pecasMapeadas[i]}, mas já está na mesa.')
									# 	print('Alguém teria vencido?')
									# 	encerrarJogo = True
									# 	break

						
						if escolheLado == 1: # lado direito
							
							for i in range(14):
								
								# encontra o "match"

								# isola cada lado da peça em variáveis
								peca_Esquerda = identificaNumerosNaPeca_Esquerda(str(pecasMeroMortal[i]))
								peca_Direita = identificaNumerosNaPeca_Direita(str(pecasMeroMortal[i]))

								# encontra o índice para mapear a peça escolhida aleatoriamente na lista "pecas[]"
								indicePecas = encontraIndiceEmPecas(i, peca_Esquerda, peca_Direita)


								if ladoDireitoDaUltimaPecaJogada == peca_Direita:
									# print(f'Achei {pecasMeroMortal[i]}')
									
									# impede que uma peça na mesa seja jogada novamente	
									if pecasMeroMortal[i] not in pecasJogadas:
										
										ladoDireitoDaPecaAtual = peca_Direita
										ladoEsquerdoDaPecaAtual = peca_Esquerda
										
										# deixa "em pé" se a peça for uma carroça
										if ladoEsquerdoDaPecaAtual == ladoDireitoDaPecaAtual:
											img = pecas[indicePecas].copy()
											tela.blit(img, (posicaoX_direito, 230))
											posicaoX_esquerdo = posicaoX_esquerdo + int(125//2.958)
											pecasJogadas.append(pecasMeroMortal[i])
											print(f'Peças jogadas: {pecasJogadas}')
											ladoDireitoDaUltimaPecaJogada = ladoDireitoDaPecaAtual
											print(f'lado direito da ultima peça jogada: {ladoDireitoDaUltimaPecaJogada}')
											proximaJogadaLiberada = False
											# print('saindo do while...')
											numeroJogadas = numeroJogadas + 1
											print(f'numero de peças na mesa: {numeroJogadas}')
											print('-')
											break
										else:
											# deixa "deitada" se a peça não for uma carroça
											img = pecas[indicePecas].copy()
											img = pygame.transform.rotate(img,-90)
											tela.blit(img, (posicaoX_direito, 250))
											posicaoX_direito = posicaoX_direito + int(225//2.958)
											pecasJogadas.append(pecasMeroMortal[i])
											print(f'Peças jogadas: {pecasJogadas}')
											ladoDireitoDaUltimaPecaJogada = ladoEsquerdoDaPecaAtual	# invertido, pois aqui a peça girou
											print(f'lado direito da ultima peça jogada: {ladoDireitoDaUltimaPecaJogada}')
											proximaJogadaLiberada = False
											# print('saindo do while...')
											numeroJogadas = numeroJogadas + 1
											print(f'numero de peças na mesa: {numeroJogadas}')
											print('-')
											break
									else:
										print(f'Direita 1: achei {pecasMeroMortal[i]}, mas já está na mesa.')


								if ladoDireitoDaUltimaPecaJogada == peca_Esquerda:
									# print(f'Achei {pecasMeroMortal[i]}')
									
									# impede que uma peça na mesa seja jogada novamente	
									if pecasMeroMortal[i] not in pecasJogadas:
										
										ladoDireitoDaPecaAtual = pecasMeroMortal[i][0]
										ladoEsquerdoDaPecaAtual = pecasMeroMortal[i][1]
										
										# deixa "em pé" se a peça for uma carroça
										if ladoEsquerdoDaPecaAtual == ladoDireitoDaPecaAtual:
											img = pecas[indicePecas].copy()
											tela.blit(img, (posicaoX_direito, 230))
											posicaoX_esquerdo = posicaoX_esquerdo + int(125//2.958)
											pecasJogadas.append(pecasMeroMortal[i])
											print(f'Peças jogadas: {pecasJogadas}')
											ladoDireitoDaUltimaPecaJogada = ladoDireitoDaPecaAtual
											print(f'lado direito da ultima peça jogada: {ladoDireitoDaUltimaPecaJogada}')
											proximaJogadaLiberada = False
											# print('saindo do while...')
											numeroJogadas = numeroJogadas + 1
											print(f'numero de peças na mesa: {numeroJogadas}')
											print('-')
											break
										else:
											# deixa "deitada" se a peça não for uma carroça
											img = pecas[indicePecas].copy()
											img = pygame.transform.rotate(img,90)
											tela.blit(img, (posicaoX_direito, 250))
											posicaoX_direito = posicaoX_direito + int(225//2.958)
											pecasJogadas.append(pecasMeroMortal[i])
											print(f'Peças jogadas: {pecasJogadas}')
											ladoDireitoDaUltimaPecaJogada = ladoDireitoDaPecaAtual	# sentido normal, já que neste ponto está ocorrendo uma comparação com o elemento 0
											print(f'lado direito da ultima peça jogada: {ladoDireitoDaUltimaPecaJogada}')
											proximaJogadaLiberada = False
											# print('saindo do while...')
											numeroJogadas = numeroJogadas + 1
											print(f'numero de peças na mesa: {numeroJogadas}')
											print('-')
											break
									else:
										# chegar neste ponto significa que não há mais jogadas e o último que jogou a peça ganhou o jogo
										# print(f'Direita 2: achei {pecasMapeadas[i]}, mas já está na mesa.')
										print('Alguém teria vencido?')
										encerrarJogo = True
										break

					proximaJogada = True
					meroMortalPodeJogar = False
					print('meroMortal acabou de jogar.')
					heuristicaUmPodeJogar = True

		# ação ao pressionar qualquer tecla
		if event.type == KEYDOWN:
			if event.key == K_h: 
				# próxima jogada
				if jogoIniciado == True and proximaJogada == True:

					if numeroJogadas == 28 or encerrarJogo == True:
						print()
						print('- - -')
						print('Fim de jogo.')
						print()
						break

					proximaJogadaLiberada = True

					while proximaJogadaLiberada == True and encerrarJogo == False and heuristicaUmPodeJogar == True:

						escolheLado = randint(0,1) 
						if escolheLado == 0: # lado esquerdo
							
							for i in range(14):

								# encontra o "match"

								# isola cada lado da peça em variáveis
								peca_Esquerda = identificaNumerosNaPeca_Esquerda(str(pecasHeuristicaUm[i]))
								peca_Direita = identificaNumerosNaPeca_Direita(str(pecasHeuristicaUm[i]))

								# encontra o índice para mapear a peça escolhida aleatoriamente na lista "pecas[]"
								indicePecas = encontraIndiceEmPecas(i, peca_Esquerda, peca_Direita)


								if ladoEsquerdoDaUltimaPecaJogada == peca_Esquerda: # compara com o elemento 0
									# print(f'Achei {pecasHeuristicaUm[i]}')

									# impede que uma peça na mesa seja jogada novamente	
									if pecasHeuristicaUm[i] not in pecasJogadas:
										
										ladoDireitoDaPecaAtual = peca_Direita
										ladoEsquerdoDaPecaAtual = peca_Esquerda

										# deixa "em pé" se a peça for uma carroça
										if ladoEsquerdoDaPecaAtual == ladoDireitoDaPecaAtual: 
											img = pecas[indicePecas].copy()
											# img = pygame.transform.rotate(img,90)					# gira a peça
											posicaoX_esquerdo =  posicaoX_esquerdo + 30
											pecaRecenteEmPe = True
											tela.blit(img, (posicaoX_esquerdo, 230))				# posiciona a imagem na tela
											posicaoX_esquerdo = posicaoX_esquerdo - int(125//2.958)	# atualiza posição de X para a próxima peça
											pecasJogadas.append(pecasHeuristicaUm[i])				# adiciona a peça à lista das peças jogadas
											print(f'Peças jogadas: {pecasJogadas}')
											ladoEsquerdoDaUltimaPecaJogada = ladoEsquerdoDaPecaAtual
											print(f'lado esquerdo da ultima peça jogada: {ladoEsquerdoDaUltimaPecaJogada}')
											proximaJogadaLiberada = False
											# print('saindo do while...')
											numeroJogadas = numeroJogadas + 1
											print(f'numero de peças na mesa: {numeroJogadas}')
											print('-')
											break
										else:
											# deixa "deitada" se a peça não for uma carroça
											img = pecas[indicePecas].copy()
											img = pygame.transform.rotate(img,-90) # aqui a imagem gira 90º para seguir o "match" no lado esquerdo
											
											# ajuste para encaixar a peça deitada quando a anterior ficou em pé
											if pecaRecenteEmPe == True:
												posicaoX_esquerdo =  posicaoX_esquerdo - 30
												pecaRecenteEmPe = False

											tela.blit(img, (posicaoX_esquerdo, 250))
											posicaoX_esquerdo = posicaoX_esquerdo - int(225//2.958)
											pecasJogadas.append(pecasHeuristicaUm[i])
											print(f'Peças jogadas: {pecasJogadas}')
											ladoEsquerdoDaUltimaPecaJogada = ladoDireitoDaPecaAtual # invertido, pois aqui a peça girou
											print(f'lado esquerdo da ultima peça jogada: {ladoEsquerdoDaUltimaPecaJogada}')
											proximaJogadaLiberada = False
											# print('saindo do while...')
											numeroJogadas = numeroJogadas + 1
											print(f'numero de peças na mesa: {numeroJogadas}')
											print('-')
											break
									# else:
									# 	print(f'Esquerda 1: achei {pecasHeuristicaUm[i]}, mas já está na mesa.')

								# encontra o "match"
								if ladoEsquerdoDaUltimaPecaJogada == peca_Direita: # compara com o elemento 1
									# print(f'Achei {pecasHeuristicaUm[i]}')

									# impede que uma peça na mesa seja jogada novamente	
									if pecasHeuristicaUm[i] not in pecasJogadas:
										
										ladoDireitoDaPecaAtual = peca_Direita
										ladoEsquerdoDaPecaAtual = peca_Esquerda

										# deixa "em pé" se a peça for uma carroça
										if ladoEsquerdoDaPecaAtual == ladoDireitoDaPecaAtual: 
											img = pecas[indicePecas].copy()
											# img = pygame.transform.rotate(img,90)					# gira a peça
											posicaoX_esquerdo =  posicaoX_esquerdo + 30
											pecaRecenteEmPe = True
											tela.blit(img, (posicaoX_esquerdo, 230))				# posiciona a imagem na tela
											posicaoX_esquerdo = posicaoX_esquerdo - int(125//2.958)	# atualiza posição de X para a próxima peça
											pecasJogadas.append(pecasHeuristicaUm[i])					# adiciona a peça à lista das peças jogadas
											print(f'Peças jogadas: {pecasJogadas}')
											ladoEsquerdoDaUltimaPecaJogada = ladoEsquerdoDaPecaAtual
											print(f'lado esquerdo da ultima peça jogada: {ladoEsquerdoDaUltimaPecaJogada}')
											proximaJogadaLiberada = False
											# print('saindo do while...')
											numeroJogadas = numeroJogadas + 1
											print(f'numero de peças na mesa: {numeroJogadas}')
											print('-')
											break
										else:
											# deixa "deitada" se a peça não for uma carroça
											img = pecas[indicePecas].copy()
											img = pygame.transform.rotate(img,90) # aqui a imagem gira 90º para seguir o "match" no lado esquerdo
											
											# ajuste para encaixar a peça deitada quando a anterior ficou em pé
											if pecaRecenteEmPe == True:
												posicaoX_esquerdo =  posicaoX_esquerdo - 30
												pecaRecenteEmPe = False

											tela.blit(img, (posicaoX_esquerdo, 250))
											posicaoX_esquerdo = posicaoX_esquerdo - int(225//2.958)
											pecasJogadas.append(pecasHeuristicaUm[i])
											print(f'Peças jogadas: {pecasJogadas}')
											ladoEsquerdoDaUltimaPecaJogada = ladoEsquerdoDaPecaAtual # sentido normal, já que neste ponto está ocorrendo uma comparação com o elemento 1
											print(f'lado esquerdo da ultima peça jogada: {ladoEsquerdoDaUltimaPecaJogada}')
											proximaJogadaLiberada = False
											# print('saindo do while...')
											numeroJogadas = numeroJogadas + 1
											print(f'numero de peças na mesa: {numeroJogadas}')
											print('-')
											break
									# else:
									# 	# chegar neste ponto significa que não há mais jogadas e o último que jogou a peça ganhou o jogo
									# 	# print(f'Esquerda 2: achei {pecasMapeadas[i]}, mas já está na mesa.')
									# 	print('Alguém teria vencido?')
									# 	encerrarJogo = True
									# 	break

						
						if escolheLado == 1: # lado direito
							
							for i in range(14):
								
								# encontra o "match"
								if ladoDireitoDaUltimaPecaJogada == peca_Direita: # compara com o elemento 1
									# print(f'Achei {pecasHeuristicaUm[i]}')
									
									# impede que uma peça na mesa seja jogada novamente	
									if pecasHeuristicaUm[i] not in pecasJogadas:
										
										ladoDireitoDaPecaAtual = peca_Direita
										ladoEsquerdoDaPecaAtual = peca_Esquerda
										
										# deixa "em pé" se a peça for uma carroça
										if ladoEsquerdoDaPecaAtual == ladoDireitoDaPecaAtual:
											img = pecas[indicePecas].copy()
											tela.blit(img, (posicaoX_direito, 230))
											posicaoX_esquerdo = posicaoX_esquerdo + int(125//2.958)
											pecasJogadas.append(pecasHeuristicaUm[i])
											print(f'Peças jogadas: {pecasJogadas}')
											ladoDireitoDaUltimaPecaJogada = ladoDireitoDaPecaAtual
											print(f'lado direito da ultima peça jogada: {ladoDireitoDaUltimaPecaJogada}')
											proximaJogadaLiberada = False
											# print('saindo do while...')
											numeroJogadas = numeroJogadas + 1
											print(f'numero de peças na mesa: {numeroJogadas}')
											print('-')
											break
										else:
											# deixa "deitada" se a peça não for uma carroça
											img = pecas[indicePecas].copy()
											img = pygame.transform.rotate(img,-90)
											tela.blit(img, (posicaoX_direito, 250))
											posicaoX_direito = posicaoX_direito + int(225//2.958)
											pecasJogadas.append(pecasHeuristicaUm[i])
											print(f'Peças jogadas: {pecasJogadas}')
											ladoDireitoDaUltimaPecaJogada = ladoEsquerdoDaPecaAtual	# invertido, pois aqui a peça girou
											print(f'lado direito da ultima peça jogada: {ladoDireitoDaUltimaPecaJogada}')
											proximaJogadaLiberada = False
											# print('saindo do while...')
											numeroJogadas = numeroJogadas + 1
											print(f'numero de peças na mesa: {numeroJogadas}')
											print('-')
											break
									else:
										print(f'Direita 1: achei {pecasHeuristicaUm[i]}, mas já está na mesa.')


								if ladoDireitoDaUltimaPecaJogada == peca_Esquerda: # compara com o elemento 0
									# print(f'Achei {pecasHeuristicaUm[i]}')
									
									# impede que uma peça na mesa seja jogada novamente	
									if pecasHeuristicaUm[i] not in pecasJogadas:
										
										ladoDireitoDaPecaAtual = peca_Direita
										ladoEsquerdoDaPecaAtual = peca_Esquerda
										
										# deixa "em pé" se a peça for uma carroça
										if ladoEsquerdoDaPecaAtual == ladoDireitoDaPecaAtual:
											img = pecas[indicePecas].copy()
											tela.blit(img, (posicaoX_direito, 230))
											posicaoX_esquerdo = posicaoX_esquerdo + int(125//2.958)
											pecasJogadas.append(pecasHeuristicaUm[i])
											print(f'Peças jogadas: {pecasJogadas}')
											ladoDireitoDaUltimaPecaJogada = ladoDireitoDaPecaAtual
											print(f'lado direito da ultima peça jogada: {ladoDireitoDaUltimaPecaJogada}')
											proximaJogadaLiberada = False
											# print('saindo do while...')
											numeroJogadas = numeroJogadas + 1
											print(f'numero de peças na mesa: {numeroJogadas}')
											print('-')
											break
										else:
											# deixa "deitada" se a peça não for uma carroça
											img = pecas[indicePecas].copy()
											img = pygame.transform.rotate(img,90)
											tela.blit(img, (posicaoX_direito, 250))
											posicaoX_direito = posicaoX_direito + int(225//2.958)
											pecasJogadas.append(pecasHeuristicaUm[i])
											print(f'Peças jogadas: {pecasJogadas}')
											ladoDireitoDaUltimaPecaJogada = ladoDireitoDaPecaAtual	# sentido normal, já que neste ponto está ocorrendo uma comparação com o elemento 0
											print(f'lado direito da ultima peça jogada: {ladoDireitoDaUltimaPecaJogada}')
											proximaJogadaLiberada = False
											# print('saindo do while...')
											numeroJogadas = numeroJogadas + 1
											print(f'numero de peças na mesa: {numeroJogadas}')
											print('-')
											break
									else:
										# chegar neste ponto significa que não há mais jogadas e o último que jogou a peça ganhou o jogo
										# print(f'Direita 2: achei {pecasMapeadas[i]}, mas já está na mesa.')
										print('Alguém teria vencido?')
										encerrarJogo = True
										break

					proximaJogada = True
					meroMortalPodeJogar = True
					print('heuristicaUm acabou de jogar.')
					heuristicaUmPodeJogar = False






				
	
	# jogada inicial
	if jogoIniciado == False and proximaJogada == False:
		# escolhe uma peça aleatoriamente
		primeiraJogada = randint(0,14)
		
		# isola cada lado da peça em variáveis
		primeiraJogada_Esquerda = identificaNumerosNaPeca_Esquerda(str(pecasHeuristicaUm[primeiraJogada]))
		primeiraJogada_Direita = identificaNumerosNaPeca_Direita(str(pecasHeuristicaUm[primeiraJogada]))

		# encontra o índice para mapear a peça escolhida aleatoriamente na lista "pecas[]"
		indicePecas = encontraIndiceEmPecas(primeiraJogada, primeiraJogada_Esquerda, primeiraJogada_Direita)

		imgRect = pecas[indicePecas].get_rect(center = tela.get_rect().center)		# centraliza a peça na tela
		img = pecas[indicePecas].copy()												# faz uma cópia da imagem (peça) para não haver distorção ao girar
		img = pygame.transform.rotate(img,90)										# gira a imagem
		# tela.blit(img, imgRect)
		tela.blit(img, (555, 250))													# posiciona a imagem da peça na tela
		pecasJogadas.append(pecasHeuristicaUm[primeiraJogada])
		posicaoX_esquerdo = 468
		posicaoX_direito = 642
		jogoIniciado = True
		proximaJogada = True
		proximaJogadaLiberada = True
		meroMortalPodeJogar = True
		heuristicaUmPodeJogar = False
		numeroJogadas = numeroJogadas + 1
		print(f'Peças jogadas: {pecasJogadas}')
		print(f'numero de peças na mesa: {numeroJogadas}')
		print('-')

		ladoDireitoDaUltimaPecaJogada = int(primeiraJogada_Direita)
		ladoEsquerdoDaUltimaPecaJogada = int(primeiraJogada_Esquerda)
		print(f'lado esquerdo da ultima peça jogada: {int(primeiraJogada_Esquerda)}')
		print(f'lado direito da ultima peça jogada: {int(primeiraJogada_Direita)}')

		

	pygame.display.flip()




