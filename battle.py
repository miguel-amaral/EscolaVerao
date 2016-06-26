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
				colourCode = bcolors.ANSI_GREEN
			elif(coluna == 1):
				colourCode = bcolors.ANSI_RED
			else:
				colourCode = bcolors.ANSI_BLUE
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
 2 barco, sem danos
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
		print("Ja tinhas disparado nesta posicao, bala perdida ")
	elif(valor_posicao > 1):
		print("Parabens acertaste no barco!")
		tabuleiro[linha][coluna] = 1 #Registar que barco foi atacado
		if(barcoAbatido(tabuleiro,valor_posicao)):
			print("Parabens! barco afundado!")
	else:
		print("Apenas havia agua..")




##### Testes
#tabuleiro = criaTabuleiro()
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
