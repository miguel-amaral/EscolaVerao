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
			elif(coluna == 0):
				colourCode = bcolors.ANSI_BLUE
			elif(coluna == 1):
				colourCode = bcolors.ANSI_RED

			print(colourCode , "X", end="", sep="")
			resetColour()


		print(" ┃")
		numLinha = numLinha + 1
	desenhaLinhaBaixo()


'''tabuleiro = [[0,1,0,-1,0,0,0,0,0,0] for i in range(10)]
desenhaTabuleiro(tabuleiro)'''
