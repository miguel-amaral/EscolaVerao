import random
class bcolors:
	ANSI_RESET =  "\033[0m"
	ANSI_BLACK =  "\033[30m"
	ANSI_RED =    "\033[31m"
	ANSI_GREEN =  "\033[32m"
	ANSI_YELLOW = "\033[33m"
	ANSI_BLUE =   "\033[34m"
	ANSI_PURPLE = "\033[35m"
	ANSI_CYAN =   "\033[36m"
	ANSI_WHITE =  "\033[37m"
	ANSI_BOLD =   "\033[1m"

def resetColour():
	print(bcolors.ANSI_RESET, end="")

def desenhaLinhaCima():
	print("    0 1 2 3 4 5 6 7 8 9 ")
	print("  ┏", end="")
	for i in range(21):
		print("━", end="")
	print("┓")

def desenhaLinhaBaixo():
	print("  ┗", end="")
	for i in range(21):
		print("━", end="")
	print("┛")

def desenhaTabuleiro(tabuleiro):
	colourCode = ""
	numLinha = 0
	desenhaLinhaCima()
	for linha in tabuleiro:
		print(numLinha, end=" ")
		print("┃", end="")

		for coluna in linha:
			print("", end=" ")
			if(coluna == -1):
				colourCode = bcolors.ANSI_BLUE
			elif(coluna == 1):
				colourCode = bcolors.ANSI_RED
			else:
				colourCode = bcolors.ANSI_BLACK
			print(colourCode , "X", end="", sep="")
			resetColour()


		print(" ┃")
		numLinha = numLinha + 1
	desenhaLinhaBaixo()

def desenhaTabuleiroDescoberto(tabuleiro):
	colourCode = ""
	numLinha = 0
	desenhaLinhaCima()
	for linha in tabuleiro:
		print(numLinha, end=" ")
		print("┃", end="")

		for coluna in linha:
			print("", end=" ")
			if(coluna == -1):
				colourCode = bcolors.ANSI_BLUE
			elif(coluna == 1):
				colourCode = bcolors.ANSI_RED
			elif(coluna == 0):
				colourCode = bcolors.ANSI_BLUE
			else:
				colourCode = bcolors.ANSI_YELLOW
			print(colourCode , "X", end="", sep="")
			resetColour()


		print(" ┃")
		numLinha = numLinha + 1
	desenhaLinhaBaixo()


'''
lista de listas com inteiros
-1 tiro disparado sem barco
 0 agua
 1 barco, danificado
 numero > 2 barco, sem danos
'''
def criaTabuleiro():
	return [[0,0,0,0,0,0,0,0,0,0] for i in range(10)]

def pedeJogada():
	bool = True
	while(bool):
		linha  = input("Qual a linha? [0-9]: ")
		coluna = input("Qual a coluna?[0-9]: ")
		if(not linha.isdigit() or not coluna.isdigit() or int(linha) > 9 or int(coluna) > 9 or int(linha) < 0 or int(coluna) < 0):
			print("Por favor apenas numeros entre 0 e 9 sao permitidos.")
		else:
			bool = False
	return (int(linha),int(coluna))

def tabuleiroCompleto(tabuleiro):
	for linha in tabuleiro:
		for coluna in linha:
			if(coluna > 1):
				return False #Ainda ha pelo menos um barco sem estar danificado
	return True

def barcoAbatido(tabuleiro,barco):
	for linha in tabuleiro:
		for coluna in linha:
			if(coluna == barco):
				return False #Ainda ha pelo menos um barco sem estar danificado
	return True

def dispararTiro(tabuleiro, coordenadas):
	linha  = coordenadas[0]
	coluna = coordenadas[1]

	valor_posicao = tabuleiro[linha][coluna]
	if (valor_posicao == -1 or valor_posicao == 1 ):
		print("Ja tinhas disparado nesta posicao, bala perdida ..")
	elif(valor_posicao > 1):
		print(bcolors.ANSI_GREEN + "Parabens acertaste no barco!" + bcolors.ANSI_RESET)
		tabuleiro[linha][coluna] = 1 #Registar que barco foi atacado
		if(barcoAbatido(tabuleiro,valor_posicao)):
			print(bcolors.ANSI_GREEN + "Parabens! barco afundado!" + bcolors.ANSI_RESET)
	else:
		tabuleiro[linha][coluna] = -1 #Registar posicao falhada
		print("Apenas havia agua..")

def coordenadaRandom():
	linha  = random.randint(0, 9)
	coluna = random.randint(0, 9)
	return (linha,coluna)

def orientacaoRandom():
	return random.randint(0, 1)

def posicaoRandom():
	return (coordenadaRandom(),orientacaoRandom())

'''
posicao (coordena, orientacao )
orientacao - 0 para horizontal, 1 para vertical
'''
def colocarBarco(tabuleiro, posicao, tamanhoBarco):
	orientacao = posicao[1]

	base    = posicao[0][ orientacao ]
	iterada = posicao[0][ (orientacao +1) %2]

	if(iterada + tamanhoBarco > 10):
		#Barco demasiado grande..
		return False
	else:
		for i in range (iterada, iterada+tamanhoBarco):
			if(orientacao == 0):
				if(tabuleiro[base][i] > 1):
					#Posicao preenchida
					return False
			else:
				if(tabuleiro[i][base] > 1):
					#Posicao preenchida
					return False
		#Preencher
		for i in range (iterada, iterada+tamanhoBarco):
			if(orientacao == 0):
				tabuleiro[base][i] = tamanhoBarco
			else:
				tabuleiro[i][base] = tamanhoBarco
	#Barco colocado com sucesso
	return True


def preencherTabuleiroAleatoriamente(tabuleiro):
	tamanho_barcos = [2,3,4,5]
#	tamanho_barcos = [2]
	for tamanho in tamanho_barcos:
		colocado = False
		while(not colocado):
			colocado = colocarBarco(tabuleiro, posicaoRandom(), tamanho)

def jogo():
	tabuleiro1 = criaTabuleiro()
	tabuleiro2 = criaTabuleiro()
	preencherTabuleiroAleatoriamente(tabuleiro1)
	preencherTabuleiroAleatoriamente(tabuleiro2)
	

	print("Bem vindos ao jogo BATALHA NAVAL")

	while(not tabuleiroCompleto(tabuleiro1) and not tabuleiroCompleto(tabuleiro2)):
		print("\n\nVez do ",bcolors.ANSI_PURPLE,bcolors.ANSI_BOLD,"Jogador 1:",sep="")
		resetColour()
		print("Tabuleiro do Adversario:")
		desenhaTabuleiro(tabuleiro2)
		coordenadas = pedeJogada()
		dispararTiro(tabuleiro2,coordenadas)

		print("\n\nVez do ",bcolors.ANSI_CYAN,bcolors.ANSI_BOLD,"Jogador 2:", sep="")
		resetColour()
		print("Tabuleiro do Adversario:")
		desenhaTabuleiro(tabuleiro1)
		coordenadas = pedeJogada()
		dispararTiro(tabuleiro1,coordenadas)
	print("\n\nWell done game is now over")
	if(tabuleiroCompleto(tabuleiro1)):
		print(bcolors.ANSI_CYAN,bcolors.ANSI_BOLD,"Jogador 2 foi o vencedor\n\n", sep="")
	else:
		print(bcolors.ANSI_PURPLE,bcolors.ANSI_BOLD,"Jogador 1 foi o vencedor\n\n", sep="")
	
	desenhaTabuleiroDescoberto(tabuleiro1)
	desenhaTabuleiroDescoberto(tabuleiro2)
	resetColour()
	
	
# jogo()
##### Testes
#tabuleiro = criaTabuleiro()
#print(colocarBarco(tabuleiro,((5,0),1),5))
#colocarBarcos(tabuleiro)
#desenhaTabuleiroDescoberto(tabuleiro)
#tabuleiro[0][0] = 3
#tabuleiro[0][1] = 3
#tabuleiro[6][0] = 4
#dispararTiro(tabuleiro,(0,0))
#print(tabuleiroCompleto(tabuleiro))
#dispararTiro(tabuleiro,(0,1))
#print(tabuleiroCompleto(tabuleiro))
#dispararTiro(tabuleiro,(6,0))
#print(tabuleiroCompleto(tabuleiro))
#desenhaTabuleiro(tabuleiro)
